import unittest
from appium import webdriver

class AndroidBaseTest(unittest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)

    def setUp(self):
        """
        This method instantiates the Android driver
        """
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "10",
            "automationName": "UiAutomator2",
            "deviceName": "<ANDROID EMULATOR>",
            "app": "<ANDROID APP ABSOLUTE PATH>"
        }

        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()