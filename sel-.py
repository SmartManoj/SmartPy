#run in cmd in interactive py and use exec()
#exec(open('D:\Gits\SmartPy\sel-.py').read())
from selenium import webdriver
from pymsgbox import *
from time import *
from pyautogui import *
import os
from glob import glob
import pyperclip,subprocess
from datetime import datetime
dn=lambda :(str(datetime.now().time()).split('.')[0])
un=os.getenv('username')
if not globals().get('selp'):selp='x'
rk=selp=='x'
if rk:selp='1'
fpp=glob(r'C:\Users\{}\AppData\Roaming\Mozilla\Firefox\Profiles\*.Sel{}'.format(un,selp))[0]
def stm():
	try:
		b.switch_to_window(b.window_handles[0])
		b.switch_to.default_content()
	except  Exception as e:
		print(e);exit()
def sp(r):
	try:
		return subprocess.check_output(r,shell=True)
	except Exception as e:
		print(e)

def r(i):
	q=r'wmic process get name,parentprocessid,processid | findstr "\<%s\>"' %(i,)
	a=sp(q)
	a=(a.decode().split()) 
	if a[3:] and a[3]=='firefox.exe':return (a[5])
	for k in a[5::3]:
		i=(r(k))
	return i

def r(i):
	q=r'wmic process get name,parentprocessid,processid | findstr "\<%s\>"' %(i,)
	a=sp(q)
	a=(a.decode().split('\r\r\n')) [:-1]
	a=[a.split() for a in a]
	if a[1:] and a[1][0]=='firefox.exe':return (a[1][2])
	for k in a[1:]:
		if k[0]=='cmd.exe':continue
		i=(r(k[2]))
	return i

def ff():
	z=selp if not rk else ''
	q='tasklist /v  | findstr /C:"ahkz{} - py"'.format(z)
	a=sp(q)
	a=(a.decode().split()[1]) 
	return r(a)


def copy():
	print('selp={}'.format(selp),file=open(r'C:\Windows\Temp\selp.txt','w'))
	_x=b.command_executor._url
	_c=b.session_id
	# fid=ff()
	fid=None
	# print(fid)
	# sp('nircmd win min process /{}'.format(fid))
	vbvb='''
url = '{}'
b = SessionRemote(command_executor=url,desired_capabilities={{}})
b.session_id="{}"
fid={}
'''.format(_x,_c,fid)
	with open(r'C:\Windows\Temp\sel{}.txt'.format(selp),'w') as f:
		print(vbvb,file=f)

def bb(ch=0):
	global b
	if ch==0:
		fp = webdriver.FirefoxProfile(fpp)
		b = webdriver.Firefox(fp)
		hotkey('alt','space','n')

	elif ch==1:b = webdriver.PhantomJS(r'D:\1.Manoj\2.Soft-war\5.Rest\phantomjs-2.1.1-windows\bin\phantomJS')
	copy()
	bes=b.execute_script
	bfc=b.find_element_by_css_selector
	bfcs=b.find_elements_by_css_selector
	bfx=b.find_element_by_xpath
	bfxs=b.find_elements_by_xpath
	globals().update(locals())

import re
bcu=lambda :b.current_url
def bes(a):
	a=re.sub(r'(?<!\\)\$','document.querySelector',a)
	a=a.replace(r'\$','$')
	return b.execute_script(a)

def bl():
	b.get('about:blank')
	




bb()
# copy()

driver=b
browser=b
