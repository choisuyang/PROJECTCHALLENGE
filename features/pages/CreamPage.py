from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from pages.WaitHelper import WaitHelper


class CreamPage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)
    
    # 모바일웹 진입시에 팝업 (앱으로가기 / 웹으로 그대로)
    def close_popup(self):
        self.wait.wait_and_click(By.XPATH, "//*[@id='modal-layer']/div[1]/div[2]/div[2]/div/div[2]/button[2]")
    
    # FNB 영역에서 마이존 클릭
    def click_myzone(self):
        self.wait.wait_and_click(By.XPATH, "//*[@id='mobileGnbContainer']/ul/li[5]/a")
    
    # 로그인 페이지에서 ID 입력    
    def input_id(self, id):
        self.wait.wait_and_send_keys(By.XPATH, "//*[@id='wrap']/div[2]/div/form/div[1]/div/input", id)
     
    # 로그인 페이지에서 Password 입력   
    def input_pw(self, pw):
        self.wait.wait_and_send_keys(By.XPATH, "//*[@id='wrap']/div[2]/div/form/div[2]/div/input", pw)
        
    # 로그인 페이지에서 로그인 버튼 클릭    
    def click_login(self):
        self.wait.wait_and_click(By.XPATH, "//*[@id='wrap']/div[2]/div/form/div[3]/button")
        
    # 로그인 성공 확인
    def check_login_success(self):
        try:
            check_login_text = self.wait.wait_and_get_text(By.XPATH,"//*[@id='__nuxt']/main/div/div[5]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/a[1]")
            if check_login_text == "프로필 관리":
                print("로그인 성공")
            else:
                print("로그인 실패")
            
        except Exception as e:
            print(f"로그인 실패: {e}")
            
    # FNB 영역에서 홈 클릭
    def click_home(self):
        time.sleep(5)
        self.wait.wait_and_click(By.XPATH, "//*[@id='mobileGnbContainer']/ul/li[1]/a")
    
    # GNB 영역에서 검색 클릭
    def click_search(self):
        self.wait.wait_and_click(By.XPATH, "//*[@id='wrap']/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/input")
        
    # 검색 페이지에서 검색어 입력 후 언테키 입력
    def input_search_keyword(self):
        self.wait.wait_and_send_keys(By.XPATH, "//*[@id='modal-layer']/div[1]/div/div[2]/div[1]/div/div/div/input", "마루는강쥐 행운키링 칼퇴")
        
        # # 검색어 입력 후 엔터키 입력
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER).perform()
        time.sleep(5)
        
    # 검색 결과에서 상품 클릭     
    def click_search_list(self):    
        time.sleep(5)
        self.wait.wait_and_click(By.XPATH, "//*[@id='__layout']/div/div[3]/div[2]/div[6]/div/div[1]/div/div[1]/div[1]/div[1]/div/a")
        
    # 상품 페이지에서 구매하기 버튼 클릭
    def click_purchase_button(self):
        time.sleep(5)
        self.wait.wait_and_click(By.XPATH, "//*[@id='wrap']/div[3]/div[1]/div[1]/div[2]/div/div[6]/div/div/button")        
        
    # 즉시 구매하기 버튼 클릭
    def click_immediate_purchase_button(self):
        self.wait.wait_and_click(By.XPATH, "/html/body/div/div/div/div[7]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/button[2]")
        
    # 주문 페이지에서 제목 확인
    def check_order_page_title(self):
        try:
            order_page_title = self.wait.wait_and_get_text(By.XPATH, "//*[@id='__layout']/div/div[1]/div[2]/div[1]/h1/span")
            if order_page_title == "배송/결제":
                print("주문 페이지 진입 성공")
            else:
                print("주문 페이지 진입 실패")
                
        except Exception as e:
            print(f"주문 페이지 진입 실패: {e}")
    
    # 카드 간편결제 버튼 클릭
    def click_card_simple_payment_button(self): 
        self.wait.wait_and_click(By.XPATH, "//*[@id='__layout']/div/div[2]/div/div[1]/div[2]/div[11]/div/div/div[10]")
        time.sleep(5)
    
    # 마지막 구매내역 버튼 선택 > 동의 필수 선택 > 결제버튼 선택
    def click_last_purchase_button(self):
        self.wait.wait_and_click(By.XPATH, "//*[@id='__layout']/div/div[2]/div/div[1]/div[2]/div[15]/div[1]/button")
        self.wait.wait_and_click(By.XPATH, "/html/body/div/div/div/div[5]/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/label/span")
        self.wait.wait_and_click(By.XPATH, "/html/body/div/div/div/div[5]/div[3]/div/div[2]/div[3]/div/button")
        time.sleep(10)
    
    
    
        
        
