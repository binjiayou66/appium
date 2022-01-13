from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver

from baidu_aip_test import cordinate


def screenCordinateStep(driver: WebDriver, text):
    data = driver.get_screenshot_as_png()
    point = cordinate(text, data)
    if not point:
        print('未找到元素')
        return
    TouchAction(driver=driver).tap(
        x=point['x'], y=point['y']).release().perform()
    sleep(3)


def main():
    caps = {}
    caps["platformName"] = "ios"
    caps["bundleId"] = "com.kangmeng.zstyd"
    caps["automationName"] = "xcuitest"
    caps["deviceName"] = "iPhone 13"
    caps["platformVersion"] = "15.0"
    caps["noReset"] = True

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    driver.implicitly_wait(3)
    # element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="任务中心")
    # element.click()

    # driver.implicitly_wait(3)
    # element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="历史任务")
    # element.click()

    screenCordinateStep(driver=driver, text='任务中心')
    screenCordinateStep(driver=driver, text='去完成')
    screenCordinateStep(driver=driver, text='审核通过')

    driver.quit()


if __name__ == "__main__":
    main()
