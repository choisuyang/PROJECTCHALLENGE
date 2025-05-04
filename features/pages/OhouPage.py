from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from pages.WaitHelper import WaitHelper
from pages.OrderPage import OrderPage


class OhouPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)
        
    
    # 모바일웹 진입시에 팝업 (앱으로가기 / 웹으로 그대로)
    def close_popup(self):
        self.wait.wait_and_click(By.XPATH, '/html/body/div[2]/div/div/div/div/button[2]')
        
        
    
    # 홈탭에서 베스트 영역 찾아서 스크롤
    def scroll_to_find_best_title_text(self,xpath):
        # self.order_page.scroll_to_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[9]/div[1]/div[1]/div/strong')
        # self.driver.execute_script("window.scrollBy(0, 1000);")

        try:
            element = WebDriverWait(self.driver, 10).until(  # ✅ self.driver 사용
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(4)
            return element  # ✅ 요소를 찾으면 반환
            
        except Exception as e:
            print(f"❌ 스크롤할 요소를 찾을 수 없습니다: {xpath}, 오류: {e}")
            return None  # 실패 시 None 반환
        
    def swipe_right_with_js(self, element):
        self.driver.execute_script("arguments[0].scrollLeft += 300;", element)
        time.sleep(5)
        
        
    
    
        
        
