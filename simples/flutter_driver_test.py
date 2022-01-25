from time import sleep
import unittest
from appium import webdriver
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder

SleepDuration = 1


class FlutterDriverTest():
    def setUp(self):
        caps = {}
        caps["platformName"] = "ios"
        caps["bundleId"] = "com.kangmeng.zstyd"
        # caps["automationName"] = "xcuitest"
        caps["automationName"] = "flutter"
        caps["deviceName"] = "iPhone 13"
        caps["platformVersion"] = "15.0"
        caps["noReset"] = True

        # caps = {}
        # caps["platformName"] = "Android"
        # caps["platformVersion"] = "10.0"
        # caps["deviceName"] = "OCE-AN10"
        # caps["appPackage"] = "com.zyhealth.app_demo"
        # caps["automationName"] = "flutter"
        # caps["appActivity"] = ".MainActivity"
        # caps["resetKeyboard"] = True
        # caps["noReset"] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.finder = FlutterFinder()

    def test_flutter(self):
        print('AAAA')
        # ele = self.driver.find_element_by_accessibility_id('任务中心')
        # ele.click()
        # text_finder = self.finder.by_value_key("counter")
        # button_finder = self.finder.by_value_key("increment")
        # text_element = FlutterElement(self.driver, text_finder)
        # button_element = FlutterElement(self.driver, button_finder)
        # button_element.click()
        # button_element.click()
        # print('2' == text_element.text)

    def tearDown(self):
        self.driver.quit()


def main():
    fdt = FlutterDriverTest()
    fdt.setUp()
    fdt.test_flutter()
    fdt.tearDown()


if __name__ == '__main__':
    main()
