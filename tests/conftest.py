import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selene import browser, Browser, Config


@pytest.fixture(scope="function")
def setup_browser(request):

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVideo": True
        }
    }

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        desired_capabilities=capabilities)

    browser = Browser(Config(driver))
    yield browser

    browser.quit()