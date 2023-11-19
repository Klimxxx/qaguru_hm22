import os

import pytest
import allure
import allure_commons

from appium import webdriver
from selene import browser, support

from config import remote_url, driver_options, config
from android_wikipedia_tests.utils import attach


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    with allure.step('Init app session'):
        browser.config.driver = webdriver.Remote(
            remote_url,
            options=driver_options())

    browser.config.timeout = config.timeout

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield browser

    attach.add_screenshot(browser)
    attach.add_xml(browser)

    session_id = browser.driver.session_id

    with allure.step('Tear down app session'):
        browser.quit()

    if config.context == 'bstack':
        attach.attach_bstack_video(session_id, os.getenv('USER_NAME'), os.getenv('ACCESS_KEY'))