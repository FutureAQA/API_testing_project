from src.utils.data_preparation.prepare_basic_test_data import BaseTestData


class PrepareUserData(BaseTestData):

    def create_user_id(self, user_id):
        if user_id is None:
            user = self.get_all_user_data()
            return user.user_id
        return user_id

    def create_username(self, user_name):
        if user_name is None:
            user = self.get_all_user_data()
            return user.user_name
        return user_name

    def create_first_name(self, first_name):
        if first_name is None:
            user = self.get_all_user_data()
            return user.first_name
        return first_name

    def create_last_name(self, last_name):
        if last_name is None:
            user = self.get_all_user_data()
            return user.last_name
        return last_name

    def create_password(self, password):
        if password is None:
            user = self.get_all_user_data()
            return user.password
        return password

    def create_email(self, email):
        if email is None:
            user = self.get_all_user_data()
            return user.email
        return email

    def create_phone(self, phone):
        if phone is None:
            user = self.get_all_user_data()
            return user.phone
        return phone

    def create_user_status(self, user_status):
        if user_status is None:
            user = self.get_all_user_data()
            return user.user_status
        return user_status
