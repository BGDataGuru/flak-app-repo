import pytest
from app import app
import json

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    res = client.get("/users")
    res_json = res.get_json()

    assert res.status_code == 200
    assert res_json[0]['id'] == 1
    assert res_json[0]['email'] =='john@example.com'

def test_post(client):
    res = client.post("/users",
                      json = {"id": 3, "name": "Bhavesh Gawade", "email": "bhavesh.gawade@gmail.com"})

    res_json = res.get_json()
    assert res.status_code == 201