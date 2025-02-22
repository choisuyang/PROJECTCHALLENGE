# # Behave의 환경설정 파일

# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import sys
# import os
# import time

# import config

    
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


# from features.pages.HomePage import HomePage
# from features.pages.MyZonePage import MyZonePage
# from features.pages.LoginPage import LoginPage
# from features.pages.RankingPage import RankingPage

# def before_all(context):
#     appium_server_url = "http://127.0.0.1:4723/wd/hub"
#     options = UiAutomator2Options()
#     options.platform_name = "Android"
#     options.platform_version = "15.0"
#     options.device_name = "emulator-5554"
#     options.browser_name = "Chrome"
#     options.automation_name = "UiAutomator2"
#     options.no_reset = True
#     options.chromedriver_executable = config.CHROMEDRIVER_PATH
    
#     context.driver = webdriver.Remote(appium_server_url, options=options)
#     context.driver.implicitly_wait(10)
#     print("\n[Setup] Appium WebDriver initialized.")

# def after_all(context):
#     """전체 테스트 실행 후 한 번 실행"""
#     if hasattr(context, "driver"):
#         context.driver.quit()
#         print("\n[Teardown] Appium WebDriver closed.")

# features/environment.py
from appium import webdriver
from appium.options.android import UiAutomator2Options
import config
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    options.chromedriver_executable = config.CHROMEDRIVER_PATH
    
    appium_server_url = "http://127.0.0.1:4723/wd/hub"
    context.driver = webdriver.Remote(appium_server_url, options=options)
    context.wait = WebDriverWait(context.driver, 10)

def after_all(context):
    if context.driver:
        context.driver.quit()
