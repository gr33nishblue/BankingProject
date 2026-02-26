import logging
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

logger = logging.getLogger(__name__)

scenarios('../features/UserRoleNavigation.feature')

@when('the user clicks on the "Home" button')
def click_home_button(login_page):
    logger.info("When the user clicks on the 'Home' button")
    login_page.click_home_button()

@then(parsers.parse('the user is redirected to the {portal_path} portal'))
def verify_portal_path(login_page, portal_path):
    logger.info("Then the user is redirected to the '%s' portal", portal_path.strip())
    assert login_page.verify_url_contains(portal_path.strip()), f"Expected URL to contain '{portal_path}'"

@then('the user returns to the XYZ Login page')
def user_returns_to_login_page(login_page, base_url):
    logger.info("Then the user returns to the XYZ Login page")  
    assert login_page.verify_url_contains(base_url), f"Expected URL to contain '{base_url}'"