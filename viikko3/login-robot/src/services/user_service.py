from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        # korvaa tällä: self.validate(username, password)
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        username_pattern = '[a-z]{3,}'
        if not re.match(username_pattern, username):
            raise UserInputError("Username must be formed from letters a-z and be at least 3 characters long")

        if len(password) < 8:
            raise UserInputError("Password length must be at least 8")

        # Pattern asserts that there is >= 1 letters and numbers in the sentence. 
        # Length is checked above.
        password_pattern = '^(?=.+\w)(?=.+\d+).+$'
        if not re.match(password_pattern, password):
            raise UserInputError("Password must be contain characters and numbers")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
