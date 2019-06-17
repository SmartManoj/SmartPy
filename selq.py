import re
from time import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
class SessionRemote(webdriver.Remote):
	def start_session(self, desired_capabilities, browser_profile=None):
		self.w3c = True

	
a=r'C:\Windows\Temp\selp.txt'
a=(open(a). read());exec(a)
a=r'C:\Windows\Temp\sel{}.txt'.format(selp)
a=(open(a).read());exec(a)
bcu=lambda :b.current_url
def bes(a):
	a=re.sub(r'(?<!\\)\$','document.querySelector',a)
	a=a.replace(r'\$','$')
	return b.execute_script(a)

bfc=b.find_element_by_css_selector
bfcs=b.find_elements_by_css_selector
bfx=b.find_element_by_xpath
bfxs=b.find_elements_by_xpath
driver=b
browser=b
# ==========================
# Use your code below
# ==========================

if __name__ == '__main__':
	# b.get('http://google.com')
	from smart import *
	# print(opens(webdriver))
	# alert = driver.switch_to.alert()
	# print(driver.current_window_handle)
	# print(driver.window_handles[0])
	driver.switch_to.default_content()
	driver.execute_script("alert('qwer');")

	# print(EC.alert_is_present())
	# alert=browser.switch_to.alert
	# alert.accept()
	# sleep(5)
	# print(b.window_handles)
	# alert = browser.(b.window_handles)
	from time import sleep
	while EC.alert_is_present()(driver):
		driver.switch_to.window(driver.current_window_handle)
		sleep(2)
		print('iruku')
	   
	driver.execute_script("alert('qweeer');")