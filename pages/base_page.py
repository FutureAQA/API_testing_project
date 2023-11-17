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
    create_store = CreateStore()
    urls = Urls()
    request = MyRequests()
    store = PrepareStoreData()
    create_pet = CreatePet()
    pet = PreparePetData()

    @allure.step("Prepare store data using the provided data")
    def prepare_store_data(self, uid=None, pet_id=None, quantity=None, ship_date=None, status=None, complete=None):

        data = {
            "id": self.store.get_id(uid=uid),
            "petId": self.store.create_pet_id(pet_id=pet_id),
            "quantity": self.store.create_quantity(quantity=quantity),
            "shipDate": self.store.create_ship_date(ship_date=ship_date),
            "status": self.store.create_status(status=status),
            "complete": self.store.create_complete(complete=complete)
        }
        return data

    def create_store_data(self, dct, key=None):
        if key is not None:
            dct[key] = None

        data = self.create_store.get_store_data(
            uid=dct["id"],
            pet_id=dct["petId"],
            quantity=dct["quantity"],
            ship_date=dct["shipDate"],
            status=dct["status"],
            complete=dct["complete"]
        )
        return data

    @allure.step("Prepare pet data using the provided data")
    def prepare_pet_data(self, uid=None, name=None, category_value=None, photo_urls=None,
                         url_iteration=1, tags=None, tags_iteration=1, status=None):
        """
        This method prepares pet data using the provided data
        :param uid:
        :param name:
        :param category_value:
        :param photo_urls:
        :param url_iteration:
        :param tags:
        :param tags_iteration:
        :param status:
        :return:
        """
        data = {
            "id": self.pet.get_id(uid=uid),
            "name": self.pet.create_name(name=name),
            "category": self.pet.create_category(category_value=category_value),
            "photoUrls": self.pet.create_photo_urls(photo_url_value=photo_urls, url_iteration=url_iteration),
            "tags": self.pet.create_tags(tags_value=tags, tags_iteration=tags_iteration),
            "status": self.pet.get_status(status=status)
        }
        return data

    def create_pet_data(self, dct, key=None):
        if key is not None:
            dct[key] = None

        data = self.create_pet.get_pet_data(
            uid=dct["id"],
            name=dct["name"],
            category=dct["category"],
            photo_urls=dct["photoUrls"],
            tags=dct["tags"],
            status=dct["status"]
        )
        return data

    @allure.step("Create pet with valid data")
    def create_pet_with_data(self, uid=None, name=None, category_value=None, photo_urls=None,
                             url_iteration=1, tags=None, tags_iteration=1, status=None):

        data = self.create_pet.get_pet_data(
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
