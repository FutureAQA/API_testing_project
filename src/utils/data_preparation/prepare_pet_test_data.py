from src.utils.data_preparation.prepare_basic_test_data import BaseTestData


class PreparePetData(BaseTestData):

    def create_name(self, name):
        if name is None:
            pet = self.get_all_pet_data()
            return pet.name
        return name

    def create_category(self, category_value=None):
        if category_value is None:
            pet = self.get_all_pet_data()
            return pet.category
        return category_value

    def create_photo_urls(self, url_iteration, photo_url_value=None):
        if photo_url_value is None:
            lst = []
            for i in range(url_iteration):
                pet = self.get_all_pet_data()
                lst.append(pet.photo_urls)
            return lst
        return photo_url_value

    def create_tags(self, tags_iteration, tags_value=None):
        if tags_value is None:
            lst = []
            for i in range(tags_iteration):
                pet = self.get_all_pet_data()
                lst.append(pet.tags)
            return lst
        return tags_value

    def get_status(self, status=None):
        if status is None:
            pet = self.get_all_pet_data()
            return pet.status
        return status

    def create_category_name(self, name=None):
        if name is None:
            name = self.get_category_and_tags_name()
            return name.category_name
        return name

    def create_tags_name(self, name=None):
        if name is None:
            name = self.get_category_and_tags_name()
            return name.tags_name
        return name
