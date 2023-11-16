from src.logger.logger import get_logs

logger = get_logs(r"pages\create_pet.py")


class CreatePet:

    def get_id(self, uid):
        if uid is not None:
            return {"id": uid}

    def get_name(self, name):
        if name is not None:
            return {"name": name}

    def get_category(self, category):
        if category is not None:
            return {"category": category}

    def get_photo_urls(self, photo_urls):
        if photo_urls is not None:
            return {"photoUrls": photo_urls}

    def get_tags(self, tags: dict):
        if tags is not None:



            return {"tags": tags}

    def get_status(self, status):
        if status is not None:
            return {"status": status}

    def get_pet_data(self, uid=None, name=None, category=None, photo_urls=None, tags=None, status=None):
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
