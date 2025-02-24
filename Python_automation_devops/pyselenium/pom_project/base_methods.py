# base_method.py
from selenium.webdriver.common.by import By

class Base:
    def __init__(self, driver, page_definition):
        """
        Initialize the Base class with the WebDriver and page definitions.

        :param driver: WebDriver instance
        :param page_definition: Dictionary containing locators for the page
        """
        self.driver = driver
        self.username_input = page_definition.get('username_input')

    def enter_username(self, username):
        """
        Enter the username into the username input field.

        :param username: Username to be entered
        """
        self.driver.find_element(By.NAME, self.username_input).send_keys(username)