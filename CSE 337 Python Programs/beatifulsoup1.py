from bs4 import BeautifulSoup
from urllib2 import urlopen, Request
with open("index.html") as fp:
    soup = BeautifulSoup(fp)

soup = BeautifulSoup("<html>data</html>")