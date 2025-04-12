import pytest
from main import app, db, NecktieDoctor, NecktieDistrict, NecktieCategory

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:z0h3T0WC84KLoN0I@tonelessly-contiguous-terrapin.data-1.use1.tembo.io:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.test_client() as client:
        yield client


def test_create_doctor(client):
    response = client.post('/doctor', json={
        "first_name": "Jamie",
        "last_name": "Lai",
        "category_id": 1,
        "district_id": 1,
        "price_range_low": 300,
        "price_range_high": 500,
        "languages": ["English", "Mandarin"],
        "bio": "Great ENT specialist"
    })

    assert response.status_code == 201
    assert b"Doctor created" in response.data


def test_get_doctor(client):
    response = client.get('/doctor/1')
    data = response.get_json()

    assert response.status_code == 200
    assert data["first_name"] == "John"
    assert data["district"] == "Central"


def test_filter_doctors_by_district_and_by_price_1000(client):
    response = client.get('/doctor?district=Central&price_max=1000')
    data = response.get_json()

    assert response.status_code == 200
    assert data[2]["first_name"] == "Createfirst"
    assert data[0]["district"] == "Central"

def test_filter_doctors_by_district_and_by_price_600(client):
    response = client.get('/doctor?district=Central&price_max=600')
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) >= 6