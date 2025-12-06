#Day 3-Number guessing game
import random

print("Welcome to the number guessing game!")
print("I'm thinking number between 1 and 10")

secret_number = random.randint(1,10)
guess = int(input("Enter number:"))

if guess == secret_number:
    print("correct!you guessed the number")
elif guess > secret_number:
    print("too high!try small number")
else:
    print("too small!try large number")
    print("secret number was:",secret_number)