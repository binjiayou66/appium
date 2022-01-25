import os

from appium.webdriver import Remote
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder

# Example

# caps = {}
# caps["platformName"] = "ios"
# caps["bundleId"] = "com.kangmeng.zstyd"
# # caps["automationName"] = "xcuitest"
# caps["automationName"] = "flutter"
# caps["deviceName"] = "iPhone 13"
# caps["platformVersion"] = "15.0"
# caps["noReset"] = True

# driver = Remote(
#     'http://localhost:4723/wd/hub',
#     dict(
#         platformName='iOS',
#         automationName='flutter',
#         # packageName='com.cloudr.cd.doctor',
#         deviceName='iPhone 13',
#         bundleId='com.kangmeng.zstyd',
#         platformVersion='15.0',
#         noReset=True
#     ))

driver = Remote(
    'http://localhost:4723/wd/hub',
    dict(
        platformName='Android',
        automationName='flutter',
        appActivity='.MainActivity',
        deviceName='OCE-AN10',
        platformVersion='10.0',
        noReset=True,
        # packageName='com.cloudr.cd.doctor',
        app='/Users/andy/Desktop/clouddoctor.apk'
    ))

finder = FlutterFinder()

text_finder = finder.by_text('同意协议')
text_element = FlutterElement(driver, text_finder)
text_element.click()


# text1_finder = finder.by_text('跳过 2')
# driver.execute_script('flutter:waitFor', text1_finder, 500)
# text1_element = FlutterElement(driver, text1_finder)
# text1_element.click()
# print(text1_element.text)

input_finder = finder.by_value_key('account')
driver.execute_script('flutter:waitFor', input_finder)
#driver.element_send_keys(finder.by_type('TextFormField'), 'I can enter text')
input_element = FlutterElement(driver, input_finder)
input_element.send_keys('17316911511')
print(input_element.text)

#driver.execute_script('flutter:waitFor', input_element.text == "17316911511")

input_finder1 = finder.by_value_key('code')
#driver.element_send_keys(finder.by_type('TextFormField'), 'I can enter text')
input_element1 = FlutterElement(driver, input_finder1)
input_element1.send_keys('1111')
print(input_element1.text)

login_finder = finder.by_text('登录')
login_element = FlutterElement(driver, login_finder)
print(login_element.text)
login_element.click()

mine_button = finder.by_text('我的')
driver.execute_script('flutter:waitFor', mine_button)
mine_element = FlutterElement(driver, mine_button)
print(mine_element.text)
mine_element.click()

back_finder = finder.page_back()
back_element = FlutterElement(driver, back_finder)
back_element.click()

tooltip_finder = finder.by_tooltip("Increment")
driver.execute_script('flutter:waitFor', tooltip_finder, 100)

floating_button_element = FlutterElement(driver, tooltip_finder)
floating_button_element.click()

counter_finder = finder.by_value_key("counter")
counter_element = FlutterElement(driver, counter_finder)
print(counter_element.text)
