from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains




class OrderPage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

        
    def check_the_order_page(self):
        orderPageTitle = self.driver.find_element(By.XPATH,"//*[@id='header']/div/h1").text
        return orderPageTitle.strip() == "주문서"
    
    def change_payment_method(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='_btn_change_payment']").click()
        time.sleep(10)
        
        # blind = self.driver.find_element(By.XPATH, "//*[@id='radiooneclick']")

        # JavaScript를 사용하여 display 속성을 변경
        # self.driver.execute_script("arguments[0].style.display = 'inline-block';", blind)
        
        # time.sleep(5)
        # self.driver.execute_script("arguments[0].click();", blind)
        # JavaScript로 <input> 요소 제거
        self.driver.execute_script("document.getElementById('radiooneclick').remove();")

        # 연결된 <label> 요소 클릭
        label_element = self.driver.find_element(By.XPATH, "//*[@id='oneclick-payment-control-view']/div[1]/div/div/ul/li[1]/label")
        label_element.click()
        time.sleep(5)
        
        # radio_button = self.driver.find_element(By.XPATH, '//*[@id="8E5AD34D4B5D5FBC6F807F8539F0742247C55D5797326E28B1A627643801468EXI1"]')
        
        # radio_button.click()
        
        # label_element = self.driver.find_element(By.XPATH, "//*[@id='oneclick-payment-control-view']/div[1]/div/div/ul/li[1]/label/span")
        # self.driver.execute_script("arguments[0].click();", label_element)
        # label_element.click()
        # time.sleep(5)
        
        # assert label_element.is_selected(), "❌ 현대카드가 선택되지 않았습니다!"

        time.sleep(10)


        # # 클릭 시도
        # try:
        #     label.click()  # 기본 클릭
        #     selected_input = self.driver.find_element(By.XPATH, "//*[@id='oneclick-payment-control-view']/div[1]/div/div/ul/li[1]/button")
        #     assert selected_input.is_selected(), "❌ 현대카드가 선택되지 않았습니다!"
        #     time.sleep(10)
            
        # except Exception as e:
        #    assert False, f"❌ 현대카드 선택 중 오류 발생: {str(e)}"

        
    
    # def click_last_purchase_button(self):
        
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
    
    def search_image(self,searchImage):
        img_path_keypad = os.path.join(os.path.dirname(__file__), 'img', searchImage)  # 이미지 경로 설정
        print(f"이미지 위치 찾는 중: {img_path_keypad}")
        
        attempt = 0
        max_attempts = 10  # 10번까지만 시도
        
        while attempt < max_attempts:
            img_capture = pyautogui.locateOnScreen(img_path_keypad, confidence=0.8)  # confidence 추가 (유사도 80%)
            if img_capture is None:
                print(f"[{attempt + 1}/{max_attempts}] 이미지 못 찾음, 다시 시도 중...")
                time.sleep(2)  # 2초 후 재시도
                attempt += 1
            else:
                center_x, center_y = pyautogui.center(img_capture)  # 중심 좌표 찾기
                pyautogui.click(center_x, center_y)  # 클릭
                print(f"이미지 클릭 완료: {center_x}, {center_y}")
                break
        else:
            print("이미지 찾기 실패. 프로그램 종료")
