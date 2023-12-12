import os
from unittest import TestCase

from flask import session

from web_app.app import create_app, db
from web_app.environment import Environment
from web_app.models import User, UserReq, Auction

from dotenv import load_dotenv

class TestModels(TestCase):
    def setUp(self):
        # Create a test app with the testing flag set to True
        self.app = create_app(Environment.from_env(), testing=True)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_model(self):
        with self.app.app_context():
            # Create a sample user
            user = User(email='test@example.com', name='Test User', password='testpassword')
            db.session.add(user)
            db.session.commit()

            # Retrieve the user from the database
            retrieved_user = User.query.filter_by(email='test@example.com').first()

            # Check if the user is correctly stored and retrieved
            self.assertIsNotNone(retrieved_user)
            self.assertEqual(retrieved_user.name, 'Test User')

    def test_user_req_model(self):
        with self.app.app_context():
            # Create a sample user and user_req
            #user = User(email='test@example.com', name='Test User', password='testpassword')
            user_req = UserReq(user_id='124', zip_code='12345', sqft_price=100.5, min_sqft=50)
            #db.session.add(user)
            db.session.add(user_req)
            db.session.commit()

            # Retrieve the user_req from the database
            retrieved_user_req = UserReq.query.filter_by(zip_code='12345').first()

            # Check if the user_req is correctly stored and retrieved
            self.assertIsNotNone(retrieved_user_req)
            self.assertEqual(retrieved_user_req.sqft_price, 100.5)

    def test_auction_model(self):
        with self.app.app_context():
            # Create a sample auction
            auction = Auction(
                auid='22222',
                zip_code='54321',
                price=100.0,
                state='California',
                city='Los Angeles',
                photo='path/to/photo.jpg',
                description='Test Auction',
                sqft=200.0
            )
            db.session.add(auction)
            db.session.commit()

            # Retrieve the auction from the database
            retrieved_auction = Auction.query.filter_by(auid='22222').first()

            # Check if the auction is correctly stored and retrieved
            self.assertIsNotNone(retrieved_auction)
            self.assertEqual(retrieved_auction.price, 100.0)
