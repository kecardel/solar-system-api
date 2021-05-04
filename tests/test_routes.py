def test_get_all_planets_(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Jupiter",
        "description": "Largest planet in our solar system",
        "type": "So much GAS THO"
    },
        {
        "id": 2,
        "name": "Saturn",
        "description": "The rings one, duh.",
        "type": "gas giant"
        }]

def test_get_one_planet(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Jupiter",
        "description": "Largest planet in our solar system",
        "type": "So much GAS THO"
    }

def test_get_one_planet_no_match(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == None

def test_post_planet(client, planet_data):
    response = client.post("/planets", json=planet_data)
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == f"Planet Paper has been added."