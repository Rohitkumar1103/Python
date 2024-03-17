import random

from hangman_art import logo
from hangman_words import word_list
from hangman_art import stages


end_of_game = False
lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)

print(chosen_word)

display = []
for _ in range(word_length):
  display += "_"
print(display)



while not end_of_game:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print(f"You've already guessed {guess}")

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  print(display)

  if guess not in chosen_word:
    print(f"You've guessed {guess}, that's not in the word. You loose a life.")
    lives -=1
    if lives == 0:
      end_of_game = True
      print("You Lose")

  if "_" not in display:
    end_of_game = True
    print("Congratulations, you won!")

  print(stages[lives])
