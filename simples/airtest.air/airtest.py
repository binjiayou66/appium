import sys 
sys.path.append("..") 

from time import sleep
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from auto_test import AutoTest

auto = AutoTest()


poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").offspring("cn.dreamplus.wentangdoctor:id/home_app_bar_layout").offspring("cn.dreamplus.wentangdoctor:id/rl_item").offspring("cn.dreamplus.wentangdoctor:id/rv_top_actions").child("android.widget.LinearLayout")[7].offspring("android.widget.FrameLayout").click()

sleep(5)

auto.stepTextInScreen('去完成')
