from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage():
    URL = "https://display.cjonstyle.com/p/homeTab/main?hmtabMenuId=H00005"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.driver.find_element(By.ID, "id_input").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, "loginButton").click()

    def is_dashboard_visible(self):
        return "Dashboard" in self.driver.title
