#!/usr/bin/python3
import requests

url = 'https://stepic.org/media/attachments/course67/3.6.3/'
path = '699991.txt'

while(1):
    r = requests.get(url + path)
    path = r.text
    print(path)
    if(r.status_code != 200):
        break
