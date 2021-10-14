#Hangman
import random


key = ["hello", "candy", "tree", "unique", "pencil", "plant", "keyboard", "bike", "chair", "bear", "absolute", "abstract", "accident", "satisfied", "criminal", "database", "humanity", "lifetime", "magazine", "multipule", "violence"]


#-------------------NEW------------------

#File open read 

#Note: Check file location of words.txt
f = open("Hangman/words.txt","r")

for x in f:
  x = x[:-1]
  key.append(x)
f.close()

#-----------------------------------------

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