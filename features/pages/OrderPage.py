from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import logging

logger = logging.getLogger("AppiumTest")

# 보안 키패드 숫자 이미지 경로 (각 숫자별로 PNG로 저장해둬야 함)
number_images = {
    # '1': 'img/1.png',
    # '2': 'img/2.png',
    '3': 'img/3.png',
    # '4': 'img/4.png',
    # '5': 'img/5.png',
    '6': 'img/6.png',
    '7': 'img/7.png',
    # '8': 'img/8.png',
    '9': 'img/9.png',
    # '0': 'img/0.png'
}

# 입력할 비밀번호 (예: 485172)
password = '369777'


class OrderPage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

        
    def check_the_order_page(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//*[@id='naver']").click()
        time.sleep(40)
        orderPageTitle = self.driver.find_element(By.XPATH,"//*[@id='header']/div/h1").text
        return orderPageTitle.strip() == "주문서"
    
    def change_payment_method(self):
        # time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='bottomOrderButtonSection']/button").click()
        time.sleep(5)
        
    def scroll_to_element_by_xpath(self, xpath):
        logger.info("start")
        try:
            element = WebDriverWait(self.driver, 10).until(  # ✅ self.driver 사용
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return element  # ✅ 요소를 찾으면 반환
            
        except Exception as e:
            print(f"❌ 스크롤할 요소를 찾을 수 없습니다: {xpath}, 오류: {e}")
            return None  # 실패 시 None 반환
        
    def click_password_image(self):
        # 현재 윈도우 핸들 저장
        original_window = self.driver.current_window_handle

        # 모든 윈도우 핸들 가져오기
        all_windows = self.driver.window_handles

        # 새로 열린 창으로 전환
        for window in all_windows:
            if window != original_window:
                self.driver.switch_to.window(window)
                break
        title = self.driver.find_element(By.XPATH, "//*[@id='txt1']").text
        print("titled: %s,",title)
        logger.info("title: %s", title)
        
        print(f"❌ 스크롤할 요소를 찾을 수 없습니다: {title}, 오류: {title}")
        # 이미지 검색 및 클릭 함수
        def click_number(num):
            img_path = number_images[num]
            location = pyautogui.locateCenterOnScreen(img_path, confidence=0.8)
            if location:
                pyautogui.click(location)
                time.sleep(0.3)  # 안정성을 위해 딜레이 추가
                
         # 비밀번호 입력
        for digit in password:
            click_number(digit)
        # self.search_image(3)
        
        
        # 새 창에서 작업 수행 후, 원래 창으로 돌아오기
        self.driver.close()  # 새 창 닫기
        self.driver.switch_to.window(original_window)
        
    
        
        
    
    def search_image(self,searchImage):
        # img_path_keypad = os.path.join(os.path.dirname(__file__), 'png', searchImage)  # 이미지 경로 설정
        # img_path_keypad = os.path.join(os.path.dirname(__file__), 'img', f"{searchImage}.png")
        # 프로젝트 루트 기준으로 경로 설정
        PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 현재 파일의 상위 폴더
        IMG_DIR = os.path.join(PROJECT_ROOT, "features", "img")  # 이미지 폴더 경로

        def get_image_path(searchImage):
            return os.path.join(IMG_DIR, f"{searchImage}.png")
        
        img_path_keypad = get_image_path(searchImage)

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
