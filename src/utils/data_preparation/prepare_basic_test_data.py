import allure
from generator.generator import generated_pet, generated_store, generated_pet_tags_and_category, generated_user


class BaseTestData:

    @allure.step("Get all pet data")
    def get_all_pet_data(self):
        """
        This method generates pet data and returns it
        :return: pet data
        """
        return next(generated_pet())

    @allure.step("Get all store data")
    def get_all_store_data(self):
        """
        This method generates store data and returns it
        :return: store data
        """
        return next(generated_store())

    @allure.step("Get all user data")
    def get_all_user_data(self):
        """
        This method generates user data and returns it
        :return: user data
        """
        return next(generated_user())

    @allure.step("Get pet category and tags name")
    def get_category_and_tags_name(self):
        """
        This method generates pet category and tags name and returns it
        :return:
        """
        return next(generated_pet_tags_and_category())

    def get_id(self, uid):
        if uid is None:
            pet = self.get_all_pet_data()
            return pet.uid
        return uid
