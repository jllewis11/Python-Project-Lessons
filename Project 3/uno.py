#----- Before Coding -----
#Have the student break down Uno into different "code-able" steps


#----- Example -----

#Preparations: 
# - Deck of Cards consisting of colors(B,Y,R,G) and Numbers (0...9)
# - X number of hands (2 is what I have. Player vs AI)

#Setting Up:
# - Each Player needs 7 random cards
# - A play pile that holds the most recent card

#Playing the game:
# - Player chooses a card
# - Compare the chosen card to the play pile
# - The card needs to match colors or number to be playable.
# - If it is playable, remove the card from hand and replace with the play pile
# - Draw a card if not playable or no cards

#Same steps for AI but no picking using input


#Win Conditions:
# - If the hand is empty

#----- Coding -----
#Use the comments and create some space in between to write the actual code.





import random


#Preparations: 
# - Deck of Cards consisting of colors(B,Y,R,G) and Numbers (0...9)
colors = ["b","y","g","r"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]

#--- Since draw is used multiple times, we should create a function
def draw():
  #String Concatenation
  return colors[random.randint(0,3)] + numbers[random.randint(0,8)]
  
def unogame():
  # - X number of hands (2 is what I have. Player vs AI)
  hand1 = []
  hand2 = []
  
    
  #Setting Up:
  # - Each Player needs 7 random cards
  for x in range(7):
    hand1.append(draw())
    hand2.append(draw())
  # - A play pile that holds the most recent card
  play = draw()
  
  
  flag = True
  while flag:
    #Win Conditions:
    # - If the hand is empty
    if hand1 == []:
      print("Player has won!")
      break
    if hand2 == []:
      print("The AI has won!")
      break
    #Playing the game:
    # - Player chooses a card
    #pos = position
    print(" ----- Play Pile -----")
    print("Play: ", play)
    print(" ----- Player -----")
    print("Player:", hand1)
    pos = input("Enter the Position(Press Enter to draw): ")
  
    try:
      #Try: pos = int(pos)
      pos = int(pos)
      # - Compare the chosen card to the play pile
      # - The card needs to match colors or number to be playable.
      if play[0] == hand1[pos][0]:
        #replace with the play pile
        play = hand1[pos]
        hand1.remove(hand1[pos])
      elif play[1] == hand1[pos][1]:
        play = hand1[pos]
        hand1.remove(hand1[pos])
      else:
      # - If it is playable, remove the card from hand and replace with the play pile
      # - Draw a card if not playable or no cards
        hand1.append(draw())
  
    except:
      #If the player entered anything else, we will just make them draw a card.
      hand1.append(draw())
    #Same steps for AI but no picking using input
  
  
    print(" ----- AI -----")
    print("AI has", len(hand2), "cards.")
    # ----- AI -----
    #Make sure when you copy the code, to replace all hand1 with hand2
    canDraw = True
    for pos in range(len(hand2)-1):
      print(hand2)
      print("POS", pos)
      # - Compare the chosen card to the play pile
      # - The card needs to match colors or number to be playable.
      if play[0] == hand2[pos][0]:
        #replace with the play pile
        canDraw = False
        play = hand2[pos]
        hand2.remove(hand2[pos])
        break
      elif play[1] == hand2[pos][1]:
        canDraw = False
        play = hand2[pos]
        hand2.remove(hand2[pos])
        break
    if canDraw:
      hand2.append(draw())



