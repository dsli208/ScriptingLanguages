#import urllib2
from bs4 import BeautifulSoup
#from urllib2 import urlopen, Request

import urllib.request
r = urllib.request.urlopen("https://www.dataquest.io/blog/web-scraping-tutorial-python/")
soup = BeautifulSoup(r, 'html.parser')
print(soup.prettify())

for line in lines:
    if line[:3] == "<p>":
        line_split = line.split("<p>")[1].split("</p>")[0]
    print line_split