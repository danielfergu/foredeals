from typing import Union
from uuid import UUID

from flask import Blueprint, render_template, g, flash, redirect, request, session, url_for
from flask.typing import ResponseReturnValue

import string
import random

from web_app.models import db, User, UserReq

def notification_page() -> Blueprint:
    api = Blueprint("notification_page", __name__)

    def generate_password():
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for i in range(12))

    @api.route("/notification", methods=["GET", "POST"])
    def notification_form():
        if request.method == "POST" or request.method == "GET":
            # Retrieve data from the request (form or query parameters)
            zip_code = request.form.get("zip_code") if request.method == "POST" else request.args.get("zip_code")
            sqft_price = float(request.form.get("sqft_price") if request.method == "POST" else request.args.get("sqft_price"))
            min_sqft = float(request.form.get("min_sqft") if request.method == "POST" else request.args.get("min_sqft"))
            email = request.form.get("email") if request.method == "POST" else request.args.get("email")

            # Generate a random password for the user
            password = generate_password()

            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()

            user_id = new_user.id

            new_user_req = UserReq(zip_code=zip_code, sqft_price=sqft_price, min_sqft=min_sqft, user_id=user_id)
            db.session.add(new_user_req)
            db.session.commit()

            db.session.commit()

            # Redirect to a thank you page or any other desired page
            return redirect("/thank_you")

        # Render the form for GET requests
        return render_template("notification.html")

    @api.route("/thank_you")
    def thank_you():
        return "Thank you for your interest! We'll send you notifications."


    return api
