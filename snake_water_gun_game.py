#-------------------SNAKE-WATER-GUN-GAME------------------------------------------
import random
print("             !Welcome to SNAKE-WATER-GUN-GAME!")
print("\nHOW TO PLAY:")
print(""""You have to select any one thing from(snake,water,gun) 
and then computer will select any one from it.Now if you select snake
and computer select water then its mean snake drinks all the water and
you get 1 point and you select snake and computer select gun then
computer will get 1 point because gun gonna kill the snake.""")
swg=["SNAKE","WATER","GUN"]


your_point = 0
computer_point = 0
i=0
def game():
 global i
 global your_point
 global computer_point
 while(i<10):
  try:
   com = random.choice(swg)
   i=i+1
   print("\nSelect: 1.Snake 2.Water 3.Gun")
   player=int(input("Enter number:"))
   if player==1:
    if player==1 and com=="SNAKE":
        print("YOU BOTH ARE SAME\n")
    elif player==1 and com=="WATER":
        print("WOAH! YOU DRINK ALL THE WATER")
        your_point+=1
    elif player==1 and com=="GUN":
        print("OH!YOU GET KILLED BY GUN")
        computer_point+=1

   if player==2:
    if player==2 and com=="SNAKE":
        print("OH!YOU GET DRINK BY SNAKE\n")
        computer_point+=1
    elif player==2 and com=="WATER":
        print("YOU BOTH ARE SAME\n")
    elif player==2 and com=="GUN":
        print("WOAH!YOU SUBMERGED THE GUN")
        your_point+=1

   if player==3:
    if player==3 and com=="SNAKE":
        print("WOAH! YOU KILLED THE SNAKE\n")
        your_point +=1
    elif player==3 and com=="WATER":
        print("OH! YOU SUBMERGED INTO WATER\n")
        computer_point+=1
    elif player==3 and com=="GUN":
        print("YOU BOTH ARE SAME")
   elif player>3 or player<1 and (com=="SNAKE" or com=="GUN" or com=="WATER"):
       print("             !-----PLEASE SELECT A VALID NUMBER-----!")
       i-=1

  except Exception as a:
    print(a,"is not a number please select a number")
    i-=1
game()
print("____YOUR SCORE:",your_point)
print("COMPUTER SCORE:",computer_point)
if your_point>computer_point:
            print("!---VICTORY---!")
elif your_point<computer_point:
            print("!---DEFEAT---!")
elif your_point==computer_point:
            print("!----DRAW----!")

for i in range(0,50):
  try:
    print("\nWANNA PLAY AGAIN?\n1.YES\n2.NO")
    pa=int(input("Enter number:"))
    if pa==1:
      i=0
      your_point=0
      computer_point=0
      game()
    elif pa==2:
        print("Thanks for playing.")
        break
    else:
        print("PLEASE SELECT A VALID NUMBER")
        continue
    print("____YOUR SCORE:", your_point)
    print("COMPUTER SCORE:", computer_point)
    if your_point > computer_point:
        print("!---VICTORY---!")
    elif your_point < computer_point:
        print("!---DEFEAT---!")
    elif your_point == computer_point:
        print("!----DRAW----!")

  except Exception as abc:
     print(abc,"is not a number please select a number.")
