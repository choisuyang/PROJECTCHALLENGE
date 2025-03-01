from appium import webdriver
from appium.options.android import UiAutomator2Options
import config
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from features.pages.LoginPage import LoginPage
from features.pages.MyZonePage import MyZonePage
from features.pages.HomePage import HomePage
from features.pages.RankingPage import RankingPage

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
    
    # Appium 설정 초기화
    # context.driver = context.create_driver()  # Custom driver factory 활용
    context.login_page = LoginPage(context.driver)
    context.my_zone_page = MyZonePage(context.driver)
    context.home_page = HomePage(context.driver)
    context.ranking_page = RankingPage(context.driver)
    context.driver.get(config.LIVE_URL)

def after_all(context):
    if context.driver:
        context.driver.quit()
