import requests,os,sys,pickle,subprocess
from pymsgbox import alert
from bs4 import BeautifulSoup
from datetime import datetime,timedelta
from time import sleep
tid=os.getenv('TID')
u=os.getenv('username') =='Smart'
tgtoken=os.getenv('TG_TOKEN')
df= r'D:\Gits\SmartPy\smart.py' if u  else __file__
def opens(s=None):
	# print(s in sys.modules)
	if type(s)==str:
		s=exec(f'import {s}')
	r = s.__file__ if s	else df
	os.system(f'subl {r}')

def dir2(a):
	return [i for i in a if not i.startswith('_')]
def pk(s):
	pickle.dump(s,open('tmp','wb'))

def pkl():
	return pickle.load(open('tmp','b'))
	
def done(t=None):
	alert('Done',timeout=t)
def stg(t,tid=tid):
	if not (tid and tgtoken) :alert('config telegram')
	if t:return requests.get(f'https://api.telegram.org/bot{tgtoken}/sendMessage?chat_id={tid}&text={t}')
ctd=lambda :(str(datetime.now()).split('.')[0])
ct=lambda :(str(datetime.now().time()).split('.')[0])

parse_request_header=lambda x: [i.split(': ',1) for i in x.splitlines()[1:]]
parse_post_data=lambda a: [i.split('=') for i in a.splitlines()] 


if __name__ == '__main__':
	if u:
		import setup
		subprocess.run(['gt.cmd'])

