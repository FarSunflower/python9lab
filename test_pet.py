from data import Routes
from faker import Faker

class TestPet:
    def test_pet_by_id(self, api_url, create_new_pet):
        pet_id = create_new_pet
        response = api_url.get(Routes.list_pets + f"/{pet_id}")
        assert response.status_code == 200
        
    def test_change_pet(self, api_url, update_pet):
        pet = update_pet
        response = api_url.put(Routes.list_pets, json = pet)
        assert response.status_code == 200
        
