Feature: User Role Navigation
    As a user of the XYZ bank
    I want to select my user role
    So that I can access the correct portal

    Background:
        Given the XYZ Login page is opened

    Scenario Outline: Navigate to the appropriate login portal
        When the user clicks on the <role_button> role
        Then the user is redirected to the <portal_path> portal

        Examples:
            |role_button|portal_path|
            |Customer Login|/customer|
            |Bank Manager Login|/manager|

    Scenario Outline: Return to the login page
        When the user clicks on the <role_button> role
        And the user clicks on the "Home" button
        Then the user returns to the XYZ Login page

        Examples:
            |role_button|portal_path|
            |Customer Login|/customer|
            |Bank Manager Login|/manager|

        