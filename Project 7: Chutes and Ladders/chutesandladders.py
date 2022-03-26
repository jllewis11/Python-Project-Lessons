
#Draft the different functionalities of the game chutes and ladders.

#Type out the different steps in code before starting the code.
#user input space number 1-100 check if inputed space is a chute,ladder or neither.


#Example:
#1. creating the players and what position they start in
#2. roll for movement between 1-6


#For the chutes and ladders portion, use a dictionary to determine if a position is a chute or ladder. 
#key = player position
#value = if you add or subtract from the player.


#------------------------------------

#Good Start on incorporating chutes and ladders.
#One thing that is missing is the ending position of the player.

#Utilize a 2D array to get starting and ending position.

#[ [1,38], [5,16], [57,98]]

#Do the start and ending position for both chutes and ladders.


#------------------------------------
import random



spaces = {'chutes'    : [ [16,6], [48,26], [49,11], [56,53], [62,19], [64,60], [87,24], [93,73], [95,75], [98,78]],
          'ladders'   : [ [1,38], [4,14], [9,31], [21,42],[28,84], [36,44], [51,67], [71,91], [80,100]],
          #'neither'   : [2,3,5,7,8,10,12,13,15,17,18,20,22,23,25,27,29,30,32,33,34,35,37,39,40,41,43,45,46,47,50,52,56,61,68,69,70,72,77,79,92,94,96,97,99] 
         }
#value = input()
#value = int(value)

#for list_of_values in spaces:
#  for x in spaces[list_of_values]:
#    if value == x[0]:
#      print("Ending up at",x[1])


#A list starts at position 0



#Break the game down into different steps 

      
#4 player positions 
#Initialization
p = [0,0,0,0]
current = 0

while True:

  
  #Roll the dice and add to player position
  print("Currently is player", current+1)

  a = input("Press enter to roll the dice: ")

  dice = random.randint(1,6)
  print("You rolled a", dice)

  p[current] += dice 
  print("Now going to", p[current])


  #Check win condition
  if p[current] >= 100:
    print("Player", current, "is the winner!!!!!!!")
    break


  #Determine if the player hit a chute or ladder
  for list_of_values in spaces:
    for x in spaces[list_of_values]:
      if p[current] == x[0]:
        print("It is a", list_of_values)
        print("Ending up at",x[1])
        p[current] = x[1]


  #+1 to go through each player, but reset after 4
  #We need to reset the player count after 4
  if current+1 == 4:
    current = 0
  else:
    current += 1



#