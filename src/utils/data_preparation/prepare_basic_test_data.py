import allure
from generator.generator import generated_pet, generated_store


class BaseTestData:

    @allure.step("Get all pet data")
    def get_all_pet_data(self):
        """
        This method generates pet data and returns it
        :return: pet data
        """
        pet = next(generated_pet())
        return pet

    @allure.step("Get all store data")
    def get_all_store_data(self):
        """
        This method generates store data and returns it
        :return: store data
        """
        store = next(generated_store())
        return store

    def get_id(self, uid):
        if uid is None:
            pet = self.get_all_pet_data()
            return pet.uid
        return uid

