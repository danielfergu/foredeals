import sys
sys.path.append('src/applications/')
from flask import session
from web_app.app import create_app, db
from web_app.environment import Environment
from data_collector.WebFetcher import WebFetcher
from data_collector.CollectList import CollectList
from data_collector.CollectAuction import CollectAuction
from web_app.models import Auction
from dotenv import load_dotenv
import time
import random

class CollectData:
    def __init__(self, url=None, html_content=None):
        self.app = create_app(Environment.from_env(), testing=False)
        self.app_context = self.app.app_context()
        self.app_context.push()
        #db.create_all()
        self.list_url = 'https://www.bid4assets.com/search/#t=ps%7Cc=22%7Ckt=a%7Cas=l%7Cls=state%7Cdr=6'
        self.auction_url = 'https://www.bid4assets.com/auction/index/number'
        self.states = ['CA', 'TX']

    def collect(self):
        for state in self.states:
            state_url = self.list_url.replace('state', state)
            collector = WebFetcher(state_url)
            collector.run()

            alist = CollectList()
            alist.parse(collector.response)
            alist.save_to_database()

            sleep_duration = random.uniform(1, 5)
            time.sleep(sleep_duration)
            
            auids = db.session.query(Auction.auid).filter_by(fetch_page=False).all()

            for auid_tuple in auids:
                auid = auid_tuple[0]
                auction_url = self.auction_url.replace('number', str(auid))

                collector = WebFetcher(auction_url)
                collector.run()

                auct = CollectAuction()
                auct.parse(collector.response)
                auct.save_to_database()
                #turn messaging queue on
                #auct.send_to_analyzer()
                
                sleep_duration = random.uniform(1, 5)
                time.sleep(sleep_duration)


if __name__ == '__main__':
    print("This program will fetch and parse about 40 pages of auctions. There's a wait between requests so auction companies wont block this ip address.")
    collector = CollectData()
    collector.collect()
