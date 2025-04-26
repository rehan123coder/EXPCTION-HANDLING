import random
playing=True
print("i will generate a number from 10,20 you have to guess it")
print("if you get it right you win the game and become a master")
number=random.randint(10,20)
while playing :
    guessnumber=int(input("please enter a number"))
    if guessnumber==number:
        print("you win the game")
        break
    else:
      print("your guess is wrong try again")
