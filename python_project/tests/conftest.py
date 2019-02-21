import pytest
import os

from appium import webdriver

EXECUTOR = 'http://0.0.0.0:4723/wd/hub'


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Remote(
        command_executor=EXECUTOR,
        desired_capabilities={
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': 'Nexus 5',
            'app': os.path.abspath('/root/tmp/Ali.apk')
        }
    )
    driver.implicitly_wait(5)
    return driver
