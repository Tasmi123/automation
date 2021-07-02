import time
import unittest
import pytest
from selenium import webdriver

from selenium.webdriver.common.keys import Keys


class TestCaseChrome(unittest.TestCase):

    def setUp(self):

        BROWSERSTACK_URL = 'https://oysheetasmi_39xAL7:jZFfP6qouUuJ842JVJCJ@hub-cloud.browserstack.com/wd/hub'

        desired_cap = {

            'os': 'Windows',
            'os_version': '10',
            'browser': 'Chrome',
            'browser_version': '89.0',
            'name': 'login test buy Appliances_chrome',
            'build':'BA_login'

        }

        self.driver = webdriver.Remote(
            command_executor=BROWSERSTACK_URL,
            desired_capabilities=desired_cap
        )

        self.driver.get("http://18.134.60.157/customer/account/login")
        self.driver.maximize_window()
        # driver.implicitly_wait(3)
    def test_A(self):
        self.driver.find_element_by_css_selector("div[class='field email required'] input[id='email']").send_keys("tasmitamanna123@gmail.com")
        self.driver.find_element_by_css_selector("div[class='field password required'] input[id='pass'").send_keys("hello123!@#")
        self.driver.find_element_by_css_selector("div[class='actions-toolbar'] button[class='action login primary']").click()
        time.sleep(10)
        elem=self.driver.find_element_by_css_selector(".ba-greet > .logged-in").text
        elem=str(elem)
        if (elem=="Hello, tasmi"):
            self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "logged On"}}')
        else:
            self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "not looged on"}}')

    def test_B(self):
        self.driver.find_element_by_css_selector("div[class='field email required'] input[id='email']").send_keys("tasmitamanna123@gmail.com")
        self.driver.find_element_by_css_selector("div[class='field password required'] input[id='pass'").send_keys("abcd")
        self.driver.find_element_by_css_selector("div[class='actions-toolbar'] button[class='action login primary']").click()
        time.sleep(10)
        elem = self.driver.find_element_by_css_selector(".not-logged-in.ba-desktop-not-logged-in").text
        elem = str(elem)
        print(self.assertNotEquals(elem, "Hello, tasmi"))

        if (elem!="Hello, tasmi"):
            self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Not Logged On"}}')
        else:
            self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "logged on"}}')

        #driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
    def tearDown(self):
        self.driver.quit()
class TestCasefirefox(unittest.TestCase):

    def setUp(self):

        BROWSERSTACK_URL = 'https://oysheetasmi_39xAL7:jZFfP6qouUuJ842JVJCJ@hub-cloud.browserstack.com/wd/hub'

        desired_cap = {

            'os': 'Windows',
            'os_version': '10',
            'browser': 'Firefox',
            'browser_version': 'latest',
            'name': 'login test buy Appliances_firefox',
            'build':'BA_login'

        }

        self.driver = webdriver.Remote(
            command_executor=BROWSERSTACK_URL,
            desired_capabilities=desired_cap
        )

        self.driver.get("http://18.134.60.157/customer/account/login")
        self.driver.maximize_window()


        # driver.implicitly_wait(3)
    def test_A(self):
        self.driver.find_element_by_css_selector("div[class='field email required'] input[id='email']").send_keys("tasmitamanna123@gmail.com")
        self.driver.find_element_by_css_selector("div[class='field password required'] input[id='pass'").send_keys("hello123!@#")
        self.driver.find_element_by_css_selector("div[class='actions-toolbar'] button[class='action login primary']").click()
        time.sleep(10)
        elem=self.driver.find_element_by_css_selector(".ba-greet > .logged-in").text
        elem=str(elem)
        if (elem=="Hello, tasmi"):
            self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "logged On"}}')
        else:
            self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "not looged on"}}')

    def test_B(self):
        self.driver.find_element_by_css_selector("div[class='field email required'] input[id='email']").send_keys("tasmitamanna123@gmail.com")
        self.driver.find_element_by_css_selector("div[class='field password required'] input[id='pass'").send_keys("abcd")
        self.driver.find_element_by_css_selector("div[class='actions-toolbar'] button[class='action login primary']").click()
        time.sleep(10)
        elem = self.driver.find_element_by_css_selector(".not-logged-in.ba-desktop-not-logged-in").text
        elem = str(elem)
        print(self.assertNotEquals(elem, "Hello, tasmi"))

        if (elem!="Hello, tasmi"):
            self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Not Logged On"}}')
        else:
            self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "logged on"}}')

        #driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
    def tearDown(self):
        self.driver.quit()
class TestCaseIE(unittest.TestCase):

    def setUp(self):

        BROWSERSTACK_URL = 'https://oysheetasmi_39xAL7:jZFfP6qouUuJ842JVJCJ@hub-cloud.browserstack.com/wd/hub'

        desired_cap = {

            'os': 'Windows',
            'os_version': '10',
            'browser': 'IE',
            'browser_version': 'latest',
            'name': 'login test buy Appliances_IE',
            'build':'BA_login'

        }

        self.driver = webdriver.Remote(
            command_executor=BROWSERSTACK_URL,
            desired_capabilities=desired_cap
        )

        self.driver.get("http://18.134.60.157/customer/account/login")
        self.driver.maximize_window()

        # driver.implicitly_wait(3)
    def test_A(self):
        self.driver.find_element_by_css_selector("div[class='field email required'] input[id='email']").send_keys("tasmitamanna123@gmail.com")
        self.driver.find_element_by_css_selector("div[class='field password required'] input[id='pass'").send_keys("hello123!@#")
        self.driver.find_element_by_css_selector("div[class='actions-toolbar'] button[class='action login primary']").click()
        time.sleep(10)
        elem=self.driver.find_element_by_css_selector(".ba-greet > .logged-in").text
        elem=str(elem)
        if (elem=="Hello, tasmi"):
            self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "logged On"}}')
        else:
            self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "not looged on"}}')

    def test_B(self):
        self.driver.find_element_by_css_selector("div[class='field email required'] input[id='email']").send_keys("tasmitamanna123@gmail.com")
        self.driver.find_element_by_css_selector("div[class='field password required'] input[id='pass'").send_keys("abcd")
        self.driver.find_element_by_css_selector("div[class='actions-toolbar'] button[class='action login primary']").click()
        time.sleep(10)
        elem = self.driver.find_element_by_css_selector(".not-logged-in.ba-desktop-not-logged-in").text
        elem = str(elem)
        print(self.assertNotEquals(elem, "Hello, tasmi"))

        if (elem!="Hello, tasmi"):
            self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Not Logged On"}}')
        else:
            self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "logged on"}}')

        #driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')



