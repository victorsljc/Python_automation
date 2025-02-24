# common.py
from base_methods import Base  # Importing the Base class

class Common:
    def __init__(self, driver):
        """
        Initialize the Common class with the WebDriver.

        :param driver: WebDriver instance
        """
        self.driver = driver
        self.base = Base(driver)  # Initialize the Base class

    def user_login(self, username):
        """
        Perform user login by entering the username.

        :param username: Username to be entered
        """
        self.base.enter_username(username)  # Reusing the method from the Base class