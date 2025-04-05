from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.webdriver.common.action_chains import ActionChains




logger = logging.getLogger("AppiumTest")


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
        
    def click_password_image(self,img_num):
        time.sleep(8)

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
        
        print("img_num====> : %s", img_num)
        
        # img_num을 문자열로 변환 후 개별 숫자 리스트로 분리
        img_numbers = list(str(img_num))
        print("이미지 리스트====> :", img_numbers)

        # 각 숫자에 대해 click_password_image_module 실행
        for number in img_numbers:
            print(f"{number}.png 이미지를 찾고 클릭 시도 중...")
            success = self.click_password_image_module(number)  # 숫자를 개별적으로 전달
            
            if not success:
                print(f"이미지 {number}.png 화면에서 찾을 수 없었습니다. 최대 시도 횟수를 초과했습니다.")
                return False  # 이미지 찾기 실패 시 중단'
        # 모든 이미지를 클릭한 후 기본 창으로 복귀
        self.driver.switch_to.window(original_window)
        print("기본 창으로 성공적으로 복귀했습니다.")
        return True  # 모든 이미지 찾기 성공 
        
        # self.click_password_image_module(img_num)
        
        # print(f"이미지 {img_num}.png 화면에서 찾을 수 없었습니다. 최대 시도 횟수를 초과했습니다.")
        # return False  # 이미지 찾기 실패 
    
    def click_password_image_module(self,img_num ,max_attempts=5):
        attempts = 0
        
        project_root = os.path.abspath(os.path.join(__file__, "../../.."))
        img_path = os.path.join(project_root, 'features/img/')
        
        # 이미지 파일 확장자 추가
        # if isinstance(img_num, int):
        #     img_num = f"{img_num}.png"  # '3.png'로 변환
        
        # img_num에 확장자 추가
        if isinstance(img_num, int) or not img_num.endswith(".png"):
            img_num = f"{img_num}.png"
        
        # 이미지 절대 경로 생성
        image_path = os.path.join(img_path, img_num)
        
         # 디버깅 출력 추가
        print(f"최종 이미지 경로: {image_path}")
        print(f"파일 존재 여부: {os.path.exists(image_path)}")
        
        print(f"이미지 경로: {image_path}")
        print(f"파일 존재 여부: {os.path.exists(image_path)}")

        while attempts < max_attempts:
            print(f"이미지 {img_num}.png 검색 시도 {attempts + 1}/{max_attempts}...")
            location = pyautogui.locateOnScreen(image_path, confidence=0.9)
            
            if location:
                print(f"이미지 {img_num}.png 위치 발견: {location}")

                # 중앙 좌표 계산 및 배율 보정
                center_x, center_y = pyautogui.center(location)
                center_x = center_x // 2  # X좌표 보정
                center_y = center_y // 2  # Y좌표 보정
                print(f"보정된 좌표: ({center_x}, {center_y})")

                # 이동 및 클릭
                pyautogui.moveTo(center_x, center_y, duration=0.9)
                pyautogui.click(center_x, center_y)
                time.sleep(2)
                print(f"이미지 {img_num}.png 클릭 완료! ({center_x}, {center_y})")
                return True  # 이미지 찾기 성공
            else:
                print(f"이미지 {img_num}.png 화면에서 찾을 수 없음. 다음 시도...")
                time.sleep(1)  # 잠깐 대기 후 재시도
                attempts += 1
                
    
    def check_success_message(self):
        time.sleep(20)
        check_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='header']/div/h1")))
        print("check_message: %s",check_message)
        return check_message.strip() == "주문완료"
        
        

    #    # locateOnScreen으로 화면에서 이미지 
    #     location = pyautogui.locateOnScreen(image_path, confidence=0.8) 
    #     print('location--->',location)
    #     # pyautogui.center(location)
    #     # pyautogui.moveTo(location, duration=0.6)
    #     # pyautogui.click(location)
    #     if location:
    #         print(f"이미지 {img_num}.png 위치 발견: {location}")

    #         # 중앙 좌표 계산 및 배율 보정
    #         center_x, center_y = pyautogui.center(location)
    #         center_x = center_x // 2  # X좌표 보정
    #         center_y = center_y // 2  # Y좌표 보정
    #         print(f"보정된 좌표: ({center_x}, {center_y})")

    #         # 이동 및 클릭
    #         pyautogui.moveTo(center_x, center_y, duration=0.6)
    #         pyautogui.click(center_x, center_y)
    #         time.sleep(2)
    #         print(f"이미지 {img_num}.png 클릭 완료! ({center_x}, {center_y})")
    #     else:
    #         print(f"이미지 {img_num}.png 화면에서 찾을 수 없음.")
        # location = pyautogui.locateCenterOnScreen(image_path, confidence=0.4)
        
        # if location is not None:
        #     pyautogui.click(location)
        #     time.sleep(0.3)  # 안정성 확보를 위한 딜레이
        #     print("이미지 클릭 성공!")
        # else:
        #     raise pyautogui.ImageNotFoundException(f"이미지 인식 실패: {image_path}")
        
        
        