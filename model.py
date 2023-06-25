import pickle
import os


class PickleFileService:
    """Provides functionality for saving and reading data from a file in pickle format."""

    def __init__(self, filename):
        self.__filename = filename
        if not os.path.exists(filename):
            self.clear()

    def write(self, data):
        """Writes data to a file in pickle format."""
        with open(self.__filename, "wb") as file:
            file.write(pickle.dumps(data))

    def read(self):
        """Reads data from a file in pickle format."""
        with open(self.__filename, "rb") as file:
            return pickle.loads(file.read())

    def clear(self):
        """Clears the contents of a file."""
        with open(self.__filename, "wb") as file:
            file.write(pickle.dumps([]))


class User:
    """`User` base class represents a user with a login and password.

    Attributes:
        username (str): Username.
        password (str): User password."""

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Admin(User):
    """The `Admin` class represents an administrator object.

    Methods:
        __str__(): Returns the string representation of the administrator."""

    def __str__(self):
        return f"Администратор: {self.username}"


class Author(User):
    """The `Author` class represents the author object.

    Methods:
        __str__(): Returns a string representation of the author."""

    def __str__(self):
        return f"Автор: {self.username}"


class Subscriber(User):
    """The `Subscriber` class represents a subscriber object.

    Methods:
        __str__(): Returns a string representation of the subscriber."""

    def __str__(self):
        return f"Подписчик: {self.username}"


class UserDatabase:
    """The `UserDatabase` class represents the user database.

    Attributes:
        data (list): List of users.
        __fileservice (PickleFileService): An object for working with a file.

    Methods:
        register(user_type, username, password): Register a new user.
        login(username, password): User login.
        save(): Saving the database to a file.
        sync(): Synchronization of the database with the file.
        __str__(): Returns a string representation of the user database."""

    def __init__(self, filename):
        self.__fileservice = PickleFileService(filename)
        self.sync()

    def register(self, user_type, username, password):
        """New user registration."""
        user = user_types[user_type](username, password)
        self.data.append(user)
        self.save()

    def login(self, username, password):
        """User login."""
        for user in self.data:
            if user.username == username and user.password == password:
                return user
        return None

    def save(self):
        """Saving the database to a file."""
        self.__fileservice.write(self.data)

    def sync(self):
        """Synchronization of the database with the file."""
        self.data = self.__fileservice.read()

    def __str__(self):
        """Returns a string representation of the user database."""
        return "\n".join(str(user) for user in self.data)


user_types = {
    "author": Author,
    "subscriber": Subscriber,
    "admin": Admin
}

users = UserDatabase("users.txt")
