import unittest
from appium import webdriver


class IOSBaseTest(unittest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)

    def setUp(self):
        """
        This method instantiates the iOS driver
        """
        desired_caps = {
            "platformName": "iOS",
            "platformVersion": "15.4",
            "automationName": "XCUITest",
            "deviceName": "<IOS SIMULATOR>",
            "app": "<IOS APP ABSOlUTE PATH>"
        }

        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
