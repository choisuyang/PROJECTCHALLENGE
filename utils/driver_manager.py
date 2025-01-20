# WebDriver/Appium Driver


from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from module.login_page import LoginPage



# Desired Capabilities 설정
desired_caps = {
    "platformName": "Android",
    "platformVersion": "15.0",
    "deviceName": "emulator-5554",
    "browserName": "Chrome",
    "automationName": "UiAutomator2",
    "noReset": True,
    'chromedriverExecutable': '/Users/choesuyang/Documents/chromedriver-mac-x64/chromedriver',
}


appium_server_url = "http://127.0.0.1:4723/wd/hub"

# WebDriver 초기화
driver = webdriver.Remote(
    appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps)
)

login_page = LoginPage(driver)


# Chrome 브라우저에서 원하는 URL로 이동
driver.get("https://display.cjonstyle.com/m/homeTab/main?hmtabMenuId=H00005")

driver.implicitly_wait(10)

driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/button[2]").click()

driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//ul[@class='bar_util']/li[4]/a").click()

driver.implicitly_wait(10)

login_page.enter_username("test_user")


# 테스트 완료 후 WebDriver 종료
driver.quit()