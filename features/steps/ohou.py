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
@given('enter the ohou mweb url and close popup')
def step_impl(context):
    context.ohou.close_popup()
    
 
# ///////////////////////////////
# //////////// WHEN /////////////
# ///////////////////////////////
@when('scroll to find the best title text')
def step_impl(context):
    context.ohou.scroll_to_find_best_title_text("//*[@class='css-1d0kvw3' and contains(text(), '베스트')]")

@when('select the food area by swipe')
def step_impl(context):
    element = context.driver.find_element(By.XPATH, "//*[contains(@class, 'css-1qm1lh') and contains(@class, 'enbz7te0')]/div/div/ul[@class='css-j1j67n']")
    context.ohou.swipe_right_with_js(element)


# ///////////////////////////////
# //////////// THEN /////////////
# ///////////////////////////////
