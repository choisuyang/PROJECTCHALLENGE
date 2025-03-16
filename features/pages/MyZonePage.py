from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

class MyZonePage():

    def __init__(self, driver):
        self.driver = driver

    def check_login_success(self):
        try:
            myZoneTitle = self.driver.find_element(By.XPATH, "//*[@id='header']/div/h1").text
            time.sleep(5)
            print("mz: %s,",myZoneTitle)
            return myZoneTitle.strip() == "마이존"  # 문자열 양쪽 공백 제거 후 비교
        except Exception as e:
            print("❌ 로그인 성공 여부 확인 실패: 요소를 찾을 수 없음", e)
            return False  # 요소가 없으면 False 반환
    
