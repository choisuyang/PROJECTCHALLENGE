import sys
import os
from features import config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



from behave import given, when, then

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ///////////////////////////////
# //////////// GIVEN ////////////
# ///////////////////////////////
@given('enter the cream mweb url and close popup')
def step_impl(context):
    context.cream_page.close_popup()
    
@given('click button purchase button on product page')
def step_impl(context):
    context.cream_page.click_purchase_button()
    
@given('scroll to find the card-simple payment text')
def step_impl(context):
    context.order_page.scroll_to_element_by_xpath("//*[@id='__layout']/div/div[2]/div/div[1]/div[2]/div[11]/div/div/div[8]/div[1]/div[1]/p")
    
    
 
# ///////////////////////////////
# //////////// WHEN /////////////
# ///////////////////////////////


@when('click myzone on fnb')
def step_impl(context):
    context.cream_page.click_myzone()
    
@when('input login id and password in myzone')
def setp_impl(context):
    context.cream_page.input_id(config.CREAM_ID)
    context.cream_page.input_pw(config.CREAM_PW)
    
@when('click login button in myzone')
def step_impl(context):
    context.cream_page.click_login()
    
@when('click the home button on fnb')
def step_impl(context):
    context.cream_page.click_home()

@when('click the search button on gnb')
def step_impl(context):
    context.cream_page.click_search()

@when('input the search keyword on search page')
def step_impl(context):
    context.cream_page.input_search_keyword()
    
@when('click button immediate purchase button')
def step_impl(context):
    context.cream_page.click_immediate_purchase_button()

@when('click the card-simple payment button')
def step_impl(context):
    context.cream_page.click_card_simple_payment_button()
    
# ///////////////////////////////
# //////////// THEN /////////////
# ///////////////////////////////

@then('check the login success')
def step_impl(context):
    context.cream_page.check_login_success()
    
@then('click search list results Product')
def step_impl(context):
    context.cream_page.click_search_list()
    
@then('check order page title text')
def step_impl(context):
    context.cream_page.check_order_page_title()

@then('click last purchase button')
def step_impl(context):
    context.cream_page.click_last_purchase_button()