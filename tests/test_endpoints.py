from fastapi.testclient import TestClient
from grocery_api.main import app

client = TestClient(app)


def test_home_should_respond_with_hello_world_message():
    response = client.get("/")
    assert response.json() == {"message": "Hello World!"}
