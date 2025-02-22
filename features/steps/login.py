# from behave import *

# given("entering the login page")
# def step_open_login_page(context):
#     context.driver.get("https://example.com/login")

# @when("click bottom sheet myzone button")
# def step_enter_credentials(context):
#     context.driver.find_element(By.ID, "username").send_keys("testuser")
#     context.driver.find_element(By.ID, "password").send_keys("password123")
#     context.driver.find_element(By.ID, "login-button").click()

# @then("enter the login")
# def step_verify_homepage(context):
#     assert "dashboard" in context.driver.current_url, "User was not redirected to dashboard"


# features/steps/login_steps.py
from behave import given, when, then
from selenium.webdriver.common.by import By
from features.pages.LoginPage import LoginPage
from features.pages.MyZonePage import MyZonePage
from features.pages.HomePage import HomePage
import config
from features.pages.RankingPage import RankingPage

@given('the user is on the login page')
def step_impl(context):
    # Appium 설정 초기화
    context.driver = context.driver_factory.create_driver()  # Custom driver factory 활용
    context.login_page = LoginPage(context.driver)
    context.my_zone_page = MyZonePage(context.driver)
    context.home_page = HomePage(context.driver)
    context.ranking_page = RankingPage(context.driver)
    context.driver.get(config.LIVE_URL)

@when('the user enters valid credentials')
def step_impl(context):
    context.login_page.enter_username(config.TEST_ID)
    context.login_page.enter_password(config.TEST_PW)

@when('the user logs in')
def step_impl(context):
    context.login_page.click_login()

@then('the user should be on the MyZone page')
def step_impl(context):
    context.my_zone_page.check_login_success()

@then('the user navigates to the ranking tab')
def step_impl(context):
    context.home_page.go_to_ranking_tab()

@then('the user swipes right to view rankings')
def step_impl(context):
    element = context.driver.find_element(By.XPATH, "//*[@id='header_cnt']/div[2]/div/nav")
    context.home_page.swipe_right_with_js(element)

@then('the user selects the first ranking item')
def step_impl(context):
    context.ranking_page = context.ranking_page or RankingPage(context.driver)
    context.ranking_page.first_item_click()
