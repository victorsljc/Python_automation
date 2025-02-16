"""
    1.NoSuchElementException:
        Raised when the locator used to find an element does not match any element on the page.
        Example: driver.find_element(By.ID, "nonexistent-id").

    2.ElementNotInteractableException:
        Raised when an element is present in the DOM but is not interactable
        (e.g., hidden, disabled, or overlapped by another element).

    3.TimeoutException:
        Raised when a command does not complete in the expected time (e.g., waiting for an element to appear).

    4.StaleElementReferenceException:
        Raised when the element reference is no longer valid
        (e.g., the element was removed from the DOM or the page was refreshed).

    5.NoSuchWindowException:
        Raised when the target window or tab does not exist.

    6.NoSuchFrameException:
        Raised when the target frame does not exist.

    7.ElementClickInterceptedException:
        Raised when an element cannot be clicked because it is obscured by another element.

    8.WebDriverException:
        A generic exception for WebDriver-related errors (e.g., browser crashes or connectivity issues)

    9.InvalidSelectorException:
        Raised when an invalid selector is used (e.g., an invalid XPath or CSS selector).

    10.UnexpectedAlertPresentException:
        Raised when an unexpected alert is present on the page.

Common Scenarios and Solutions
    Element Not Found:
        Use explicit waits or verify the locator.
    Element Not Interactable:
        Scroll the element into view or wait for it to become interactable.
        element = driver.find_element(By.ID, "element-id")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    Stale Element:
        Re-locate the element before interacting with it.
    Timeout:
        Increase the wait time or investigate why the element is not appearing.
    Unexpected Alert:
        Handle the alert using driver.switch_to.alert

"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    ElementNotInteractableException,
    StaleElementReferenceException,
    WebDriverException, UnexpectedAlertPresentException,
)

driver = webdriver.Chrome()
def test_selenium_exception():
# Initialize the WebDriver


    try:
        # Open a webpage
        driver.get("https://example.com")

        # Attempt to find an element
        try:
            element = driver.find_element(By.ID, "nonexistent-id")
            element.click()
        except NoSuchElementException:
            print("Element not found on the page.")
        except ElementNotInteractableException:
            print("Element is present but not interactable.")
        except StaleElementReferenceException:
            print("Element reference is stale. Retrying...")
        except TimeoutException:
            print("Timed out waiting for the element to appear.")

        # Handle unexpected alerts
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except UnexpectedAlertPresentException:
            print("An unexpected alert was present.")

    except WebDriverException as e:
        print(f"A WebDriver error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()
'''
Use Explicit Waits:
    Use WebDriverWait to wait for elements to appear or become interactable. 
    This reduces the likelihood of NoSuchElementException and TimeoutException.
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_usage_of_explicit_waits():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "element-id"))
        )
    except TimeoutException:
        print("Element did not appear within the timeout.")

def test_custom_exceptions():
    class ElementNotFoundError(Exception):
        """Raised when an element is not found on the page."""
        pass

    # Usage
    try:
        raise ElementNotFoundError("The element was not found on the page.")
    except ElementNotFoundError as e:
        print(e)

