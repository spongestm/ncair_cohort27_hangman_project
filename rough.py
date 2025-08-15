import random
from retrieve_word_fn import retrieve_word


def hangman():
    print("🎮 Welcome to Hangman!")

    # Get a random word (length between 4 and 14 allowed)
    word_to_guess = retrieve_word(6).lower()  # here I chose 6 letters, you can change this
    guessed_letters = []
    attempts_remaining = 6  # Number of allowed wrong guesses

    print("A random word has been chosen. Start guessing!\n")

    # Game loop
    while attempts_remaining > 0:
        # Build display word step by step (expanded version instead of list comprehension)
        display_word_list = []
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word_list.append(letter)
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

        # Validate input
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
