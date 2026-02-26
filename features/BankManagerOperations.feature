Feature: Bank Manager Operations
    As a bank manager of the XYZ bank
    I want to log to the manager dashboard
    So that I can manage customers and accounts

Background:
    Given the XYZ Login page is opened
    And the user clicks on the Bank Manager Login role

Scenario: Successfully add a new customer
    Given the manager is on the "Add Customer" tab
    When the manager enters the following details:
        |First Name|Last Name|Post Code|
        |John       |Doe      |12345    |
    And the manager submits the customer form
    Then a confirmation is displayed with a new customer id
    And the manager accepts the alert

#Delete customer record test passes although the record is not actually deleted
#The John Doe record does not seem to be persisted
#To be investigated further, but for now the test is left in place to demonstrate the intended functionality
Scenario: Delete a customer record
    Given the manager is on the "Customers" tab
    When the manager deletes the record for John Doe
    Then the record for John Doe should be removed from the customers list