from bs4 import BeautifulSoup
from web_app.app import db
from web_app.models import Auction

class CollectList:
    def __init__(self):
        self.parsed_data = []

    def parse(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        table = soup.find('table', class_='k-selectable')

        if table:
            rows = table.find_all('tr')
            for row in rows:
                columns = row.find_all('td')
                if len(columns) == 6:

                    id_tag, image_tag, description_tag, _, _, _ = columns

                    property_id = id_tag.text.strip()

                    photo = image_tag.find('img', class_='grid-thumbnail')['src']

                    description_div = description_tag.find('div')
                    description = description_div.contents[0].strip()

                    state_city_element = description_div.find('strong')
                    if state_city_element is not None:
                        state_city_text = state_city_element.text.strip()
                        parts = state_city_text.split(',')
                        if len(parts) == 2:
                            state, city = parts
                        elif len(parts) == 3:
                            state, city, _ = parts
                        else:
                            state, city = "", state_city_text
                    else:
                        state, city = "", ""

                    self.parsed_data.append({
                        'auid': property_id,
                        'photo': photo,
                        'description': description,
                        'state': state.strip(),
                        'city': city.strip(),
                        'fetch_page': False,
                    })

    def save_to_database(self):
        for data in self.parsed_data:
            #missing sqft, zipcode, price
            auid, photo, description, state, city, fetch_page = data.values()
            #check if auid is in db, if so ignore
            exists = db.session.query(Auction.auid).filter_by(auid=auid).first()
            if exists is None:
                auction = Auction(auid=auid, photo=photo, description=description, state=state, city=city, fetch_page=fetch_page)
                db.session.add(auction)
        db.session.commit()

