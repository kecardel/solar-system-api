from flask import Blueprint, make_response
from app.models.planet import Planet
from flask import request
from app import db

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"], strict_slashes=False)
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(name = request_body["name"],
                    description = request_body["description"],
                    type = request_body["type"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} has been added.", 201)

# @planets_bp.route("", methods=["GET"], strict_slashes=False)
# def get_planets():
