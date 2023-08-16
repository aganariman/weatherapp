import weather_service

# izmir weather
# data = weather_service.getWeatherForecast(37.941113, 27.341944)

# print(len(data['list']))

# for item in data['list']:
#     print(item['dt'])
#     print(datetime.datetime.utcfromtimestamp(item['dt']).strftime('%Y-%m-%d %H:%M:%S'))
       
data = weather_service.getFiveDayForecastSummary(37.941113, 27.341944)
print (data)