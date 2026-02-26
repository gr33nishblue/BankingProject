from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def load(self, url):
        self.driver.get(url)
        
    def wait_for_element_present(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Element not found within {self.timeout} seconds")
    
    def is_element_present(self, locator):
        try:
            self.wait_for_element_present(locator)
            return True
        except TimeoutException:
            return False
            
    def find_element(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Element not visible within {self.timeout} seconds")
        
    def wait_for_element_clickable(self, locator):
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise TimeoutException(f"Element not clickable within {self.timeout} seconds")
        
    def click_element(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    def get_title(self):
        return self.driver.title
    
    def get_element_from_list_by_text(self, locator, text):
        elements = self.driver.find_elements(*locator)
        for element in elements:
            if element.text.strip() == text:
                return element
            
        raise Exception(f"Element with text '{text}' not found within {self.timeout} seconds in locator {locator}")
    
    def click_element_from_list_by_text(self, locator, text):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        element = self.get_element_from_list_by_text(locator, text)
        element.click()

    def verify_url_contains(self, partial_url):
        try:
            self.wait.until(EC.url_contains(partial_url))
            return True
        except TimeoutException:
            raise TimeoutException(f"URL did not contain '{partial_url}' within {self.timeout} seconds")