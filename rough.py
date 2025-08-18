#importing relevant packages
import random
from retrieve_word_fn import retrieve_word


def hangman():#game function
    print("🎮 Welcome to Hangman!")

    # Get a random word (length between 4 and 14 allowed)
    word_to_guess = retrieve_word(6).lower()  # using the retrieve function to set the number of letters in the word
    guessed_letters = []
    attempts_remaining = 6  # Number of wrong guesses allowed

    print("A random word has been chosen. Start guessing!\n")

    # Game loop
    while attempts_remaining > 0: 
        display_word_list = [] #a list to store letters guessed correctly 
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word_list.append(letter) #If user guesses a correct letter it appends it to the list of displayed words
            else:
                display_word_list.append('_')
        display_word = ''.join(display_word_list)

        print(f"Word: {display_word}")

        # Check win condition
        if '_' not in display_word:
            print("🎉 Congratulations! You guessed the word!")
            break

        # Ask player for guess
        guess = input("Guess a letter: ").lower()

        # input checker for alphabet and multiple letters
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        # Check guess
        if guess in word_to_guess:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            attempts_remaining -= 1
            print(f"❌ Wrong guess! Attempts remaining: {attempts_remaining}")

    else:
        print(f"💀 Game Over! The word was '{word_to_guess}'.")


# Run the game
if __name__ == "__main__":
    hangman()

