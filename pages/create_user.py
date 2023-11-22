"""
This module contains the CreateUser class
"""

from src.logger.logger import get_logs

logger = get_logs(r"pages\create_user.py")


class CreateUser:

    @staticmethod
    def get_id(uid):
        """
        This method returns id
        :param uid: passed as a parameter
        :return: id
        """
        if uid is not None:
            return {"id": uid}

    @staticmethod
    def get_user_name(user_name):
        """
        This method returns user_name
        :param user_name: passed as a parameter
        :return: user_name
        """
        if user_name is not None:
            return {"username": user_name}

    @staticmethod
    def get_first_name(first_name):
        """
        This method returns first_name
        :param first_name: passed as a parameter
        :return: first_name
        """
        if first_name is not None:
            return {"firstName": first_name}

    @staticmethod
    def get_last_name(last_name):
        """
        This method returns last_name
        :param last_name: passed as a parameter
        :return: last_name
        """
        if last_name is not None:
            return {"lastName": last_name}

    @staticmethod
    def get_email(email):
        """
        This method returns email
        :param email: passed as a parameter
        :return: email
        """
        if email is not None:
            return {"email": email}

    @staticmethod
    def get_password(password):
        """
        This method returns password
        :param password: passed as a parameter
        :return: password
        """
        if password is not None:
            return {"password": password}

    @staticmethod
    def get_phone(phone):
        """
        This method returns phone
        :param phone: passed as a parameter
        :return: phone
        """
        if phone is not None:
            return {"phone": phone}

    @staticmethod
    def get_user_status(user_status):
        """
        This method returns user_status
        :param user_status: passed as a parameter
        :return: user_status
        """
        if user_status is not None:
            return {"userStatus": user_status}

    def get_user_data(self, uid=None, user_name=None, first_name=None, last_name=None,
                      email=None, phone=None, user_status=None):
        """
        This method prepares user data using the provided data
        :param uid: passed as a parameter to the get_id method
        :param user_name: passed as a parameter to the get_user_name method
        :param first_name: passed as a parameter to the get_first_name method
        :param last_name: passed as a parameter to the get_last_name method
        :param email: passed as a parameter to the get_email method
        :param phone: passed as a parameter to the get_phone method
        :param user_status: passed as a parameter to the get_user_status method
        :return: prepared data
        """
        data = {}

        id_value = self.get_id(uid)
        if id_value:
            data["id"] = id_value["id"]

        user_name_value = self.get_user_name(user_name)
        if user_name_value:
            data["username"] = user_name_value["username"]

        first_name_value = self.get_first_name(first_name)
        if first_name_value:
            data["firstName"] = first_name_value["firstName"]

        last_name_value = self.get_last_name(last_name)
        if last_name_value:
            data["lastName"] = last_name_value["lastName"]

        email_value = self.get_email(email)
        if email_value:
            data["email"] = email_value["email"]

        phone_value = self.get_phone(phone)
        if phone_value:
            data["phone"] = phone_value["phone"]

        user_status_value = self.get_user_status(user_status)
        if user_status_value:
            data["userStatus"] = user_status_value["userStatus"]

        logger.info(f"Request data: {data}")
        return data
