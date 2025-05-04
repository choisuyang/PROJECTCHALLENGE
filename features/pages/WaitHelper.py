# helpers/wait_helper.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class WaitHelper:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def wait_and_click(self, by, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((by, locator))
            )
            element.click()
        except TimeoutException:
            raise AssertionError(f"[Timeout] Click failed: ({by}, {locator})")


    def wait_and_send_keys(self, by, locator, text):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            element.send_keys(text)
        except TimeoutException:
            raise AssertionError(f"[Timeout] Click failed: ({by}, {locator})")

    def wait_and_get_text(self, by, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            return element.text
        except TimeoutException:
            raise AssertionError(f"[Timeout] Click failed: ({by}, {locator})")
        