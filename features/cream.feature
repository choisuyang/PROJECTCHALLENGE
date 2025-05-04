# features/login.feature

@allure.label.epic:WebInterface
Feature: Cream Mobile Web Automation Test
  @normal
  @allure.label.owner:SuyangChoi
  @allure.link:https://kream.co.kr/
  @allure.label.story:Labels



  Scenario: Purchase Scenario Test to Cream Mobile Web
  
    Given enter the cream mweb url and close popup
    When click myzone on fnb
    When input login id and password in myzone
    When click login button in myzone
    Then check the login success
    When click the home button on fnb
    When click the search button on gnb
    When input the search keyword on search page
    Then click search list results Product
    Given click button purchase button on product page
    When click button immediate purchase button
    Then check order page title text
    Given scroll to find the card-simple payment text
    When click the card-simple payment button
    Then click last purchase button
    
