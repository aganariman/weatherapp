import weather_service
       
data = weather_service.getFiveDayForecastSummary(37.941113, 27.341944)
print("Date".ljust(12), "Temperature".ljust(14), "Precipitation(Rain)  Precipitation(Snow)")

for item in data:
    temp = '%0.0f' % data[item]["temp_max"] + "/" + '%0.0f' % data[item]["temp_min"]
    print(data[item]["dt_txt"].ljust(12), temp.ljust(14), ('%0.0f' % data[item]["precipitation"]["rain"]).ljust(20), ('%0.0f' % data[item]["precipitation"]["snow"]).ljust(14))