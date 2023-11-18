"""
This module contains the CreatePet class
"""

from src.logger.logger import get_logs

logger = get_logs(r"pages\create_pet.py")


class CreatePet:
    @staticmethod
    def get_id(uid):
        """
        This method returns id
        :param uid: passed as a parameter
        :return: id
        """
        if uid is not None:
            return {"id": uid}

    @staticmethod
    def get_name(name):
        """
        This method returns name
        :param name: passed as a parameter
        :return: name
        """
        if name is not None:
            return {"name": name}

    @staticmethod
    def get_category(category):
        """
        This method returns category
        :param category: passed as a parameter
        :return: category
        """
        if category is not None:
            return {"category": category}

    @staticmethod
    def get_photo_urls(photo_urls):
        """
        This method returns photo_urls
        :param photo_urls: passed as a parameter
        :return: photo_urls
        """
        if photo_urls is not None:
            return {"photoUrls": photo_urls}

    @staticmethod
    def get_tags(tags: dict):
        """
        This method returns tags
        :param tags: passed as a parameter
        :return: tags
        """
        if tags is not None:
            return {"tags": tags}

    @staticmethod
    def get_status(status):
        """
        This method returns status
        :param status: passed as a parameter
        :return: status
        """
        if status is not None:
            return {"status": status}

    def get_pet_data(self, uid=None, name=None, category=None, photo_urls=None, tags=None, status=None):
        """
        This method prepares pet data using the provided data
        :param uid: passed as a parameter to the get_id method
        :param name: passed as a parameter to the get_name method
        :param category: passed as a parameter to the get_category method
        :param photo_urls: passed as a parameter to the get_photo_urls method
        :param tags: passed as a parameter to the get_tags method
        :param status: passed as a parameter to the get_status method
        :return: prepared data
        """
        data = {}

        id_value = self.get_id(uid)
        if id_value:
            data["id"] = id_value["id"]

        name_value = self.get_name(name)
        if name_value:
            data["name"] = name_value["name"]

        category_value = self.get_category(category)
        if category_value:
            data["category"] = category_value["category"]

        photo_urls_value = self.get_photo_urls(photo_urls)
        if photo_urls_value:
            data["photoUrls"] = photo_urls_value["photoUrls"]

        tags_value = self.get_tags(tags)
        if tags_value:
            data["tags"] = tags_value["tags"]

        status_value = self.get_status(status)
        if status_value:
            data["status"] = status_value["status"]

        logger.info(f"Request data: {data}")
        return data
