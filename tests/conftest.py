import pytest
from app import create_app
from app import db
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    jupiter = Planet(id=1,
                name="Jupiter",
                description="Largest planet in our solar system",
                type="So much GAS THO")
    db.session.add_all([jupiter])

    db.session.commit()
