from pages import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    HOME_BUTTON = (By.CSS_SELECTOR, ".home")
    ROLE_BUTTONS = (By.CSS_SELECTOR, ".btn-lg")
    

    def select_role(self, role_name):
        self.click_element_from_list_by_text(self.ROLE_BUTTONS, role_name)

    def click_home_button(self):
        self.click_element(self.HOME_BUTTON)