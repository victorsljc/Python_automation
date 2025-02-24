
from selenium.webdriver.common.by import By

locators ={
    'email': (By.NAME, 'email'),
    'menu_Help?':  "//a[text()='Help?']",
}

def test_print():
    print(locators['email'])

email = locators['email']
menu_help=locators['menu_Help?']
