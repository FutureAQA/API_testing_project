import allure
from data.urls import Urls
from pages.create_pet import CreatePet
from pages.create_store import CreateStore
from src.utils.data_preparation.prepare_pet_test_data import PreparePetData
from src.utils.data_preparation.prepare_store_test_data import PrepareStoreData
from src.utils.http_methods import MyRequests
from src.utils.schemas.store.store_validator import StoreValidator
from src.utils.schemas.pets.pet_validator import PetValidator


class BasePage:
    create_store_data = CreateStore()
    urls = Urls()
    request = MyRequests()
    store = PrepareStoreData()
    create_pet_data = CreatePet()
    pet = PreparePetData()

    @allure.step("Prepare store data using provided information")
    def prepare_store_data(self, uid=None, pet_id=None, quantity=None, ship_date=None, status=None, complete=None):

        data = self.create_store_data.get_store_data(
            uid=self.store.get_id(uid=uid),
            pet_id=self.store.create_pet_id(pet_id=pet_id),
            quantity=self.store.create_quantity(quantity=quantity),
            ship_date=self.store.create_ship_date(ship_date=ship_date),
            status=self.store.create_status(status=status),
            complete=self.store.create_complete(complete=complete))
        return data

    @allure.step("Create pet with valid data")
    def create_pet_with_data(self, uid=None, name=None, category_value=None, photo_urls=None,
                             url_iteration=1, tags=None, tags_iteration=1, status=None):

        data = self.create_pet_data.get_pet_data(
            uid=self.pet.get_id(uid=uid),
            name=self.pet.create_name(name=name),
            category=self.pet.create_category(category_value=category_value),
            photo_urls=self.pet.create_photo_urls(photo_url_value=photo_urls, url_iteration=url_iteration),
            tags=self.pet.create_tags(tags_value=tags, tags_iteration=tags_iteration),
            status=self.pet.get_status(status=status)
        )
        return data

    @allure.step("Verify that the request or response body conforms to the expected JSON schema")
    def validate_response_store(self, response):
        """
        This method verifies that the request or response body conforms to the expected JSON schema
        :param response:
        :return: response or validation error message
        """
        if StoreValidator.validate_store_response(response=response) is True:
            return response
        else:
            return StoreValidator.validate_store_response(response=response)

    @allure.step("Verify that the request or response body conforms to the expected JSON schema")
    def validate_response_pet(self, response):
        """
        This method verifies that the request or response body conforms to the expected JSON schema
        :param response:
        :return: response or validation error message
        """
        if PetValidator.validate_pet_response(response=response) is True:
            return response
        else:
            return PetValidator.validate_pet_response(response=response)
