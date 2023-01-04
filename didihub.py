import requests
import json
import sys
import os
import time
from requests import session
from prettytable import PrettyTable
import datetime
from datetime import datetime
from random import SystemRandom
import random
from termcolor import cprint
import termcolor

P = '\033[95m'
CYAN = '\033[96m'
DARK = '\033[36m'
B = '\033[94m'
G = '\033[92m'
Y = '\033[93m'
R = '\033[91m'
BO = '\033[1m'
UNDER = '\033[4m'
N = '\033[0m'




def besar ():
			periodeberikutnya()
			a = open("periode.txt",'r')
			b = a.read()
			c = ['5','6','7','8','9']
			d = random.SystemRandom()
			e = d.choice(c)
			print(f"Tebakan Angka : {e}")
			print(f"{G}PERIODE BERIKUTNYA => {Y}{b} {B}PREDIKSI => {Y}BESAR")
			countdownTimer()
			taruhanbesar()
			
def kecil ():
			periodeberikutnya()
			a = open("periode.txt",'r')
			b = a.read()
			c = ['0','1','2','3','4']
			d = random.SystemRandom()
			e = d.choice(c)
			print(f"Tebakan Angka : {e}")
			print(f"{G}PERIODE BERIKUTNYA => {Y}{b} {B}PREDIKSI => {G}KECIL")
			countdownTimer()
			taruhankecil()
			
			
def countdownTimer ():
    aa = datetime.now()
    bb = aa.strftime("%S")
    total_second = 60-int(bb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{mins:02d}:{secs:02d}', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def periodeberikutnya ():
 data = {'type':'2'}
 a = requests.Session()
 b = a.get('https://45.76.187.36/api/main/lottery/curRound?type=2', data = data)
 c = json.loads(b.text)
 d = c.get("period")
 with open("periode.txt",'w') as f:
  f.write(str(d))
  f.close()
  
  
def taruhanbesar ():
 data = {
 'page':'1',
 'count':'20',
 'type':'2'
 }
 a = requests.Session()
 b = a.get("https://45.76.187.36/api/main/lottery/rounds?page=1&count=20&type=2", data = data)
 c = json.loads(b.text)
 d = c.get('items')
 e = d[0].get('period')
 f = d[0].get('number')
 with open("nomor.txt",'w') as g:
  g.write(str(f))
  g.close()
 h = open("nomor.txt",'r')
 i = h.read()
 if i > '4':
  print(f"{BO}{DARK}HASIL\n  ╰─▸ {Y}B{DARK}/{G}K {DARK}: {G}WIN BESAR {DARK}➤ {Y}ANGKA : {G}{i}\n")
  rumus()
 elif i < '5':
  print(f"{BO}{DARK}HASIL\n  ╰─▸ {Y}B{DARK}/{G}K {DARK}: {R}LOSE KECIL {DARK}➤ {Y}ANGKA : {R}{i}\n")
  rumuslawan()
def taruhankecil ():
 data = {
 'page':'1',
 'count':'20',
 'type':'2'
 }
 a = requests.Session()
 b = a.get("https://45.76.187.36/api/main/lottery/rounds?page=1&count=20&type=2", data = data)
 c = json.loads(b.text)
 d = c.get('items')
 e = d[0].get('period')
 f = d[0].get('number')
 with open("nomor.txt",'w') as g:
  g.write(str(f))
  g.close()
 h = open("nomor.txt",'r')
 i = h.read()
 if i > '4':
  print(f"{BO}{DARK}HASIL\n  ╰─▸ {Y}B{DARK}/{G}K {DARK}: {R}LOSE BESAR {DARK}➤ {Y}ANGKA : {R}{i}\n")
  rumus()
 elif i < '5':
  print(f"{BO}{DARK}HASIL\n  ╰─▸ {Y}B{DARK}/{G}K {DARK}: {G}WIN KECIL {DARK}➤ {Y}ANGKA : {G}{i}\n")
  rumuslawan()
def rumus ():
 data = {
 'page':'2',
 'count':'50',
 'type':'2'
 }
 a = requests.Session()
 b = a.get('https://45.76.187.36/api/main/lottery/rounds?page=2&count=50&type=2',data = data)
 c = json.loads(b.text)
 d = c.get('items')
 e = d[48].get('number')
 with open("rumus.txt",'w') as f:
  f.write(str(e))
  f.close()
 g = open("rumus.txt",'r').read()
 if g == '0':
  kecil()
 elif g == '1':
  kecil()
 elif g == '2':
  kecil()
 elif g == '3':
  kecil()
 elif g == '4':
  kecil()
 elif g == '5':
  besar()
 elif g == '6':
  besar()
 elif g == '7':
  besar()
 elif g == '8':
  besar()
 elif g == '9':
  besar()
def rumuslawan ():
 data = {
 'page':'2',
 'count':'50',
 'type':'2'
 }
 a = requests.Session()
 b = a.get('https://45.76.187.36/api/main/lottery/rounds?page=2&count=50&type=2',data = data)
 c = json.loads(b.text)
 d = c.get('items')
 e = d[48].get('number')
 with open("rumus.txt",'w') as f:
  f.write(str(e))
  f.close()
 g = open("rumus.txt",'r').read()
 if g == '0':
  kecil()
 elif g == '1':
  besar()
 elif g == '2':
  besar()
 elif g == '3':
  besar()
 elif g == '4':
  besar()
 elif g == '5':
  besar()
 elif g == '6':
  kecil()
 elif g == '7':
  kecil()
 elif g == '8':
  kecil()
 elif g == '9':
  kecil()
  
os.system("clear")
b = datetime.now()
f = b.strftime("%Y%m%d")
d = '20231128'
if f >= d:
	os.system("clear")
	print("")
	print(Y+"SCRIPT TELAH KEDALUARSA")
	print("HUBUNGI PENJUAL UNTUK SCRIPT BARU")
	print("CONTACT : @sarahanggraeny")
	time.sleep(10)
	exit()
else:
	os.system("clear")
	print(G+"╭━━━┳━━┳━━━┳━━┳╮╱╭┳╮╱╭┳━━╮╱╭━━━┳━━━┳━━━┳━━━┳━━━━╮\n╰╮╭╮┣┫┣┻╮╭╮┣┫┣┫┃╱┃┃┃╱┃┃╭╮┃╱┃╭━╮┃╭━━┫╭━╮┃╭━╮┃╭╮╭╮┃\n╱┃┃┃┃┃┃╱┃┃┃┃┃┃┃╰━╯┃┃╱┃┃╰╯╰╮┃┃╱╰┫╰━━┫╰━╯┃┃╱┃┣╯┃┃╰╯\n╱┃┃┃┃┃┃╱┃┃┃┃┃┃┃╭━╮┃┃╱┃┃╭━╮┃┃┃╱╭┫╭━━┫╭━━┫╰━╯┃╱┃┃\n╭╯╰╯┣┫┣┳╯╰╯┣┫┣┫┃╱┃┃╰━╯┃╰━╯┃┃╰━╯┃╰━━┫┃╱╱┃╭━╮┃╱┃┃\n╰━━━┻━━┻━━━┻━━┻╯╱╰┻━━━┻━━━╯╰━━━┻━━━┻╯╱╱╰╯╱╰╯╱╰╯")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	rumus()