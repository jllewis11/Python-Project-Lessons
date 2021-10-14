
#Hangman
import random

#Make a list of words to choose
#Pick a random word from the list.
#Determine the size of the word. 
#and display size using " - " to show subs.

#Game part  
# Guess a letter
# Check if letter is in word


#If letter is in the word 
#  loop to find when guess matches letter 
#   Save position and replace it  

#else 
#  print("It is not in there ")


#Example:
#word = "hello"

# - - - - -
#Guess a letter: e     


key = ["hello", "candy", "tree", "unique", "pencil", "plant", "keyboard", "bike", "chair", "bear", "absolute", "abstract", "accident", "satisfied", "criminal", "database", "humanity", "lifetime", "magazine"]

number = random.randint(0,len(key)-1)
word = key[number]

#Guess is storing our current guesses
guess = list()
#Hidden is storing the word in list format  
hidden = list()

#len(word)

#hidden.append(word[x])

for x in range( len(word)):
  guess.append("-")
  hidden.append(word[x])

tries = 10

#tries -= 1

while tries > 0:
  if guess == hidden:
    break
  
  print(guess)
  letter = input("Guess a letter: ")
  
  if letter in hidden:
    for x in range( len(word)):
      if letter == hidden[x]:
        guess[x] = letter   
  else:
    print("try again")
    tries -= 1



  print("Tries left: " + str(tries))
  
 
if tries < 1:
  print("You've ran out of tries")
else:
  print("You got the word ")