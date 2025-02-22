from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():
    # URL = "https://display.cjonstyle.com/p/homeTab/main?hmtabMenuId=H00005"

    def __init__(self, driver):
        self.driver = driver

    # def open(self):
    #     self.driver.get(self.URL)

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, "//*[@id='id_input']").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, "//*[@id='password_input']").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, "//*[@id='loginSubmit']").click()
        time.sleep(5)
    
        if EC.alert_is_present():
            alert = self.driver.switch_to.alert
            alert.dismiss()
        