import sys
import os
from features import config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



from behave import given, when, then

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))



@given('the user is on the login page')
def step_impl(context):
    context.home_page.close_popup()
    context.home_page.move_login_page()
    
@when('input login id and password')
def step_impl(context):
    context.login_page.enter_username(config.TEST_ID)
    context.login_page.enter_password(config.TEST_PW)

@when('click login button')
def step_impl(context):
    context.login_page.click_login()

@then('the user should be on the MyZone page')
def step_impl(context):
    context.my_zone_page.check_login_success()
    
@then('move to the home page')
def stp_impl(context):
    context.home_page.move_home()
    context.home_page.close_popup()

@then('the user swipes right to view rankings')
def step_impl(context):
    element = context.driver.find_element(By.XPATH, "//*[@id='header_cnt']/div[2]/div/nav")
    context.home_page.swipe_right_with_js(element)

@then('the user navigates to the ranking tab')
def step_impl(context):
    context.home_page.go_to_ranking_tab()

@then('the user selects the first ranking item')
def step_impl(context):
    # context.ranking_page = context.ranking_page or RankingPage(context.driver)
    context.ranking_page.first_item_click()
