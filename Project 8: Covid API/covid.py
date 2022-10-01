#Credits to student Lucy P. for contributing to this project and code

import requests

data = requests.get("https://covid-api.mmediagroup.fr/v1/cases")

d = data.json()

def percapita(infected, total):

  #p = proportion

  p = infected / total 
  p = round(p, 5)
  #Get percent first 
  print("Population: ", total)
  print("Percentage: ", round(p * 100, 4), '%')

  #Per capita 
  answer = p * 100000


  print("Per Capita (100,000)", answer , "people has COVID.")



#Ask for an input 
print("Enter a place")
country = input("What country are you looking for?")
#Capitalize the first letter of the country from input 


#Captialize only does first letter in string
#Title capitalizes each first letter in words in a string 
country = country.title()
print (country)
if country == "United States":
  country = "US"

if country == "South Korea":
  country = "Korea, South"
#Same thing for South Korea


print(country)
for x in d:
#Compare the input with x (which is list of countries )
  if country == x:

    print("Confirmed cases", x, ":",d.get(x).get("All").get("confirmed"))

    percapita(d.get(x).get("All").get("confirmed"),d.get(x).get("All").get("population"))




#Get the percentage of confirmed cases with the population.
#confirmed cases
#population
#A fraction of total amount to determine 
#proportion = from fraction to decimal 
#percentage = from decimal(proportions) * 100 


#percentage  = confirmed / population * 100 
 
#*****per capita******

#Percentage by per capita 



#before, it would be unequal to compare because
#i.e india vs us: india has more in pop than us.
#To equal the playing field, get rid of population and turn it into per capita 

#per capita would be per 100,000 people in a country



#example 34.1M India v 150K Australia

#Per capita percentage * x amount of people compared 

# Australia 150,000/ 25,700,000 = 0.584% = 
#0.00584 * per 100,000 people = 584
# India 34,100 / 1,380,000 = 2.471%
# 0.0247 * per 100,000 people = 2471

#proportion = decimal number of a ratio/fraction\




