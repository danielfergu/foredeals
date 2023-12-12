from typing import Union

from flask import Blueprint, render_template, session, redirect
from flask.typing import ResponseReturnValue
from web_app.models import Auction


def index_page() -> Blueprint:
    api = Blueprint("index_page", __name__)

    states = {
        "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA",
        "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", "Florida": "FL", "Georgia": "GA",
        "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
        "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD", "Massachusetts": "MA",
        "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO", "Montana": "MT",
        "Nebraska": "NE", "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM",
        "New York": "NY", "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK",
        "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC", "South Dakota": "SD",
        "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT", "Virginia": "VA", "Washington": "WA",
        "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY"
    }

    @api.before_request
    def authenticate_user_filter() -> Union[None, ResponseReturnValue]:
        if session.get("username", None) is not None:
            return redirect("/dashboard")

        return None

    @api.get("/logout")
    def logout() -> ResponseReturnValue:
        session.clear()
        return redirect("/")

    @api.get("/")
    def index() -> ResponseReturnValue:

        return render_template("index.html", state_options=states, selected_state=None)


    @api.route("/state/<state_code>")
    def get_auctions(state_code):

        auctions = Auction.query.filter_by(state=state_code).all()
        reversed_states = {v: k for k, v in states.items()}
        full_state_name = reversed_states.get(state_code.upper(), "Invalid state code")

        return render_template("auction.html", state_code=state_code, state_name=full_state_name, auctions=auctions)


    return api
