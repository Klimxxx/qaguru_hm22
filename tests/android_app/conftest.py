import allure
import os

import allure_commons
import pytest
from appium import webdriver
from dotenv import load_dotenv
from selene import browser, support
from appium.options.android import UiAutomator2Options

from android_wikipedia_tests.utils import file, attach
from config import config

if config.context == 'bstack':
    load_dotenv(file.env('.env.bstack'))
elif config.context == 'local_real':
    load_dotenv(file.env('.env.local_real'))
else:
    load_dotenv(file.env('.env.local_emulator'))

remote_url = os.getenv('REMOTE_URL')
device_name = os.getenv('DEVICE_NAME')

if config.context == 'bstack':
    apk_path = os.getenv('APP')
else:
    apk_path = file.apk_app_alpha_universal_release()


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


def driver_options():
    if config.context == 'local_emulator':
        options = UiAutomator2Options().load_capabilities({
            "app": apk_path,
            "appWaitActivity": "org.wikipedia.*"
        })

    if config.context == 'bstack':
        options = UiAutomator2Options().load_capabilities({
            "platformName": os.getenv('PLATFORM_NAME'),
            "platformVersion": os.getenv('PLATFORM_VERSION'),
            "deviceName": os.getenv('DEVICE_NAME'),
            "app": os.getenv('APP'),
            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                "userName": os.getenv('USER_NAME'),
                "accessKey": os.getenv('ACCESS_KEY')
            }
        })

    return options
