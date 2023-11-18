"""
This file includes two classes: PetName and PetBread.
The PetName class provides a method to get random pet names from a file,
and the PetBread class provides a method to get random breeds from another file.
File paths are constructed based on the current location of the file.
Internal files contain lists of strings used for randomly choosing a name or breed
"""

import os
import json
import random

current_file_path = os.path.abspath(__file__)
files_folder_path = os.path.join(os.path.dirname(current_file_path), 'files')


class PetName:
    pet_names_path = os.path.join(files_folder_path, 'pet_names.txt')

    def get_pet_name(self):
        """
        This method returns pet names from a file
        :return: random pet name
        """
        with open(self.pet_names_path) as file:
            pet_name = json.load(file)
            return random.choice(pet_name)


class PetBread:
    bread_path = os.path.join(files_folder_path, 'bread.txt')

    def get_bread(self):
        """
        This method returns breads from a file
        :return: random bread
        """
        with open(self.bread_path) as file:
            pet_bread = json.load(file)
            return random.choice(pet_bread)
