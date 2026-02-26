import logging
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

logger = logging.getLogger(__name__)

scenarios('../features/BankManagerOperations.feature')

@given('the manager is on the "Add Customer" tab')
def manager_on_add_customer_tab(manager_page):
    logger.info('Given the manager is on the "Add Customer" tab')
    manager_page.click_add_customer()

@when('the manager enters the following details:')
def manager_enters_customer_details(manager_page, datatable):
    logger.info("When the manager enters the following details:\n%s", datatable)
    for row in datatable[1:]:
        first_name = row[0].strip()
        last_name = row[1].strip()
        post_code = row[2].strip()
        logger.info("Entering customer details: first_name='%s', last_name='%s', post_code='%s'", first_name, last_name, post_code)
        manager_page.enter_customer_details(first_name, last_name, post_code)

@when('the manager submits the customer form')
def manager_submits_add_customer_form(manager_page):
    logger.info("When the manager submits the add customer form")
    manager_page.submit_add_customer()

@then('a confirmation is displayed with a new customer id')
def confirmation_displayed_with_customer_id(manager_page):
    logger.info("Then a confirmation is displayed with a new 'customer id'")
    alert_text = manager_page.get_alert_text()
    logger.info("Alert text received: '%s'", alert_text)
    assert "Customer added successfully" in alert_text, f"Expected confirmation message not found in alert: '{alert_text}'"

@then('the manager accepts the alert')
def manager_accepts_alert(manager_page):
    logger.info("Then the manager accepts the alert")
    manager_page.accept_alert()

@given('the manager is on the "Customers" tab')
def manager_on_customers_tab(manager_page):
    logger.info('Given the manager is on the "Customers" tab')
    manager_page.click_customers()

@when('the manager deletes the record for John Doe')
def manager_deletes_john_doe_record(manager_page):
    logger.info('When the manager deletes the record for John Doe')
    manager_page.delete_customer_record("John", "Doe")

@then('the record for John Doe should be removed from the customers list')
def record_for_john_doe_removed(manager_page):
    logger.info('Then the record for John Doe should be removed from the customers list')
    customers = manager_page.get_customers_list()
    logger.info("Current customers list: %s", customers)
    assert not any(customer['first_name'] == "John" and customer['last_name'] == "Doe" for customer in customers), "Record for John Doe was not removed from the customers list"




