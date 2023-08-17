import weather_service
import os
import re

zipCode = re.compile(r"^\d{5}(?:[-\s]\d{4})?$")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def __GetZipCode():
    cls()
    zip = 0
    while True:
        zip = input("Please enter a valid US ZipCode (Ctrl+C to exit): ")
        if zipCode.match(zip):
            break
        else:
            input("Zip code format is not valid! Press enter to try again!")
            cls()
    
    return zip

def __printData(data):
    print("Date".ljust(12), "Temperature".ljust(14), "Precipitation(Rain)  Precipitation(Snow)")
    for item in data:
        temp = '%0.0f' % data[item]["temp_max"] + "/" + '%0.0f' % data[item]["temp_min"]
        print(data[item]["dt_txt"].ljust(12), temp.ljust(14), ('%0.0f mm' % data[item]["precipitation"]["rain"]).ljust(20), ('%0.0f' % data[item]["precipitation"]["snow"]).ljust(14))

if __name__ == "__main__":
    data = {};
    
    while True:
        try:
            data = weather_service.getFiveDayForecastSummaryByZip(__GetZipCode())
        except Exception as e:
            #TODO: write exception to a log file instead of exposing details to the user
            print('Error during retrieving forecast: ', e)

        if "isSuccess" in data:
            if data["isSuccess"]:
                __printData(data["results"])
                #break
            else:
                print('Error from the forecast service: ', data["message"])

        input("Press any key to enter a new zip code and try again...")

    
