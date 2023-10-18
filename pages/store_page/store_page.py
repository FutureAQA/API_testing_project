from generator.generator import generated_store
from pages.create_store import CreateStore
from src.utils.http_methods import MyRequests
from data.urls import Urls
from src.utils.schemas.store.store_validator import StoreValidator


class StorePage:
    create_store_data = CreateStore()
    urls = Urls()
    request = MyRequests()

    def get_all_stores(self):
        store = next(generated_store())
        return store

    def create_store_with_valid_data(self):
        url = self.urls.STORES_URL
        store = self.get_all_stores()
        data = self.create_store_data.get_store_data(
            uid=store.uid,
            pet_id=store.pet_id,
            quantity=store.quantity,
            ship_date="store.ship_date",
            status=store.status,
            complete=store.complete)
        response = self.request.post(url=url, data=data)
        StoreValidator.validate_store_response(response=response)
        return response
