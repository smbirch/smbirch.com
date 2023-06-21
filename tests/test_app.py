import pytest
from flask import Flask


@pytest.fixture
def client():
    app = Flask(__name__)
    app.config["TESTING"] = True

    @app.route("/", methods=["GET"])
    def index():
        return "Hello, World!"

    with app.test_client() as client:
        yield client


def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
