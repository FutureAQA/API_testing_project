import os
import json
import random

current_file_path = os.path.abspath(__file__)
files_folder_path = os.path.join(os.path.dirname(current_file_path), 'files')


class PetName:
    pet_names_path = os.path.join(files_folder_path, 'pet_names.txt')

    def get_pet_name(self):
        with open(self.pet_names_path) as file:
            pet_name = json.load(file)
            return random.choice(pet_name)


class PetBread:
    bread_path = os.path.join(files_folder_path, 'bread.txt')

    def get_bread(self):
        with open(self.bread_path) as file:
            pet_bread = json.load(file)
            return random.choice(pet_bread)
