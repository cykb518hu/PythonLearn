import urllib.request as ur
import urllib.parse as up
from html import unescape
import requests
from bs4 import BeautifulSoup
import io
import sys
import re
from datetime import datetime

requests.packages.urllib3.disable_warnings()
hdrs = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}

http_proxy  = "http://10.152.102.9:8080"
https_proxy  = "https://10.152.102.9:8080"


proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy
            }
youtubeUrl = "https://www.youtube.com/watch?v=X0qRT9nRoFU"
r = requests.get(youtubeUrl, headers = hdrs, proxies=proxyDict, verify=False)
soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'),features="lxml")

youtubeTitle = soup.find('title').text.replace(':',' -').replace('|','-')

youtubeDescription=soup.select('span[class="yt-formatted-string"]')[0].get_text()

print(youtubeTitle)
print(youtubeDescription)


