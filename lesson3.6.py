#!/usr/bin/python3
import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/997.txt')
t = r.text
d = t.splitlines()
n = len(d)
print(n)
