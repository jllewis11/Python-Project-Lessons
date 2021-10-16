import random

#Variables needed
deal =""
player = list()
computer = list()

#Cards
deck = ["G0","G1","G2","G3","G4","G5","G6","G7","G8","G9","R0","R1","R2","R3","R4","R5","R6","R7","R8","R9","B0","B1","B2","B3","B4","B5","B6","B7","B8","B9","Y0","Y1","Y2","Y3","Y4","Y5","Y6","Y7","Y8","Y9"]




#Start:
#Split cards and give each player 5 cards 
def init():
  global deal
  number = random.randint(0,39)
  deal = deck[number]

  for x in range(0, 5):
    number = random.randint(0,39)
    player.append(deck[number])
    num = random.randint(0,39)
    computer.append(deck[num])

  return deal

#To get color  player[select][0] return color
#Hand is any player's hand
def placecard(hand):
  global deal
  while True:
    print("Current Card:  " + deal)
    print(hand)
    select =input("Postition (If no cards select none): ")
    #else change select to int()
    if select == "None" or select == "none" or select.isdigit() == False:
      num = random.randint(0,39)
      hand.append(deck[num])
      break
    else:
      select = int(select)


    if select > len(hand)-1:
      print("Out of index. Try again! ")
    elif hand[select][0] == deal[0]:

      deal = hand[select]
      hand.remove(hand[select])
      break
    elif hand[select][1] == deal[1]:

      deal = hand[select]
      hand.remove(hand[select])
      break

    else:
      print("Invalid input")
 
  return hand

#To get color  player[select][0] return color
#Hand is any player's hand
def AIplacecard(hand):
  global deal
  tempsize = len(hand)
  for a in range(0,len(hand)):
    print("Current Card:  " + deal)
    print(hand)
    select =random.randint(0,len(hand)-1)
    #else change select to int()
    
    if hand[select][0] == deal[0]:
      deal = hand[select]
      hand.remove(hand[select])
      break
    elif hand[select][1] == deal[1]:

      deal = hand[select]
      hand.remove(hand[select])
      break
    else:
      print("Finding another card!")
  if tempsize == len(hand):
    num = random.randint(0,39)
    hand.append(deck[num])
     
  return hand



def main():
  global player
  global computer
  global deal
  deal = init()
  turn = 0
  while True:
    turn += 1
    print(turn)
    player = placecard(player)
    turn +=1
    print(turn)
    computer = AIplacecard(computer)
    if len(player) == 0 or len(computer) == 0:
      break
  if len(player) == 0:
    print("Player Has Won!")
  if len(computer) == 0:
    print("Computer has won")

  

main()