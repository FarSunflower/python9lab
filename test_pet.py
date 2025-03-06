from data import Routes

class TestPet:
    def test_pet_by_id(self, api_url, create_new_pet):
        pet_id = create_new_pet
        response = api_url.get(Routes.list_pets + f"/{pet_id}")
        assert response.status_code == 200