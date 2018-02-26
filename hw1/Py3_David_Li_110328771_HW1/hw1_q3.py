from bs4 import BeautifulSoup
import urllib.request
r = urllib.request.urlopen("https://finance.google.com/finance/market_news")
soup = BeautifulSoup(r, 'html.parser')

# lines 12878 and 12901 for examples of how to extract from the web page source code
# get the list of articles
articles = soup.find_all(class_="g-section news sfe-break-bottom-16")

# open text file and csv for writing
ftxt = open('top10articles.txt', 'w')


# Find TITLE, SOURCE, DATE
for article in articles:
     title = article.find(class_="name").get_text()
     source = article.find(class_="src").get_text()
     date = article.find(class_="date").get_text()

     # write to text
     commaLine = title + ',' + source + ',' + date + '\n'
     ftxt.write(commaLine)

ftxt.close()
