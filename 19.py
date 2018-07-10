#19. Play a number guessing game (User enters a guess, you print YES or Higher or Lower)
import random
endingnum=input("enter the last number:")
n=random.randint(1,endingnum+1)
print(n)
guess=input("enter the number between 1 and {0}:".format(endingnum))
print(guess)
if(guess==n):
    print("your guessed it")
elif(guess<n):
    print("your guess is low")
else:
    print("your guess id high")
