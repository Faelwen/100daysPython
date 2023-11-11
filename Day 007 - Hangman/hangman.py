import random

from wordlist import word_list
from art import *

print(logo)

chosen_word = random.choice(word_list)
word_len = len(chosen_word)

game_ongoing = True
lives = 6
display = []
for _ in range(word_len):
    display += "_"

while game_ongoing:
    player_guess = input("Guess a letter: ").lower()
    if player_guess in display:
        print(f"You've already guessed {player_guess}") 

    for position in range(word_len):
        letter = chosen_word[position]
        if letter==player_guess:
            display[position] = letter

    if player_guess not in chosen_word:
        print(f"The letter {player_guess} is not in the word. You lose a life.")
        lives -= 1

        if lives ==0:
            game_ongoing = False
            print("You lose")
        
    print(f"{' '.join(display)}")

    if "_" not in display:
        game_ongoing = False
        print("You win!")

    print(stages[lives])