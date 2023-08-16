import weather_service
import os
import re

zipCode = re.compile(r"^\d{5}(?:[-\s]\d{4})?$")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

def __GetZipCode():
    zip = 0
    while True:
        zip = input("Please enter a valid US ZipCode: ")
        if zipCode.match(zip):
            break
        else:
            input("Zip code format is not valid! Press enter to try again!")
            cls()
    
    return zip

# izmir      
#data = weather_service.getFiveDayForecastSummary(37.941113, 27.341944)
# den bosch
#data = weather_service.getFiveDayForecastSummary(51.587269, 6.027147)

data = weather_service.getFiveDayForecastSummaryByZip(__GetZipCode())

print("Date".ljust(12), "Temperature".ljust(14), "Precipitation(Rain)  Precipitation(Snow)")

for item in data:
    temp = '%0.0f' % data[item]["temp_max"] + "/" + '%0.0f' % data[item]["temp_min"]
    print(data[item]["dt_txt"].ljust(12), temp.ljust(14), ('%0.0f mm' % data[item]["precipitation"]["rain"]).ljust(20), ('%0.0f' % data[item]["precipitation"]["snow"]).ljust(14))
