from appium import webdriver
from appium.options.android import UiAutomator2Options
import config
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

from selenium.webdriver.common.by import By
from features.pages.LoginPage import LoginPage
from features.pages.MyZonePage import MyZonePage
from features.pages.HomePage import HomePage
from features.pages.RankingPage import RankingPage
from features.pages.ProductPage import ProductPage
from features.pages.OrderPage import OrderPage


def before_all(context):
    # 로그 설정
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()  # 콘솔에 로그 출력
        ],
    )
    context.logger = logging.getLogger("AppiumTest")
    
    # Appium 서버 및 Desired Capabilities 설정
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.browser_name = "Chrome"
    options.automation_name = "UiAutomator2"
    options.no_reset = True
    options.full_reset = False
    options.chromedriver_executable = config.CHROMEDRIVER_PATH
    
    appium_server_url = "http://127.0.0.1:4723/wd/hub"
    context.driver = webdriver.Remote(appium_server_url, options=options)
    context.wait = WebDriverWait(context.driver, 10)
    
    # 이전에 저장된 쿠키 불러오기 (로그인 세션 유지)
    try:
        # 쿠키 저장
        cookies = context.driver.get_cookies()

        # 쿠키 재사용
        context.driver.delete_all_cookies()
        for cookie in cookies:
            context.driver.add_cookie(cookie)
    except FileNotFoundError:
        print("쿠키 파일 없음, 새 로그인 시작.")
   
    
    # Appium 설정 초기화
    # context.driver = context.create_driver()  # Custom driver factory 활용
    context.login_page = LoginPage(context.driver)
    context.my_zone_page = MyZonePage(context.driver)
    context.home_page = HomePage(context.driver)
    context.ranking_page = RankingPage(context.driver)
    context.product_page = ProductPage(context.driver)
    context.order_page = OrderPage(context.driver)
    context.driver.get(config.LIVE_URL)

def after_all(context):
    if context.driver:
        context.driver.quit()
