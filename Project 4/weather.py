import requests

#get a user input of city and country/state
city=input("What City?")
country=input("What state/country?")



#Gets the lat and long (x and y) of a location.
location = requests.get(
    "http://open.mapquestapi.com/geocoding/v1/address?key=K3jfFwVX8fsBxNQGcyrHwAi0hxQxiCX1&location="+ city + "," + country
)


info = location.json()

#Extract information that gives me lat and long
lat = info.get('results')[0].get('locations')[0].get('latLng').get('lat')
long = info.get('results')[0].get('locations')[0].get('latLng').get('lng')



#After getting lat and long, we insert that into the weather API
weather = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=" +
                       str(lat) + "&lon=" + str(long) +
                       "&appid=38de2f98cf6e68962cc0fba3018c5311")
data = weather.json()





for x in range(7):
  #Converting Kelvin to F.
  temp = (((data.get('daily')[x].get('temp').get('day'))-273.16)*9/5)+32

  #des could be cloudy, rain, snow, windy
  des = data.get('daily')[x].get('weather')[0].get('description')
  
  temp=round(temp,1)
  print (temp)

  if temp > 90 and temp < 100:
    print("It is very hot outside!")
  if temp > 100:
    print("Oh no! You are going to get very hot!")
  if temp < 30:
    print("There is snow outside of your window!")
  if temp > 40 and temp < 50:
    print("Almost mild!")
  if temp > 50 and temp < 80:
    print("Warm!")
  if temp < 0:
    print("WAIT HOW ARE YOU SURVIVING?!?!")