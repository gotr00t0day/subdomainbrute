import requests
from fake_useragent import UserAgent
from colorama import Fore, Back, Style

# by c0deNinja

host = "reddit.com"
wordlist = "wordlist.txt"
try:
    with open(wordlist, 'r') as f:
        datalist = f.readlines()
except IOError:
    print("File not found!")

ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}
for subs in datalist:
    subslist = subs.strip()
    r = requests.get("https://" + subslist + "." + host, headers=header)
    if r.status_code == 200: 
       print(Fore.GREEN + subslist + "." + host)
