# features/login.feature

Feature: Login and navigate through the application

  Scenario: Login to the app and navigate to ranking
    Given the user is on the login page
    When the user enters valid credentials
    And the user logs in
    Then the user should be on the MyZone page
    And the user navigates to the ranking tab
    And the user swipes right to view rankings
    And the user selects the first ranking item
