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
        
    def move_home(self):
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
        self.driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[2]/div/nav/ul/li[10]/a").click()
        time.sleep(5)