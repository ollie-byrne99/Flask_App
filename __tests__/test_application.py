import pytest
from application import app
from application.locations import routes

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    data = response.get_json()
    
    assert response.status_code == 200
    
    expected_data = {
        "message": "Welcome",
        "description": "Locations API",
        "endpoints": ["GET /"]
    }
    
    assert data == expected_data

def test_locations(client):
    response = client.get("/locations")
    data = response.get_json()
    
   
    assert len(data['locations']) == 5

    
    required_fields = ["id", "name", "address", "description", "date_posted",
                       "start_date", "end_date", "business_name", "contact_email",
                       "contact_phone", "price_per_day", "latitude", "longitude",
                       "is_available"]
    
    for location in data['locations']:
        for field in required_fields:
            assert field in location

    assert response.status_code == 200
