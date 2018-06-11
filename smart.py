import requests,os
from pymsgbox import alert
from bs4 import BeautifulSoup
tid=os.getenv('TID')
tgtoken=os.getenv('TG_TOKEN')
def opens(s=None):
	r = s.__file__ if s	else __file__
	os.system(f'subl {r}')
	pass

def stg(t):
	if not (tid and tgtoken) :alert('config telegram')
	if t:return requests.get(f'https://api.telegram.org/bot{tgtoken}/sendMessage?chat_id={tid}&text={t}')


