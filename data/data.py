from dataclasses import dataclass


@dataclass
class Store:
    uid: int = None,
    pet_id: int = None,
    quantity: int = None,
    ship_date: str = None,
    status: str = None,
    complete: bool = None
