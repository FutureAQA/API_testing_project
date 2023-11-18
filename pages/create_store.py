"""
This module contains the CreateStore class
"""

from src.logger.logger import get_logs

logger = get_logs(r"pages\create_store.py")


class CreateStore:
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
    def get_pet_id(pet_id):
        """
        This method returns pet_id
        :param pet_id: passed as a parameter
        :return: pet_id
        """
        if pet_id is not None:
            return {"petId": pet_id}

    @staticmethod
    def get_quantity(quantity):
        """
        This method returns quantity
        :param quantity: passed as a parameter
        :return: quantity
        """
        if quantity is not None:
            return {"quantity": quantity}

    @staticmethod
    def get_ship_date(ship_date):
        """
        This method returns ship_date
        :param ship_date: passed as a parameter
        :return: ship_date
        """
        if ship_date is not None:
            return {"shipDate": ship_date}

    @staticmethod
    def get_status(status):
        """
        This method returns status
        :param status: passed as a parameter
        :return: status
        """
        if status is not None:
            return {"status": status}

    @staticmethod
    def get_complete(complete):
        """
        This method returns complete
        :param complete: passed as a parameter
        :return: complete
        """
        if complete is not None:
            return {"complete": complete}

    def get_store_data(self, uid=None, pet_id=None, quantity=None, ship_date=None, status=None, complete=None):
        """
        This method prepares store data using the provided data
        :param uid: passed as a parameter to the get_id method
        :param pet_id: passed as a parameter to the get_pet_id method
        :param quantity: passed as a parameter to the get_quantity method
        :param ship_date: passed as a parameter to the get_ship_date method
        :param status: passed as a parameter to the get_status method
        :param complete: passed as a parameter to the get_complete method
        :return: prepared data
        """
        data = {}

        id_value = self.get_id(uid)
        if id_value:
            data["id"] = id_value["id"]

        pet_id_value = self.get_pet_id(pet_id)
        if pet_id_value:
            data["petId"] = pet_id_value["petId"]

        quantity_value = self.get_quantity(quantity)
        if quantity_value:
            data["quantity"] = quantity_value["quantity"]

        ship_date_value = self.get_ship_date(ship_date)
        if ship_date_value:
            data["shipDate"] = ship_date_value["shipDate"]

        status_value = self.get_status(status)
        if status_value:
            data["status"] = status_value["status"]

        complete_value = self.get_complete(complete)
        if complete_value:
            data["complete"] = complete_value["complete"]

        logger.info(f"Request data: {data}")
        return data
