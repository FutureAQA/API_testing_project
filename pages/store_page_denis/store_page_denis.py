import allure
from pydantic import ValidationError
from src.logger.logger import get_logs
from generator.generator import generated_store
from pages.create_store import CreateStore
from src.utils.http_methods import MyRequests
from data.urls import Urls
from src.utils.schemas.store.store_validator import StoreValidator

logger = get_logs(r"pages\store_page_denis\store_page_denis.py")


class StorePage:
    create_store_data = CreateStore()
    urls = Urls()
    request = MyRequests()

    @allure.step("Get all stores")
    def get_all_stores(self):
        store = next(generated_store())
        return store

    @allure.step("Create store with valid data")
    def create_store_with_valid_data(self):
        url = self.urls.STORES_URL
        store = self.get_all_stores()

        with allure.step("Get store data"):
            data = self.create_store_data.get_store_data(
                uid="store.uid",
                pet_id=store.pet_id,
                quantity=store.quantity,
                ship_date=store.ship_date,
                status=store.status,
                complete=store.complete)
            response = self.request.post(url=url, data=data)

        with allure.step("Validate response"):
            try:
                if StoreValidator.validate_store_response(response=response):
                    return response
            except ValidationError as e:
                logger.error(f"Invalid data format {e.json()}")
