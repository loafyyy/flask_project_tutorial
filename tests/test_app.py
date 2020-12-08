import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    ''' Test that home page shows "Hello, World!" '''
    rv = client.get("/")
    assert b"Hello, World!" == rv.data

def test_hello_page(client):
    ''' Test that hello page shows "Hello!" '''
    rv = client.get("/hello/")
    assert  rv.data == b'<!doctype html>\n<title>Hello from Flask</title>\n\n  <h1>Hello!</h1>\n'
    assert "Hello!" in str(rv.data)

def test_hello_page_with_name(client):
    ''' Test that hello page with a name shows "Hello [name]!" '''
    name = "test_name"
    rv = client.get(f"/hello/{name}")
    assert f"Hello {name}!" in str(rv.data)