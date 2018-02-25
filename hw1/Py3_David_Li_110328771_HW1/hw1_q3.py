
import urllib.request
r = urllib.request.urlopen("http://dataquestio.github.io/web-scrapingpages/simple.html")
soup = BeautifulSoup(r, 'html.parser')

