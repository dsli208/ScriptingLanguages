from bs4 import BeautifulSoup

import urllib.request
r = urllib.request.urlopen("http://forecast.weather.gov/MapClick.php?lat=41.32406000000009&lon=-73.80020999999988#.WpOfLejwZPY")
soup = BeautifulSoup(r, 'html.parser')

