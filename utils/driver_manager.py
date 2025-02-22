from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
import time

import config

import logging

# 로그 설정
#logging.basicConfig(
#    filename="app.log",  # 로그를 파일에 저장
#    level=logging.INFO,  # 로그 레벨 설정 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
#    format="%(asctime)s [%(levelname)s] %(message)s",  # 로그 출력 형식
#    datefmt="%Y-%m-%d %H:%M:%S",  # 날짜 형식
#)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # 파일 기록
        logging.StreamHandler()  # 콘솔 출력 (Appium 터미널에서도 보임)
    ],
)
logger = logging.getLogger("AppiumTest")


sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from features.pages.HomePage import HomePage
from features.pages.MyZonePage import MyZonePage
from features.pages.LoginPage import LoginPage
from features.pages.RankingPage import RankingPage



# Appium 서버 및 Desired Capabilities 설정
appium_server_url = "http://127.0.0.1:4723/wd/hub"

options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "15.0"
options.device_name = "emulator-5554"
options.browser_name = "Chrome"
options.automation_name = "UiAutomator2"
options.no_reset = True
options.chromedriver_executable = config.CHROMEDRIVER_PATH

# WebDriver 초기화
driver = webdriver.Remote(appium_server_url, options=options)
wait = WebDriverWait(driver, 10)

login_page = LoginPage(driver)
my_zone_page = MyZonePage(driver)
home_page = HomePage(driver)
ranking_page = RankingPage(driver)

try:
    # Chrome 브라우저에서 원하는 URL로 이동
    driver.get(config.LIVE_URL)

    # 팝업 닫기
    close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[3]/button[2]")))
    close_button.click()

    # 로그인 버튼 클릭
    # login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='bar_util']/li[4]/a")))
    # login_button.click()
    
    # time.sleep(5)
    
    # 아이디/비밀번호 입력 후 로그인
    # login_page.enter_username(config.TEST_ID)
    # login_page.enter_password(config.TEST_PW)
    # login_page.click_login()
    
    # 로그인 성공 여부 확인 (마이존 페이지로 이동되었는지 확인-타이틀 체크)
    # my_zone_page.check_login_success()
    
    # 홈으로 이동
    # home_page.move_home()
    # close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[3]/button[2]")))
    # close_button.click()
    
    # 홈에서 mbrd01 요소 찾기
    # home_page.scroll_to_element_by_xpath("//*[@id='modfd']/div")
    
    # time.sleep(5)
    
    # 랭킹탭 우측 스와이프
    element = driver.find_element(By.XPATH, "//*[@id='header_cnt']/div[2]/div/nav")  # 스크롤 가능한 영역 요소
    home_page.swipe_right_with_js(element)
    # 랭킹탭으로 이동
    home_page.go_to_ranking_tab()
    
    # 랭킹탭에서 첫 번째 아이템 클릭
    ranking_page.first_item_click()
    
    
    
    


    
    
    
finally:
    # 드라이버 종료
    driver.quit()
