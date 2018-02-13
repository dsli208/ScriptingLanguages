from bs4 import BeautifulSoup

import urllib.request

def get_daily_forecast(day):
    period = day.find(class_="period-name").get_text()
    short_desc = day.find(class_="short-desc").get_text()
    temp = day.find(class_="temp").get_text()
    return period, short_desc, temp 

def get_daily_description(day):
    img = day.find("img")
    desc = img['title']
    return desc


weather_url = "http://forecast.weather.gov/MapClick.php?lat=40.9128&lon=-73.1399"
r = urllib.request.urlopen(weather_url)
soup = BeautifulSoup(r,"html.parser")
daily_forecasts = soup.find_all(class_="tombstone-container")
print("Number of records:" , len(daily_forecasts))
print("Soup length: ", len(soup))
print("-------------------------------------------")
tonight = daily_forecasts[0]
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)
print("-------------------------------------------")
img=tonight.find("img")
desc=img["title"]
print(desc)

f = open("weather_log.txt","a")

for forecast in daily_forecasts:
    period, short_desc, temp = get_daily_forecast(forecast)
    desc = get_daily_description(forecast)
    f.write(period + " " + short_desc + " " + temp + " " + desc + '\n')

f.close()
