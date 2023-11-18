import allure
from data.urls import Urls
from pages.create_pet import CreatePet
from pages.create_store import CreateStore
from src.utils.data_preparation.prepare_pet_test_data import PreparePetData
from src.utils.data_preparation.prepare_store_test_data import PrepareStoreData
from src.utils.http_methods import MyRequests
from src.utils.schemas.store.store_validator import StoreValidator
from src.utils.schemas.pets.pet_validator import PetValidator
from generator.generator import generate_fake_dict


class BasePage:
    create_store = CreateStore()
    urls = Urls()
    request = MyRequests()
    store = PrepareStoreData()
    create_pet = CreatePet()
    pet = PreparePetData()

    @allure.step("Prepare store data using the provided data")
    def prepare_store_data(self, uid=None, pet_id=None, quantity=None, ship_date=None,
                           status=None, complete=None, key=None):
        """
        This method prepares store data using the provided data
        :param uid: passed as a parameter to the get_id method
        :param pet_id: passed as a parameter to the create_pet_id method
        :param quantity: passed as a parameter to the create_quantity method
        :param ship_date: passed as a parameter to the create_ship_date method
        :param status: passed as a parameter to the create_status method
        :param complete: passed as a parameter to the create_complete method
        :param key: if the value is not None, then the key equal to the value of key is removed from the dictionary
        :return: prepared data
        """
        data = {
            "id": self.store.get_id(uid=uid),
            "petId": self.store.create_pet_id(pet_id=pet_id),
            "quantity": self.store.create_quantity(quantity=quantity),
            "shipDate": self.store.create_ship_date(ship_date=ship_date),
            "status": self.store.create_status(status=status),
            "complete": self.store.create_complete(complete=complete)
        }
        if key is not None:
            data.pop(key, None)
        return data

    @allure.step("Prepare pet data using the provided data")
    def prepare_pet_data(self, uid=None, name=None, category_value=None, photo_urls=None,
                         url_iteration=1, tags=None, tags_iteration=1, status=None, key=None):
        """
        This method prepares pet data using the provided data
        :param uid: passed as a parameter to the get_id method
        :param name: passed as a parameter to the create_name method
        :param category_value: passed as a parameter to the create_category method
        :param photo_urls: passed as a parameter to the create_photo_urls method
        :param url_iteration: the number of iterations of values, passed as a parameter to the create_photo_urls method
        :param tags: passed as a parameter to the create_tags method
        :param tags_iteration: the number of iterations of values, passed as a parameter to the create_tags method
        :param status: passed as a parameter to the get_status method
        :param key: if the value is not None, then the key equal to the value of key is removed from the dictionary
        :return: prepared data
        """
        data = {
            "id": self.pet.get_id(uid=uid),
            "name": self.pet.create_name(name=name),
            "category": self.pet.create_category(category_value=category_value),
            "photoUrls": self.pet.create_photo_urls(photo_url_value=photo_urls, url_iteration=url_iteration),
            "tags": self.pet.create_tags(tags_value=tags, tags_iteration=tags_iteration),
            "status": self.pet.get_status(status=status)
        }
        if key is not None:
            data.pop(key, None)
        return data

    @allure.step("Prepare category data using the provided data")
    def prepare_category(self, uid=None, name=None, key=None):
        """
        This method prepares category data using the provided data
        :param uid: passed as a parameter to the get_id method
        :param name: passed as a parameter to the create_category_name method
        :param key: if the value is not None, then the key equal to the value of key is added to the dictionary
        :return: prepared data
        """
        data = {
            "id": self.pet.get_id(uid=uid),
            "name": self.pet.create_category_name(name=name)
        }
        if key is not None:
            data.pop(key, None)
        return data

    @allure.step("Prepare tags data using the provided data")
    def prepare_tags(self, uid=None, name=None, key=None):
        """
        This method prepares category data using the provided data
        :param uid: passed as a parameter to the get_id method
        :param name: passed as a parameter to the create_category_name method
        :param key: if the value is not None, then the key equal to the value of key is added to the dictionary
        :return: prepared data
        """
        data = {
            "id": self.pet.get_id(uid=uid),
            "name": self.pet.create_tags_name(name=name)
        }
        if key is not None:
            data.pop(key, None)
        return data

    @allure.step("Add field in the body")
    def add_field_in_the_body(self, data):
        """
        This method adds field in the body
        :param data: data
        :return: updated data
        """
        add_dict = generate_fake_dict()
        data.update(add_dict)
        return data

    @allure.step("Verify that the request or response body conforms to the expected JSON schema")
    def validate_response_store(self, response):
        """
        This method verifies that the request or response body conforms to the expected JSON schema
        :param response: response_body
        :return: response if response is valid or validation error message
        """
        if StoreValidator.validate_store_response(response=response) is True:
            return response
        else:
            return StoreValidator.validate_store_response(response=response)

    @allure.step("Verify that the request or response body conforms to the expected JSON schema")
    def validate_response_pet(self, response):
        """
        This method verifies that the request or response body conforms to the expected JSON schema
        :param response: response_body
        :return: response if response is valid or validation error message
        """
        if PetValidator.validate_pet_response(response=response) is True:
            return response
        else:
            return PetValidator.validate_pet_response(response=response)
