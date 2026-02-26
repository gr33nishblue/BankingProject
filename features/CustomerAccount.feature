Feature: Customer Account Access
    As a customer of the XYZ bank
    I want to select my name and log in
    So that I can view my account details and transactions

Background:
    Given the XYZ Login page is opened
    And the user clicks on the Customer Login role
    And the user is on the Customer Login page

Scenario Outline: Successfull login for various customers
    When the user selects the customer name "<customer_name>"
    And the user clicks the "Login" button
    Then the dashboard displays a welcome message for "<customer_name>"
    And the account details for "<account_number>" should be displayed

    Examples:
        |customer_name|account_number|
        |Harry Potter|1004|
        |Hermoine Granger|1001|

Scenario: Logout back to the login page
    When the user selects the customer name "Ron Weasly"
    And the user clicks the "Login" button
    And the dashboard displays a welcome message for "Ron Weasly"
    And the user clicks on the "Logout" button
    Then the user is on the Customer Login page