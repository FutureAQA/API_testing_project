from src.logger.logger import get_logs

logger = get_logs(r"pages\create_store.py")


class CreateStore:

    def get_id(self, uid):
        if uid is not None:
            return {"id": uid}

    def get_pet_id(self, pet_id):
        if pet_id is not None:
            return {"petId": pet_id}

    def get_quantity(self, quantity):
        if quantity is not None:
            return {"quantity": quantity}

    def get_ship_date(self, ship_date):
        if ship_date is not None:
            return {"shipDate": ship_date}

    def get_status(self, status):
        if status is not None:
            return {"status": status}

    def get_complete(self, complete):
        if complete is not None:
            return {"complete": complete}

    def get_store_data(self, uid=None, pet_id=None, quantity=None, ship_date=None, status=None, complete=None):
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
