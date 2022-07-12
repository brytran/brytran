#weather forecasting
# selenium 4
#selenium modules + automatic updating of webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import string


def weather_info(location):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  #used to make sure driver is installed correctly
    driver.get('https://weather.com/')

    success = False
    while success == False:
        try:
            searchbar_location = driver.find_element(by=By.ID, value = "LocationSearch_input")
            searchbar_location.send_keys(location)
            success = True
        except:
            continue

    success = False
    while success == False:
        try:
            searchbar_location.click()
            search_location = driver.find_element(by = By.ID, value = "LocationSearch_listbox-0")
            search_location.click()
            success = True
        except:
            if driver.current_url != 'https://weather.com/':
                break
            continue

    temp_location = driver.find_element(by = By.CLASS_NAME, value = "CurrentConditions--tempValue--3a50n")
    weather_location = driver.find_element(by = By.CLASS_NAME, value = "CurrentConditions--phraseValue--2Z18W")
    timestamp_location = driver.find_element(by = By.CLASS_NAME, value = "CurrentConditions--timestamp--23dfw")
    timestamp = timestamp_location.text
    tup = location.split(",")
    tup[0] = tup[0][0].upper() + tup[0][1:]
    tup[1] = tup[1][1].upper() + tup[1][2:]
    
    location = "{}, {}".format(tup[0], tup[1])
    timestamp = location + timestamp
    weather = weather_location.text
    temp = temp_location.text
    info = (timestamp, weather, temp)

    return info


print("Welcome to weather searcher!")
location = input("Enter your location(City, State): ")


info = weather_info(location)
print("{} is {}, {}".format(*info))



