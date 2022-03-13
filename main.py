import random
from hangman_words import word_list
from hangman_art import stages, logo


game_over = False
lives = 6

chosen_word = random.choice(word_list)
word_lenth = len(chosen_word)

print(logo)
# print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display += '_'
print(f"{' '.join(display)}")


guessed_list = []

while not game_over:
    guess = input('Guess a letter: ').lower()

    if guess in guessed_list:
        print(f'You\'ve already guessed {guess}')
    else:
        if guess in chosen_word:
            for position in range(word_lenth):
                letter = chosen_word[position]
                if guess == letter:
                    display[position] = letter
        else:
            print(
                f'You guessed {guess}, that\'s not in the word. You lose a life')
            lives -= 1

    print(f"{' '.join(display)}")
    print(stages[lives])
    guessed_list += guess

    if lives == 0:
        game_over = True
        print("You lose.")

    if "_" not in display:
        game_over = True
        print("You win.")
