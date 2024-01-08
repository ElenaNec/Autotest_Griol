import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


with open(r"C:\Users\user\Desktop\pythonProject1\MY_DIP_GRIOL\config.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


# Инициализация сайта
@pytest.fixture(scope='session')
def browser():
    # инициализация драйвера
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

