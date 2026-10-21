
import random

print("Welcome to the Number Guessing Game!")

welcome = input("Enter your name: ")
print(f"Hello, {welcome}!")

numr = random.randint(1, 10)
count = 0
max_trials = 3

print("\nGuess a number between 1 and 10.")

while count < max_trials:
    num = int(input("Enter your guess: "))
    count += 1

    if num < 1 or num > 10:
        print("Please enter a number between 1 and 10.")
        continue

    if num == numr:
        print("Congratulations! You guessed correctly!")
        break
    elif num < numr:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

if count >= max_trials and num != numr:
    print("Game over! The number was", numr)
