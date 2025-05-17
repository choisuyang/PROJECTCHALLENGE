from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from pages.WaitHelper import WaitHelper
from pages.OrderPage import OrderPage
import logging
from selenium.webdriver.support.ui import Select




class OhouPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)
        logging.basicConfig(level=logging.INFO)
        
    
    # 모바일웹 진입시에 팝업 (앱으로가기 / 웹으로 그대로)
    def close_popup(self):
        self.wait.wait_and_click(By.XPATH, '/html/body/div[2]/div/div/div/span/div/button[2]')
    
    # 홈탭에서 베스트 영역 찾아서 스크롤
    def scroll_to_find_best_title_text(self,xpath):
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
        
    def swipe_right_with_js(self, element, clickElement):
        self.driver.execute_script("arguments[0].scrollLeft += 300;", element)
        time.sleep(5)
        self.driver.find_element(By.XPATH, clickElement).click()
        time.sleep(10)
        
    def click_first_on_best_area(self):    
        self.wait.wait_and_click(By.XPATH, "//article[contains(@class, 'e1fptbff1')][1]/a")
        time.sleep(10)
            
    def click_the_purchase_button_on_product_page(self):
        self.wait.wait_and_click(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[6]/div/div/button[2][contains(text(),'구매하기')]")
        time.sleep(5)
        
    def check_option_size_and_click_option(self):
        divs = self.driver.find_elements(By.XPATH, "//section[contains(@class,'production-selling-select-modal__form')]/div[contains(@class,'selling-option-form-content__form')]/div[contains(@class,'selling-option-select-input')]/div")
        size = len(divs)
        self.selectOptionModule(size)
        
        # logging.info("-------------> div 개수: %d", len(divs))
        # print("------------->", len(divs), flush=True)
        # time.sleep(5)

    def selectOptionModule(self, size):
        if (size == 1) :
            self.wait.wait_and_click(By.XPATH,"/html/body/div[5]/div/div/div/section/div/div/div/select")
            time.sleep(5)
            select_elem = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/section/div/div/div/select")
            # logging.info("-------------> select_elem: %s", select_elem)            
            select = Select(select_elem)
            # logging.info("-------------> element detail: %s", select.select_by_visible_text("대추 방울토마토 로얄과 2Kg(11,500원)"))
            # select.select_by_visible_text("대추 방울토마토 로얄과 2Kg(11,500원)")
            select.select_by_value("대추 방울토마토 로얄과 2Kg(11,500원)")
            logging.info("-------------> 옵션 선택 완료")
            time.sleep(10)
            
        else :
            assert False, "❌ 옵션 사이즈가 1이 아닙니다."
        
