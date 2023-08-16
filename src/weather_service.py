import requests
import datetime
import sys

url = 'https://api.openweathermap.org/data/2.5/forecast'
appid = 'INSERT_YOUR_API_KEY_HERE'
units = 'metric'

def getWeatherForecast(lat, lon):
    params = dict(
        lat=lat,
        lon=lon,
        units=units,
        appid=appid
    )

    resp = requests.get(url=url, params=params)
    data = resp.json()

    return data

def getWeatherForecastByZip(zipcode):
    params = dict(
        zip=zipcode,
        units=units,
        appid=appid
    )

    resp = requests.get(url=url, params=params)
    data = resp.json()

    return data

def __buildForecastSummary(fullforecast):
    summary = {}
    for item in fullforecast['list']:
        dt = datetime.datetime.utcfromtimestamp(item['dt'])
        shortdate = datetime.datetime(dt.year, dt. month, dt.day)
        day = str(shortdate.timestamp())
        if not day in summary: 
            summary[day] = {}
            summary[day]["dt_txt"] = shortdate.strftime('%Y-%m-%d')
            summary[day]["temp_min"] = sys.maxsize
            summary[day]["temp_max"] = -sys.maxsize
            summary[day]["precipitation"] = {}
            summary[day]["precipitation"]["rain"] = 0.0
            summary[day]["precipitation"]["snow"] = 0.0

        temp = item["main"]["temp"]
        temp_max = summary[day]["temp_max"]
        if temp > temp_max:
            temp_max = temp

        if item["main"]["temp"] > summary[day]["temp_max"]:
            summary[day]["temp_max"] = item["main"]["temp"]

        if item["main"]["temp"] < summary[day]["temp_min"]:
            summary[day]["temp_min"] = item["main"]["temp"]

        #item can be missing rain or snow precipation info
        if "rain" in item:
            summary[day]["precipitation"]["rain"] += item["rain"]["3h"]

        if "snow" in item:
            summary[day]["precipitation"]["snow"] += item["snow"]["3h"]

    return summary


def getFiveDayForecastSummary(lat, lon):
    return __buildForecastSummary(getWeatherForecast(lat, lon))

def getFiveDayForecastSummaryByZip(zipcode):
    return __buildForecastSummary(getWeatherForecastByZip(zipcode))