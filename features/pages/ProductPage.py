from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProductPage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        
    def check_alert(self):
        self.driver.find_element(By.XPATH, "//*[@id='wrap']/div[1]/div/div/div/button").click()
        time.sleep(5)
        
    def click_the_option_button(self):
        self.driver.find_element(By.XPATH, "//*[@id='orderArea']/div[2]/button[2]").click()
        time.sleep(5)
    
    def click_option_area(self):
        option_area = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='option0_0']")))
        option_area.click()
        time.sleep(5)
        
    def click_the_purchase_button(self):
        self.driver.find_element(By.XPATH, "//*[@id='orderArea']/div[3]/div/div[5]/div[2]/button[3]").click()
        time.sleep(10)
        