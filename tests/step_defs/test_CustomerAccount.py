import logging
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

logger = logging.getLogger(__name__)

scenarios('../features/CustomerAccount.feature')

@when(parsers.parse('the user selects the customer name "{customer_name}"'))
def select_customer_name(customer_page, customer_name):
    logger.info("When the user selects the customer name '%s'", customer_name.strip())
    customer_page.select_user(customer_name.strip())

@when('the user clicks the "Login" button')
def click_login_button(customer_page):
    logger.info("When the user clicks the 'Login' button")
    customer_page.click_element(customer_page.LOGIN_BUTTON)

@then(parsers.parse('the dashboard displays a welcome message for "{customer_name}"'))
@when(parsers.parse('the dashboard displays a welcome message for "{customer_name}"'))
def customer_dashboard_welcome(customer_page, customer_name):
    logger.info("Then the dashboard displays a welcome messge for '%s'", customer_name.strip())
    assert customer_page.get_welcome_message() == f"{customer_name.strip()}", "Welcome message does not match the customer name"

@then(parsers.parse('the account details for "{account_number}" should be displayed'))
def verify_account_number(customer_page, account_number):
    logger.info("Then the account details for '%s' should be displayed", account_number.strip())
    assert customer_page.get_default_account_number() == account_number.strip(), f"Expected account number to be '{account_number}'"

@when('the user clicks on the "Logout" button')
def click_logout_button(customer_page):
    logger.info("When the user clicks on the 'Logout' button")
    customer_page.click_element(customer_page.LOGOUT_BUTTON)