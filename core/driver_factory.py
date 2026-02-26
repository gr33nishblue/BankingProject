from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

class DriverFactory:
    @staticmethod
    def get_driver(browser_name, headless=False):
        browser_name = browser_name.lower()
        driver = None

        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            if headless: options.add_argument("--headless")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            if headless: options.add_argument("--headless")
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        elif browser_name.lower() == "edge":
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            raise Exception(f"Unsupported browser: {browser_name}")
        
        if driver:
            if not headless:
                driver.maximize_window()
            else:driver.set_window_size(1920, 1080)
        return driver