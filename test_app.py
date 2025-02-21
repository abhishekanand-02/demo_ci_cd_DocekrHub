from app import app

def test_home():
    # Create a test client for the Flask application
    client = app.test_client()

    # Send a GET request to the home route
    response = client.get("/")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the form asking for the user's name is in the response
    assert b"Please Enter Your Name:" in response.data

    # Send a POST request with form data (name = "John")
    response = client.post("/", data={"nm": "John"})

    # Assert the response contains the correct welcome message with the entered name
    assert b"Welcome John!" in response.data
