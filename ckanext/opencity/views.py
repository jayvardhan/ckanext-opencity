from flask import Blueprint


opencity = Blueprint(
    "opencity", __name__)


def page():
    return "Hello, opencity!"


opencity.add_url_rule(
    "/opencity/page", view_func=page)


def get_blueprints():
    return [opencity]
