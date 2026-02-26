import logging
import configparser
from pathlib import Path

import pytest
from core import DriverFactory
from pytest_bdd import scenarios, given, when, then, parsers

logger = logging.getLogger(__name__)

_ROOT = Path(__file__).resolve().parent.parent
_INI = _ROOT / "pytest.ini"

def _get_ini(key, default):
    cp = configparser.ConfigParser()
    cp.read(_INI, encoding="utf-8")
    if not cp.has_section("pytest"):
        return default
    return cp.get("pytest", key, fallback=default).strip()

def pytest_addoption(parser):
    parser.addini("base_url", help="The project base URL")
    parser.addini("timeout", help="The default wait timeout")
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on: chrome, firefox, edge")
    
@pytest.fixture(scope="function")
def timeout():
    return int(_get_ini("timeout", "10"))

@pytest.fixture(scope="function")
def base_url():
    return _get_ini("base_url", "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    driver = DriverFactory.get_driver(browser)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login_page(driver, timeout):
    from pages import LoginPage
    return LoginPage(driver, timeout = timeout)

@pytest.fixture(scope="function")
def customer_page(driver, timeout):
    from pages import CustomerPage
    return CustomerPage(driver, timeout = timeout)

@pytest.fixture(scope="function")
def manager_page(driver, timeout):
    from pages import ManagerPage
    return ManagerPage(driver, timeout = timeout)

#Common step definitions

@given("the XYZ Login page is opened")
def xyz_login_page_opened(login_page, base_url):
    logger.info("Opening XYZ Login page (base_url=%s)", base_url)
    login_page.load(base_url)
    assert login_page.is_element_present(login_page.ROLE_BUTTONS), "Login page not loaded properly, role buttons not found"

@given(parsers.parse('the user clicks on the {role_button} role'))
@when(parsers.parse('the user clicks on the {role_button} role'))
def click_role_button(login_page, role_button):
    logger.info("When the user clicks on the '%s' role", role_button.strip())
    login_page.select_role(role_button.strip())

@given('the user is on the Customer Login page')
@then('the user is on the Customer Login page')
def user_on_customer_login_page(login_page, base_url):
    logger.info("User is on the Customer Login page")
    assert login_page.verify_url_contains("customer"), "Expected URL to contain 'customer'"
