# We are going to write a program that generates a random number and asks the user to guess it
# If the player's guess is higher than the actual number, the program displays "Lower number please"
# If the player's guess is lower than the actual number, the program displays "Higher number please"
# When the user guesses the number, the program displays the number of guesses the player used to arrive at the number
import random
n = random.randint(1, 100)
a = -1
guesses = 0
while(a != n):
    guesses += 1
    a = int(input("Guess a number :"))
    if (a < n):
        print("Higher number please")
    else:
        print("Lower number please")
print(f"Congratulations! You guessed the number {n} in {guesses} guesses")