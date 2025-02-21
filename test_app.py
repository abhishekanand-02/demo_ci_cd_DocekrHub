from app import app

def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    assert b"Please Enter Your Name: " in response.data

    response = client.post("/", data={"nm": "John"})

    assert b"Welcome John!" in response.data
