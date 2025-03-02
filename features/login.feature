# features/login.feature

Feature: Login and navigate through the application

  Scenario: Login to the app and navigate to ranking
    Given the user is on the login page
    When input login id and password
    And click login button
    Then the user should be on the MyZone page
    And move to the home page
    And the user swipes right to view rankings
    And the user navigates to the ranking tab
    Then the user selects the first ranking item
    Given click the option button
    When click option area
    Then click the purchase button
    Given check the order page
    When scroll and find payment text
    When change payment method to one click payment
    
