import shutil
import subprocess
import os.path as op
p=(subprocess.run('py -0p',stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.decode().splitlines()[1:])
f='smart.py'
for i in p:
	i=i.split()[-1]
	a=op.join(op.split(i)[0],'Lib')
	# print(a)
	shutil.copy('smart.py',a)
print('done')