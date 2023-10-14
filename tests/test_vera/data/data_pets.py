"""This module stores test data for testing pets."""
import random


get_pet_by_status = [{"status": "available"},
                     {"status": "pending"},
                     {"status": "sold"}
                     ]

random_status = random.choice(get_pet_by_status)["status"]

pet_names = ["Buddy", "Max", "Lucy", "Daisy", "Charlie", "Luna", "Milo", "Sadie", "Toby", "Bailey"]

expected_non_exist_pet_keys = [
    ("code", 1, "Response JSON doesn't have key 'code'"),
    ("type", "error", "Response JSON doesn't have key 'type'"),
    ("message", "Pet not found", "Response JSON doesn't have key 'message'")
]

dog_breeds = [
        "Labrador Retriever", "German Shepherd", "Golden Retriever", "Bulldog", "Poodle", "Beagle",
        "Rottweiler", "Yorkshire Terrier", "Boxer", "Siberian Husky", "Dalmatian", "Chihuahua",
        "Bulldog", "Pug", "Shih Tzu", "Great Dane", "Border Collie", "Australian Shepherd",
        "Doberman Pinscher", "Cocker Spaniel", "Bichon Frise", "Shiba Inu", "French Bulldog",
        "Boston Terrier", "Corgi", "Maltese", "Bernese Mountain Dog", "Saint Bernard",
        "Australian Cattle Dog", "Shetland Sheepdog"
    ]

cat_breeds = [
        "Siamese", "Persian", "Maine Coon", "Ragdoll", "Bengal", "Sphynx", "British Shorthair",
        "Scottish Fold", "Russian Blue", "Norwegian Forest", "Abyssinian", "Birman", "Egyptian Mau",
        "Devon Rex", "Himalayan", "Manx", "Savannah", "Siamese", "Balinese", "Burmese", "Tonkinese",
        "Oriental", "Exotic Shorthair", "Turkish Angora", "Cornish Rex", "American Shorthair",
        "Chartreux", "Snowshoe", "Toyger"
    ]


def get_breed():
    all_breed = dog_breeds + cat_breeds
    return random.choice(all_breed)
