import re


class BasicValidator:

    def is_valid_email(self, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email)

    def is_valid_status(self, status):
        valid_statuses = ["available", "pending", "sold"]
        return status in valid_statuses
