import os
import sys
sys.path.append('src/applications/')
from flask import session
from web_app.app import create_app, db
from web_app.environment import Environment
from web_app.models import Auction
from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent

class AnalyzeData:
    def __init__(self, auction_id=None, auction_auid=None, auction_price=None, auction_zip_code=None, auction_sqft=None):
        self.app = create_app(Environment.from_env(), testing=False)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.csv = 'sqft_price.csv'
        self.market_price = None
        self.sqft_price = None
        self.auction_zip_code = auction_zip_code
        self.auction_id = auction_id

    def calculate_sqft_price(self):
        if self.auction_sqft != 0:
            self.sqft_price = self.auction_price / self.auction_sqft
        else:
            self.sqft_price = 0.0

    def get_csv_prices(self):
        with open(self.csv, 'r') as file:
            next(file)
            csv_data = [line.strip().split(',') for line in file.readlines()]
        return {row[0]: float(row[1]) for row in csv_data}

    def get_market_price(self):
        prices = self.get_csv_prices()
        self.market_price = prices.get(self.auction_zip_code, None)

    def update_auction_database(self):
        auction = Auction.query.get(self.auction_id)
        if auction:
            auction.market_price = self.market_price * self.auction_sqft
            db.session.commit()

    def loop_user_reqs(self):
        user_reqs = UserReq.query.all()
        for user_req in user_reqs:
            if (
                auction_sqft >= user_req.min_sqft
                and auction_price >= user_req.min_price
            ):
                self.send_email(user_req.email, self.auction_auid)

    def send_email(self, email, auction_auid):
        sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        from_email = From("notifications@foredeals-5bef4b23bc51.com")
        to_email = To(email)
        subject = Subject("Auction Notification")
        content = PlainTextContent(f"Click the link to view auction details: https://www.bid4assets.com/auction/index/{auction_auid}")
        message = Mail(from_email, to_email, subject, content)
        sg.send(message)

    def analyze(self):
        self.calculate_sqft_price()
        self.get_market_price()
        self.update_auction_database()
        self.loop_user_reqs()

if __name__ == '__main__':
    analyzer = AnalyzeData()
    analyzer.analyze()
