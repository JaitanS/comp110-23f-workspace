"""Step 2 to Wordle!"""
__author__ = "730675117"

# Variables
secret_word: str = ("python")
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"


# Collecting user word
guess = input(f"What is your {len(secret_word)}-letter guess? ")


# Check length
while len(guess) != len(secret_word):
    guess = input(f"Thats was not {len(secret_word)} letters! Try again: ")

# Give feedback on guess
current_index: int = 0
results: str = ""
while current_index < len(secret_word):
    guess_anywhere: int = 0
    yellow_guess: int = 0
    if guess[current_index] == secret_word[current_index]:
        results += green_box
    else:
        while yellow_guess < 1 and guess_anywhere < len(secret_word): 
            if guess[current_index] == secret_word[guess_anywhere]: 
                results += yellow_box
                yellow_guess += 1 
            else: 
                guess_anywhere += 1
        if yellow_guess < 1: 
            results += white_box
    current_index += 1

print(results)

# Final verdict on guess
if guess == secret_word:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")