from pages import BasePage
from selenium.webdriver.common.by import By

class ManagerPage(BasePage):

    ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "[ng-class='btnClass1']")
    OPEN_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[ng-class='btnClass2']")
    CUSTOMERS_BUTTON = (By.CSS_SELECTOR, "[ng-class='btnClass3']")
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "[ng-model='fName']")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "[ng-model='lName']")
    POST_CODE_FIELD = (By.CSS_SELECTOR, "[ng-model='postCd']")
    SUBMIT_ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "[type=submit]")

    def click_add_customer(self):
        self.click_element(self.ADD_CUSTOMER_BUTTON)

    def click_open_account(self):
        self.click_element(self.OPEN_ACCOUNT_BUTTON)

    def click_customers(self):
        self.click_element(self.CUSTOMERS_BUTTON)

    def enter_customer_details(self, first_name, last_name, post_code):
        self.enter_text(self.FIRST_NAME_FIELD, first_name)
        self.enter_text(self.LAST_NAME_FIELD, last_name)
        self.enter_text(self.POST_CODE_FIELD, post_code)
    
    def submit_add_customer(self):
        self.click_element(self.SUBMIT_ADD_CUSTOMER_BUTTON)

    def get_alert_text(self):
        return self.driver.switch_to.alert.text
    
    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def delete_customer_record(self, first_name, last_name):
        customers = self.get_customers_list()
        for customer in customers:
            if customer['first_name'] == first_name and customer['last_name'] == last_name:
                delete_button = (By.XPATH, f"//tr[td[text()='{first_name}'] and td[text()='{last_name}']]//button")
                self.click_element(delete_button)
                break

    def get_customers_list(self):
        customers = []
        rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        for row in rows:
            first_name = row.find_element(By.XPATH, "./td[1]").text
            last_name = row.find_element(By.XPATH, "./td[2]").text
            post_code = row.find_element(By.XPATH, "./td[3]").text
            customers.append({
                'first_name': first_name,
                'last_name': last_name,
                'post_code': post_code
            })
        return customers

    