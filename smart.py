import requests,os
tid=os.getenv('TID')
tgtoken=os.getenv('TG_TOKEN')
def opens(s=None):
	r = s.__file__ if s	else __file__
	os.system(f'subl {r}')
	pass

def stg(t):
	if t:return requests.get(f'https://api.telegram.org/bot332219102:{tgtoken}/sendMessage?chat_id={tid}&text={t}')
