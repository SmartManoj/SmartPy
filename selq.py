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
