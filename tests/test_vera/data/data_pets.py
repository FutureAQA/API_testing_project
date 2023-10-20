"""This module stores test data for testing pets."""
import random
# from tests.test_vera.generator.generator import generated_pet


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

expected_pet_error_msg = {
     "not found": "Pet not found",
     "deleted": "Pet deleted",
     "404 message": "HTTP 404 Not Found",
     "400 message": 'Input error: query parameter `status value `invalid_status` is '
               'not in the allowable values `[available, pending, sold]`'
}


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


