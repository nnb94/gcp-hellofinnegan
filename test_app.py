from main import app

def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data

if __name__ == "__main__":
    test_home_route()
    print("Test passed!")
