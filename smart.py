import requests,os,sys
from pymsgbox import alert
from bs4 import BeautifulSoup
from datetime import datetime,timedelta
from time import sleep
tid=os.getenv('TID')
tgtoken=os.getenv('TG_TOKEN')
def opens(s=None):
	print(s in sys.modules)
	if type(s)==str:
		s=exec(f'import {s}')
	r = s.__file__ if s	else __file__
	os.system(f'subl {r}')
	pass
def done():
	alert('Done',timeout=3)
def stg(t,tid=tid):
	if not (tid and tgtoken) :alert('config telegram')
	if t:return requests.get(f'https://api.telegram.org/bot{tgtoken}/sendMessage?chat_id={tid}&text={t}')
ctd=lambda :(str(datetime.now()).split('.')[0])
ct=lambda :(str(datetime.now().time()).split('.')[0])

parse_request_header=lambda x: [i.split(': ',1) for i in x.splitlines()[1:]]
parse_post_data=lambda a: [i.split('=') for i in a.splitlines()] 


if __name__ == '__main__':
	opens('tkinter')

	import webbrowser
	# webbrowser.open('https://github.com/SmartManoj/SmartPy/edit/master/smart.py')