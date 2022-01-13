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


def stepCordinate(driver: WebDriver, x: int, y: int):
    TouchAction(driver=driver).tap(x=x, y=y).release().perform()
    _stepHoldOn()


def stepTextInScreen(driver: WebDriver, text):
    data = driver.get_screenshot_as_png()
    point = cordinate(text, data)
    if not point:
        print('未找到元素')
        return
    TouchAction(driver=driver).tap(
        x=point['x'], y=point['y']).release().perform()
    _stepHoldOn()


def stepAccessibilityId(driver: WebDriver, id):
    element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=id)
    element.click()
    _stepHoldOn()


def stepBack(driver: WebDriver):
    stepCordinate(driver=driver, x=AppBarBackXIphone,
                  y=AppBarBackYIphoneNotRegular)


def _stepHoldOn():
    sleep(StepSleepDuration)


def main():
    caps = {}
    caps["platformName"] = "ios"
    caps["bundleId"] = "com.kangmeng.zstyd"
    caps["automationName"] = "xcuitest"
    caps["deviceName"] = "iPhone 13"
    caps["platformVersion"] = "15.0"
    caps["noReset"] = True

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    # element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="任务中心")
    # element.click()

    # _stepHoldOn()
    # element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="历史任务")
    # element.click()

    # stepTextInScreen(driver=driver, text='任务中心')
    # stepTextInScreen(driver=driver, text='去完成')
    # stepTextInScreen(driver=driver, text='审核通过')

    stepAccessibilityId(driver=driver, id="任务中心")
    stepBack(driver=driver)

    driver.quit()


if __name__ == "__main__":
    main()
