import requests
import json

def getWeather(zipcode):
    apiKey = "4214c34c82645531c0fd5b3064b92b72"
    #request data by zip code
    url = "http://api.openweathermap.org/data/2.5/weather?zip="+zipcode+"&appid="+apiKey

    response = requests.get(url)
    data=response.json()

    #parameters that affect bass: ,temp,weather condition,pressure,windspeed
    temp = round(((float(data['main']['temp'])-273.15) *(9/5)+32),2)
    windSpeed = round(float(data['wind']['speed']) * 2.23694,2)
    condition = data['weather'][0]['description']
    baroPressure = float(data['main']['pressure'])
    print(url)
    return [temp,windSpeed,condition,baroPressure]

def fish_forecast(zipcode):
    rating = 10
    weatherData = getWeather(zipcode)
    temp = weatherData[0]
    windSpeed = weatherData[1] 
    condition = weatherData[2]
    baroPressure = float(weatherData[3])

    if(temp<=70 or temp>=85):
        rating-=3
    
    if(windSpeed<= 4 or windSpeed>=12):
        rating -=2
    
    if(("storm" in condition) or ("rain" in condition)):
        rating-=8
    if(rating<0):
        rating=0
    
    return rating
    










