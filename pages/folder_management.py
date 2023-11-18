"""
This file provides a class for managing folders in the project.
"""

import os

import allure


class FolderManagement:
    @allure.description("Get the root path of the project")
    def get_root_path(self):
        """
        :return: The root path of the project
        """
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return project_root

    @allure.description("Cleans up the 'logs' folder, keeping only the latest 20 files")
    def cleanup_folder(self):
        current_dir = self.get_root_path()
        logs_dir = os.path.join(current_dir, 'logs')
        max_files = 20
        if not os.path.exists(logs_dir):
            # Create an empty logs folder
            os.makedirs(logs_dir)
        # Getting a list of files in a folder
        files = [f for f in os.listdir(logs_dir) if os.path.isfile(os.path.join(logs_dir, f))]

        # If the number of files exceeds the maximum, we delete old files
        if len(files) > max_files:
            # Sorting files by the time of the last modification (from old to new)
            files.sort(key=lambda x: os.path.getmtime(os.path.join(logs_dir, x)))

            # Determining the number of files to be deleted
            files_to_delete = len(files) - max_files

            # Deleting old files
            for i in range(files_to_delete):
                file_to_delete = os.path.join(logs_dir, files[i])
                os.remove(file_to_delete)
                print(f"File deleted: {file_to_delete}")
