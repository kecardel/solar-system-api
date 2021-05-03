from flask import Blueprint, make_response, jsonify
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

@planets_bp.route("", methods=["GET"], strict_slashes=False)
def get_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "type": planet.type
        })
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])

def get_one_planet(planet_id):

    try:

        planet = Planet.query.get(int(planet_id))
    
    # except AttributeError...not attribute error, this is getting thrown later in the code.

    except ValueError:

        return make_response(f"Planet ID must be an integer.", 404)

    if planet == None:
        return make_response(f"Planet ID is invalid.", 404)


    elif request.method == "GET":

        return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "type": planet.type
    }

    elif request.method == "PUT":
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.type = form_data["type"]

        db.session.commit()

        return make_response(f"Planet #{planet.id} successfully updated") 

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Book #{planet.id} successfully deleted")
