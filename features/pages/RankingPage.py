from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class RankingPage():

    def __init__(self, driver):
        self.driver = driver

    def first_item_click(self):
        self.driver.find_element(By.XPATH,"//*[@id='tabpanel1']/ul/li[4]/div/a").click()
        time.sleep(10)
    
