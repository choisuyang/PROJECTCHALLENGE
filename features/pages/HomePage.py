from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput


import pytest

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        
    def close_popup(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/button[2]").click()
        time.sleep(5)
        
    def move_login_page(self):
        self.driver.find_element(By.XPATH,"//ul[@class='bar_util']/li[4]/a").click()
        # self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='bar_util']/li[4]/a"))).click()
        
    def move_home(self):
        time.sleep(5)
        # self.driver.find_element(By.XPATH, "//*[@id='popup_spot']/div/div/div/div[2]/button").click()
        self.driver.find_element(By.XPATH, "//*[@id='footer']/div[2]/ul/li[1]/a").click()
        time.sleep(5)
        
    def scroll_to_element_by_xpath(self, xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(  # ✅ self.driver 사용
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return element  # ✅ 요소를 찾으면 반환
        except Exception as e:
            print(f"❌ 스크롤할 요소를 찾을 수 없습니다: {xpath}, 오류: {e}")
            return None  # 실패 시 None 반환
    

    def swipe_right_with_js(self, element):
        self.driver.execute_script("arguments[0].scrollLeft += 400;", element)
        time.sleep(5)
        
    def go_to_ranking_tab(self):
        ranking_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/header/div/div[2]/div/nav/ul/li[11]/a")))
        ranking_tab.click()
        time.sleep(5)