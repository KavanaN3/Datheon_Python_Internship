
import random

# Words for the game
words = ["PYTHON", "COMPUTER", "HANGMAN", "PROGRAM", "DEVELOPER"]

# ASCII hangman stages
stages = [
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """
]


def play_hangman():
    secret_word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("=" * 40)
    print("       WELCOME TO HANGMAN GAME")
    print("=" * 40)

    while wrong_guesses < max_attempts:
        print(stages[wrong_guesses])

        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)
        print("Guessed letters:", sorted(guessed_letters))
        print("Remaining attempts:", max_attempts - wrong_guesses)

        guess = input("Guess a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again!\n")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!\n")

            if all(letter in guessed_letters for letter in secret_word):
                print("Congratulations! You won!")
                print("The word was:", secret_word)
                return
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")

    print(stages[wrong_guesses])
    print("GAME OVER! You lost.")
    print("The correct word was:", secret_word)


if __name__ == "__main__":
    play_hangman()
