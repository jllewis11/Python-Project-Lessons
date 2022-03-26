import turtle


def Size_(t, size): # is going to be a 100 
 # penup pendown, and goto
  t.penup()
  t.goto(-size/2, -size*1.5)  # x -> -50 , y -> -150
  # _|_|_ 
  # _|_|_ 
  #  | |
  t.pendown()
  t.goto(-size/2, size*1.5) # x -> -50, y -> 150
  t.penup()
  t.goto(size/3, size*1.5) 
  t.pendown()
  t.goto(size/3, -size*1.5)
  t.penup()
  t.goto(-size/1,size/2)
  t.pendown()
  t.goto(size*.9, size/2)
  t.penup()
  t.goto(-size/1, -size/2)
  t.pendown()
  t.goto(size*.9, -size/2) # x -> 90 , -50


def xo(t,size,c,car): #
  x=[-size,0,size,-size,0,size,-size,0,size]
  y=[size,size,size,0,0,0,-size,-size,-size]
  xc=x[c] # We put c in the brackets
  yc=y[c]
  t.penup() 
  t.goto(xc,yc)
  t.write(car,False,"center","40pt") # Text based 
def Win(assign,v):
  Win=[0,1,2, 2,5,8, 0,4,8, 0,3,6, 2,4,6, 3,4,5, 6,7,8, 1,4,7]
  for i in range(8):
    list_=[] 
    for J in range(3):
      list_.append(assign[Win[(i*3)+J]])#i=number of combinations grouped in 3 J = var in each combination
    if list_ == [v,v,v]:
      return True
    #else:
    #   return False
  return False
  
t = turtle.Turtle() # this is t
t.speed(5)
Size = 100 # Size
Size_(t, Size)
char=["X","O"]
assign = [0,0,0,0,0,0,0,0,0]
sal = str()
for i in range(9):
  v = char[i%2]
  #inn is now the nvalue of whatever the user inputs

  while True:
    sal = input("Input int for your cell")
    numlist = ["1","2","3","4","5","6","7","8","9"]
    
    if sal in numlist:
      sal = int(sal)-1
      if assign[sal] == 0: 
        break
      else:
        print("Cell is already taken sorry")
    else:
      print("Please enter an int between 1 and 9")


  # sal is the vsalue of whatever cell the user inputs 
  #if sal < 0 or sal > 8:#if value is under 1 or over 9
    #continue#escape loop
  # not taken so fill in 
  assign[sal] = v #Put the X or O in that spot  
  xo(t,Size,sal,v) # calling the function
  if Win(assign,v):
    print (v + " is the winner")
    break

if not Win(assign,v):
  print ("DRAW")