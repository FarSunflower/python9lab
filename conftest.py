import pytest
import requests
from faker import Faker
from data import Routes

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get(self, path = "/", params = None):
        url = f"{self.base_url}{path}"
        return requests.get(url = url, params = params)
    
    def post(self, path = "/", json = None):
        url = f"{self.base_url}{path}"
        return requests.post(url = url, json = json)
    
    def put(self, path = "/", json = None):
        url = f"{self.base_url}{path}"
        return requests.put(url = url, json = json)

    def delete(self, path = "/"):
        url = f"{self.base_url}{path}"
        return requests.delete(url = url)
    
    
    
@pytest.fixture
def api_url():
    return ApiClient(base_url="https://petstore.swagger.io/v2")

def delete_pet(api_url, pet_id):
    response = api_url.delete(Routes.list_pets+f"/{pet_id}")
    assert response.status_code == 200


@pytest.fixture
def create_new_pet(api_url):
    fake = Faker()
    new_pet = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "CATEGORY"
        },
        "name": f"{fake.first_name()}",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
            "id": 0,
            "name": "string"
            }
        ],
        "status": "available"
    }
    response = api_url.post(Routes.list_pets, json = new_pet)
    assert response.status_code == 200
    print(response.json())
    
    response_data = response.json()
    assert response_data['id'] is not None
    created_id = response_data['id']
    yield created_id
    delete_pet(api_url=api_url, pet_id=created_id)

@pytest.fixture
def update_pet(api_url, create_new_pet):
    fake = Faker()
    new_pet = create_new_pet
    pet = {
            "id": new_pet,
            "category": {
                "id": 0,
                "name": "CATEGORY"
            },
            "name": f"{fake.first_name()}",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                "id": 0,
                "name": "string"
                }
            ],
            "status": "available"
    }
    yield pet 
    