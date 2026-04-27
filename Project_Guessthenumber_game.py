# We are going to write a program that generates a random number and asks the user to guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower number please”. 
# Similarly, if the user’s guess is too low, the program prints “higher number please” 
# When the user guesses the correct number, the program displays the number 
# of guesses the player used to arrive at the number.


import random
num=random.randint(1,100)
a=int(input("Guess the number:"))

a=0
Guess=1
while ( a != num):
    # a=int(input("Guess the number:"))
    if (a > num):
        print("Enter lower number")
        Guess+=1
    elif (a < num):
        print("Enter higher number")
        Guess+=1
    a=int(input("Guess the number:"))    
print(f"Congratulations You guess the number:{num} in {Guess} attempts")        