import random

# Generate a random number between 1 and 10
numberguess = random.randint(1, 10)
attempts = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10. You have 5 attempts to guess it.")

for attempt in range(attempts):
    guess = int(input(f"Attempt {attempt + 1}: Enter your guess: "))

    if guess == numberguess:
        print("Congratulations! You guessed the number!")
        break
    else:
        print("Wrong guess. Try again.")

if guess != numberguess:
    print(f"Sorry no more attempts, the correct number was {numberguess}.")