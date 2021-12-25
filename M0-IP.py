#--------------------------->
#Coded By Mokhtar Abdelkreem
#-------------------------->
#Librarys
import requests
import os
import time
import webbrowser
#--------------

print('\033[1;31m Wait Please ...')
time.sleep(3)
os.system('clear')
os.system('xdg-open https://t.me/mo_code')
webbrowser.open('https://t.me/mo_code')
#Banner
print('''
\033[1;35m

_______________________________
|  |_|  |       |  |   |       |
|       |  ___  |  |   |    _
|       | |▀-▀| |  |   |   |_| |
|       | |___| |  |   |    ___|
| ||_|| |       |  |   |   |
|_|   |_|_______|  |___|____

\033[1;36m
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

 Devolper : Mokhtar Abdelkreem

 Inf Dev  : https://dev.page/mokhtar

 Channel  : https://cutt.us/mocode

★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
''')

api ="http://ip-api.com/"
mocode = input("\033[1;34mEnter IP Victim :")
result= requests.get(api+mocode)
print(result.text)



