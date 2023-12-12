import os
from unittest import TestCase

from flask import session

from web_app.app import create_app
from web_app.index_page import index_page
from web_app.environment import Environment

class TestIndexPage(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.index_page = index_page()

    def test_index(self) -> None:
        #env = Environment(port=8080, secret_key="just testing", host_url="localhost", database_url="foredeals", use_flask_debug_mode=False)
        client = create_app().test_client()
        response = client.get("/")

        self.assertEqual(200, response.status_code)
        self.assertIn("Select a state", response.text)

    def test_select_and_submit(self) -> None:
        #env = Environment(port=8080, secret_key="just testing", host_url="localhost", database_url="foredeals", use_flask_debug_mode=False)
        client = create_app().test_client()

        # Select California from the form
        response = client.get("/state/CA")

        self.assertEqual(200, response.status_code)
        self.assertIn("California", response.text)
