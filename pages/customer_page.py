from pages import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class CustomerPage(BasePage):

    LOGIN_BUTTON = (By.CSS_SELECTOR, "[type=submit]")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".logout")
    USER_DROPDOWN = (By.CSS_SELECTOR, "#userSelect")
    USER_LIST = (By.CSS_SELECTOR, "#userSelect option")
    WELCOME_MESSAGE = (By.CSS_SELECTOR, ".fontBig")
    ACCOUNTS_LIST = (By.CSS_SELECTOR, "#accountSelect")

    def select_user(self, user_name):
        dropdown_element = self.find_element(self.USER_DROPDOWN)
        select = Select(dropdown_element)
        select.select_by_visible_text(user_name.strip())

    def get_welcome_message(self):
        return self.get_element_text(self.WELCOME_MESSAGE)

    def get_default_account_number(self):
        account_element = self.find_element(self.ACCOUNTS_LIST)
        select = Select(account_element)
        return select.first_selected_option.text.strip()