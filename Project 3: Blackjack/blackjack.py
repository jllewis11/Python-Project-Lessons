#----- Before Coding -----
#Have the student break down Uno into different "code-able" steps


#----- Example -----

#Preparations: 
# - Deck of Cards consisting of A,2,3,4,5,6,7,8,9,10,J,Q,K
# - 2 hands for player and dealer

#Setting Up:
# - Player gets 2 cards
# - Dealer gets 2 cards with only 1 facing up


#Playing the game:
# - Player decides if he wants to hit or stay
# - Record the total value of the hand and make sure the hand is not over 21
# - Display both dealers card
# - If the dealers card is lower than 17, the dealer will automatically draw
# - Record the total value of the dealer's hand and compare to determine the winner.


#Win Conditions:
# - Whoever has the highest value wins

#Possible Repeats (Functions):
#Record the total value

#----- Coding -----
#Use the comments and create some space in between to write the actual code.



import random

def value(hand):

  total = 0
  for card in hand:
    #Face cards are 10
    if card == 'J' or card == 'Q' or card == 'K':
      total += 10
    #Ace can be 1 or 11 default 11
    elif card == 'A':
      total += 11
    else:
      total += int(card)
  #Ace = 1
  if total > 21 and 'A' in hand:
    total -= 10

  return total
    


def blackjackgame():
  print("----------Blackjack----------")
  #Preparations: 
  # - Deck of Cards consisting of A,2,3,4,5,6,7,8,9,10,J,Q,K
  deck = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']
  # - 2 hands for player and dealer
  dealer = []
  player = []
  
  
  
  #Setting Up:
  for x in range(2):
    
  # - Player gets 2 cards
    player.append(random.choice(deck))
  # - Dealer gets 2 cards with only 1 facing up
    dealer.append(random.choice(deck))
  
  #Playing the game:
  # - Player decides if he wants to hit or stay
  
  print("Dealer:", dealer[0])
  
  repeat = True
  
  while repeat:
    # - Record the total value of the hand and make sure the hand is not over 21
    print("Player:", player)
    print("Value:", value(player))
  
    if value(player) > 21:
      print("The value is over 21!")
      break
    choice = input("Enter Y/N to Draw:  ")
  
    if choice == 'N' or choice == 'n':
      repeat = False 
    elif choice == 'Y' or choice == 'y':
      player.append(random.choice(deck))
    else:
      print("Invalid Input")
  # - Display both dealers card
  
  flag = True
  while flag:
    print("Dealer:", dealer)
    print("Value:", value(dealer))
  
    if value(dealer) < 17:
      dealer.append(random.choice(deck))
    else:
      flag = False 
  # - If the dealers card is lower than 17, the dealer will automatically draw
  # - Record the total value of the dealer's hand and compare to determine the winner.
  
  
  
  #Win Conditions:
  # - Whoever has the highest value wins
  print("-----Showdown-----")
  print("Player:", player)
  print("Dealer:", dealer)
  
  
  if value(player) > 21 or value(dealer) > value(player):
    print("Player Loses!")
  elif value(dealer) > 21 or value(dealer) < value(player):
    print("Player Wins!")
