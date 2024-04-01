import random
import math
#Taking inputs
lower=int(input("Enter Lower bound:-"))
upper=int(input("Enter Upper bound:-"))
#generating the random number between the lower and upper
x=random.randint(lower,upper)
print("\n\tyo've only",round(math.log(upper-lower+1,2)),"chances to guess the integer\n")
#initialize the number of guesses 
count=0
#for calculating the minimum number of guesses depends upon range
while count < math.log(upper-lower+1,2):
    count+=1
#taking guessing number as input
    guess=int(input("Guess a number:- "))
#condition testing
    if x == guess:
        print("Congratulations you did it in",count,"try")
#once guessed loop will break
        break
    elif x > guess:
        print("You guessed too Low!")
    elif x < guess:
        print("You guessed too high!")
    if count >= math.log(upper-lower+1,2):
        print("\n The number is %d" %x)
        print("\tBetter Luck Next Time!")