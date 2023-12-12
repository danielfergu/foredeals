from bs4 import BeautifulSoup
from web_app.app import db
from web_app.models import Auction
import re
from datetime import datetime
import json, pika

class CollectAuction:
    def __init__(self):
        self.parsed_data = []

    def parse(self, content):
        soup = BeautifulSoup(content, 'html.parser')

        span_element = soup.find('span', style="font-size: 1.8em")
        if span_element:
            number = span_element.get_text().split("#")[1].strip()

        sqft = self.find_sqft(content)
        if sqft is None:
            sqft = 0
        elif isinstance(sqft, str):
            sqft = sqft.replace(',', '')

        span_element = soup.find('span', id='current-bid-span')
        if span_element:
            price = span_element.get_text().replace("$", "")
            price = price.replace(',', '')

        zipcode_tag = soup.find('td', string='Location:')
        if zipcode_tag:
            location_text = zipcode_tag.find_next('td').text.strip()
            zipcode = location_text.split()[-1] if location_text else None
            zipcode = zipcode.replace(',', '')

        th_element = soup.find('th', string='Auction Started:')
        if th_element:
            td_element = th_element.find_next_sibling('td')    
            date_string = td_element.get_text(strip=True)

        try:
            date_start = self.string_to_date(date_string)
        except UnboundLocalError:
            date_start = datetime.now()

        span_element = soup.find('span', id='actual-close-time-block')
        if span_element:
            close_time_str = span_element.get_text(strip=True)
            date_end = self.string_to_date(close_time_str)
        else:
            date_end = datetime.now()

        try:
            zipcode = float(zipcode)
        except ValueError:
            zipcode = 0

        try:
            price = float(price)
        except UnboundLocalError:
            price = 1

        self.parsed_data.append({
            'auid': int(number),
            'fetch_page': True,
            'sqft': float(sqft),
            'price': float(price),
            'zip_code': float(zipcode),
            'date_start': date_start,
            'date_end': date_end
        })

    def send_to_analyzer(self):
        conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        channel = conn.channel()
        channel.queue_declare(queue="auctions")
        channel.basic_publish(exchange="", routing_key="auctions",
                              body=json.dumps({
                                  "auction_auid": self.parsed_data.auction_auid,
                                  "auction_price": self.parsed_data.price,
                                  "auction_zip_code": self.parsed_data.zip_code
                                  "auction_sqft": self.parsed_data.sqft
                              }))

    def save_to_database(self):
        for data in self.parsed_data:
            auid, fetch_page, sqft, price, zip_code, date_start, date_end = data.values()
            auction = Auction.query.filter_by(auid=auid).first()
            auction.fetch_page = fetch_page
            auction.sqft = sqft
            auction.price = price
            auction.zip_code = zip_code
            auction.date_start = date_start
            auction.date_end = date_end
        db.session.commit()

    def string_to_date(self, date_string):
        month = int(date_string[0:2])
        day = int(date_string[3:5])
        year = 2000 + int(date_string[6:8])
        hour = int(date_string[9:11])
        minutes = int(date_string[12:14])
        date = datetime(year, month, day, hour, minutes)  
        return date

    def convert_acre_to_sqft(self, value):
        return int(value) * 43560

    def find_sqft(self, text):
        pattern = re.compile(r'\b(\d+)\s*(?:sq\s*ft|sqft|sq\.?\s*ft|sqft|acre)\b', re.IGNORECASE)
        match = pattern.search(text)
        
        if match:
            number = match.group(1)
            unit = match.group().lower()
            
            if 'acre' in unit:
                return self.convert_acre_to_sqft(number)
            else:
                return int(number)
        else:
            return None