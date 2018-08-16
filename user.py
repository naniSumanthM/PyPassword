"""
User class defines all properties of a user object
"""


class user:

    def __init__(self, user_name, user_email, user_password):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password

    def get_user_name(self):
        return self.user_name

    def get_user_email(self):
        return self.user_email

    def get_user_password(self):
        return self.user_password

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_user_email(self, user_email):
        self.user_email = user_email

    def set_user_password(self, user_password):
        self.user_password = user_password
