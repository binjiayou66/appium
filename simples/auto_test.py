from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver

from baidu_aip_test import cordinate

StepSleepDuration = 3
AppBarBackXIphone = 20
AppBarBackYIphoneRegular = 40
AppBarBackYIphoneNotRegular = 90


class AutoTest:
    driver: WebDriver

    def __init__(self):
        # caps = {}
        # caps["platformName"] = "ios"
        # caps["bundleId"] = "com.kangmeng.zstyd"
        # caps["automationName"] = "xcuitest"
        # caps["deviceName"] = "iPhone 13"
        # caps["platformVersion"] = "15.0"
        # caps["noReset"] = True
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "10.0"
        caps["deviceName"] = "OCE-AN10"
        caps["appPackage"] = "cn.dreamplus.wentangdoctor"
        caps["appActivity"] = ".accout.startup.SplashActivity"
        caps["resetKeyboard"] = True
        caps["noReset"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def _stepHoldOn(self):
        sleep(StepSleepDuration)

    def stepCordinate(self, x: int, y: int):
        TouchAction(driver=self.driver).tap(x=x, y=y).release().perform()
        self._stepHoldOn()

    def stepAccessibilityId(self, id):
        element = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value=id)
        element.click()
        self._stepHoldOn()

    def stepTextInScreen(self, text):
        data = self.driver.get_screenshot_as_png()
        point = cordinate(text, data)
        if not point:
            print('未找到元素')
            return
        self.stepCordinate(x=point['x'], y=point['y'])

    def stepBack(self):
        self.stepCordinate(x=AppBarBackXIphone,
                           y=AppBarBackYIphoneNotRegular)

    def __del__(self):
        self.driver.quit()
