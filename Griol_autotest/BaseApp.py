from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self,driver, url):
        self.driver = driver
        self.base_url = url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        self.driver.maximize_window()
        return self.driver.get(self.base_url)

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def switch_to_alert(self):
        alert = self.driver.switch_to.alert
        return alert

    # # создание объекта цепочки действий
    # def action(self):
    #     action = ActionChains(self.driver)
    #     return action