"""The final Wordle Project"""
__author__ = "750675117"


white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
secret_word = "codes"
length_secret_word: int = len(secret_word)

def contains_char(secret_word, guess)-> bool: 
    """searches for same characters in guess and secret word"""
    assert len(guess) == 1
    index: int = 0
    while index < len(secret_word): 
          if guess == secret_word[index]:
               return True
          index += 1
    return False

def emojified(secret_word, guess)-> str: 
    """Translates feedback into emojis"""
    assert len(guess) == len(secret_word)
    current_index: int = 0
    results: str = ""
    while current_index < len(secret_word): 
          if guess[current_index] == secret_word[current_index]: 
               results += green_box
          elif contains_char(secret_word, guess[current_index]): 
               results += yellow_box
          else:
               results += white_box
          current_index += 1
    return results

def input_guess(length_secret_word)-> str: 
     """Ensures the length of the guess is valid"""
     guess = input(f"Enter a {length_secret_word}-character word: ")
     while len(guess) != int(length_secret_word): 
        guess = input(f"Thats wasn't {length_secret_word} chars! Try again: ")
     return guess

def main()-> None: 
     """The entrypoint of the program and main game loop."""
     turn_count: int = 1 
     win: int = 0 

     while turn_count < 7 and win < 1: 
          print(f"=== Turn {turn_count}/6 ===")
          guess: str = input_guess(len(secret_word))
          print(emojified(secret_word, guess))
          turn_count += 1
          if secret_word == guess: 
               win += 1
     if win == 1: 
          print(f"You won in {turn_count-1}/6 turns!")
     else: 
          print("X/6 - Sorry, try again tomorrow!")
               


if __name__ == "__main__": 
     main()
