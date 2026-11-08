# Task 1: Hangman Word Guessing Game

## Project Description
This project is a simple console-based Hangman Word Guessing Game developed using Python. The player must guess a hidden word by entering one letter at a time.

The player gets a maximum of 6 incorrect attempts to guess the word correctly.

## Features
- Random word selection.
- Maximum of 6 incorrect attempts.
- Displays guessed letters.
- Prevents duplicate guesses from reducing attempts.
- Validates user input.
- Displays a winning or losing message.

## Technologies Used
- Python 3
- Random module

## Installation
1. Install Python 3 on your computer.
2. Download or clone this project.
3. Open the project folder in VS Code.

## How to Run
Open the terminal in the project folder and execute:

```bash
python hangman.py
```

Follow the instructions and enter one alphabet letter at a time.

## Project Structure

```text
task1_hangman/
│
├── hangman.py
├── task1_output
└── README.md
```

## How the Game Works
1. The program selects a random word.
2. The player guesses one letter at a time.
3. Correct guesses reveal the matching letters.
4. Incorrect guesses reduce the remaining attempts.
5. The game ends when the player guesses the word or uses all 6 incorrect attempts.

## Output
The `task1_output` file shows the game execution and winning output.

## Author
Developed as part of the Datheon Python Programming Internship.