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
    # context.login_page.enter_naver_login()
    context.login_page.enter_username(config.TEST_ID)
    context.login_page.enter_password(config.TEST_PW)

@when('click login button')
def step_impl(context):
    context.login_page.click_login()

@then('the user should be on the MyZone page')
def step_impl(context):
    context.my_zone_page.check_login_success()
    
@given('move to the home page')
def stp_impl(context):
    context.home_page.close_popup() # 임시로 추가 추후 로그인 고쳐지면 삭제
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
    
@given('click the option button')
def step_impl(context):
    context.product_page.check_alert()
    context.product_page.click_the_option_button()
    
    
@when('click option area')
def step_impl(context):
    context.product_page.click_option_area()
    
@then('click the purchase button')
def step_impl(context):
    context.product_page.click_the_purchase_button()
    
@given('check the order page')
def step_impl(context):
    context.order_page.check_the_order_page()

@when('scroll and find payment text')
def step_impl(context):
    context.order_page.scroll_to_element_by_xpath("//*[@id='order_cash_receipt']/div[1]/h3")
    
@when('change payment method to one click payment')
def step_impl(context):
    context.order_page.change_payment_method()
    
@then('click password image button')
def step_impl(context):
    context.order_page.click_password_image(369777)
     
# @then('click the last purchase button')
# def step_impl(context):
#     context.order_page.click_the_last_purchase_button()
    
@then('check success message')
def step_impl(context):
    context.order_page.check_success_message()
