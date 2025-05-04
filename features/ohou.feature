# features/login.feature

@allure.label.epic:WebInterface
Feature: Ohou Mobile Web Automation Test
  @normal
  @allure.label.owner:SuyangChoi
  @allure.link:https://ohou.se/
  @allure.label.story:Labels

  Scenario: Purchase Scenario Test to ohou Mobile Web
  
    Given enter the ohou mweb url and close popup
    When scroll to find the best title text
    When select the food area by swipe
    
