#Concepts to know
# - Data Types
# - Variables
# - Conditional Statements
# - While Loops


import random

number = random.randint (1,100)

while True:
  num = input('enter a number: ')
  num = int(num)

  if number == num:
    print ('Congratulations!')
    break
  if number > num:
    print ('Wrong :(! Number is to low...')
  if number < num:
    print('Number is to high...')