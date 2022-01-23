import os,sys,subprocess
subprocess.getoutput("pip install requests")
import requests,sys,os,time
#هاا حبي تريد تخمط 
import requests,time,random,os,sys
TOKEN=input('\033[1;33m 𝚃𝙾𝙺𝙴𝙽 :')
ID=input('\033[1;31m 𝙸𝙳 :')
os.system('clear')
MM=int(input('\033[1;31m [^]\033[1;36m AMOUNT OF USER :\033[1;37m'))
os.system('clear')
oip='qwertyuioplkjhgfdsazxcvbnm'
upper = 'ABCDEFGHIKLMNOPQSTVWSYZ'
number = '0987654321'
uu7='_'
all  = number + upper +oip
length = 1
for e in range(MM):
	u= ''.join(random.sample(all,length))
	s= ''.join(random.sample(all,length))
	r= ''.join(random.sample(all,length))
	kk=(r+r+r+s+s)
	ree = requests.get(f'https://t.me/{kk}').text
	if 'tgme_username_link' in ree:
		Account = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text=• 𝚄𝚂𝙴𝚁 𝙵𝙾𝚁 𝚈𝙾𝚄 ♕︎\n ◈ ━━━━━━━ ❌ ━━━━━━━ ◈\n\n-𝚄𝚂𝙴𝚁 : @{kk} ‼️\n\n◈ ━━━━━━━ ❌ ━━━━━━━ ◈\n-𝙱𝚈 :  ⭕')
		print(f'\033[1;32m Available:{kk} ')
		
	else:
		print(f' \033[1;31mNOT Available:{kk}')
