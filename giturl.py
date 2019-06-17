# alias gh="xdg-open https://github.$(git config remote.origin.url | cut -f2 -d.)"
import  subprocess
subprocess.run('git config remote.origin.url'.split())#,stdout=subprocess.PIPE)
print(p.stdout)