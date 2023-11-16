from src.utils.data_preparation.prepare_basic_test_data import BaseTestData


class PrepareStoreData(BaseTestData):

    def create_pet_id(self, pet_id):
        if pet_id is None:
            store = self.get_all_store_data()
            return store.pet_id
        return pet_id

    def create_quantity(self, quantity):
        if quantity is None:
            store = self.get_all_store_data()
            return store.quantity
        return quantity

    def create_ship_date(self, ship_date):
        if ship_date is None:
            store = self.get_all_store_data()
            return store.ship_date
        return ship_date

    def create_status(self, status):
        if status is None:
            store = self.get_all_store_data()
            return store.status
        return status

    def create_complete(self, complete):
        if complete is None:
            store = self.get_all_store_data()
            return store.complete
        return complete
