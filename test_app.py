from app import app

def test_home():
    # Create a test client for the Flask application
    client = app.test_client()

    # Send a GET request to the home route and check for 200 status
    response = client.get("/")
    assert response.status_code == 200

    # Send a POST request with form data (name = "John") and check for 200 status
    response = client.post("/", data={"nm": "John"})
    assert response.status_code == 200
