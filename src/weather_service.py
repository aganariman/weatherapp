import requests
import datetime
import sys

url = 'https://api.openweathermap.org/data/2.5/forecast'
appid = 'INSERT_YOUR_API_KEY_HERE'
units = 'metric'

def __RequestWeatherForecast(params):
    try:
        resp = requests.get(url=url, params=params)
        data = resp.json()
        return data
    except requests.exceptions.RequestException as e:
        print(e.strerror) #print to log file
        raise Exception(e)

def __getWeatherForecast(lat, lon):
    params = dict(
        lat=lat,
        lon=lon,
        units=units,
        appid=appid
    )
    return __RequestWeatherForecast(params)

def __getWeatherForecastByZip(zipcode):
    params = dict(
        zip=zipcode,
        units=units,
        appid=appid
    )
    return __RequestWeatherForecast(params)

def __buildForecastSummary(fullforecast):
    summary = {}
    summary["results"] = {}
    summary["isSuccess"] = fullforecast["cod"] == '200'
    summary["message"] = fullforecast["message"]

    if(not summary["isSuccess"]):
        return summary

    for item in fullforecast['list']:
        dt = datetime.datetime.utcfromtimestamp(item['dt'])
        shortdate = datetime.datetime(dt.year, dt. month, dt.day)
        day = str(shortdate.timestamp())
        if not day in summary["results"]: 
            summary["results"][day] = {}
            summary["results"][day]["dt_txt"] = shortdate.strftime('%Y-%m-%d')
            summary["results"][day]["temp_min"] = sys.maxsize
            summary["results"][day]["temp_max"] = -sys.maxsize
            summary["results"][day]["precipitation"] = {}
            summary["results"][day]["precipitation"]["rain"] = 0.0
            summary["results"][day]["precipitation"]["snow"] = 0.0

        temp = item["main"]["temp"]
        temp_max = summary["results"][day]["temp_max"]
        if temp > temp_max:
            temp_max = temp

        if item["main"]["temp"] > summary["results"][day]["temp_max"]:
            summary["results"][day]["temp_max"] = item["main"]["temp"]

        if item["main"]["temp"] < summary["results"][day]["temp_min"]:
            summary["results"][day]["temp_min"] = item["main"]["temp"]

        #item can be missing rain or snow precipation info
        if "rain" in item:
            summary["results"][day]["precipitation"]["rain"] += item["rain"]["3h"]

        if "snow" in item:
            summary["results"][day]["precipitation"]["snow"] += item["snow"]["3h"]

    return summary


def getFiveDayForecastSummary(lat, lon):
    return __buildForecastSummary(__getWeatherForecast(lat, lon))

def getFiveDayForecastSummaryByZip(zipcode):
    return __buildForecastSummary(__getWeatherForecastByZip(zipcode))