# Multiplayer Hangman Game 🎮🐍

## Overview
This project is a Multiplayer Hangman game developed in Python. The game allows two players to take turns guessing letters to uncover a hidden word. Each player has a maximum of six incorrect guesses, with hints provided to guide them. Incorrect guesses are visually represented by different stages of a hangman figure. The objective is for a player to correctly guess the word before running out of attempts.

## Key Features
- **Multiplayer Mode**: Two players alternate turns guessing letters.
- **Hint System**: Hints are provided using a dictionary to assist with guesses.
- **Visual Feedback**: Incorrect guesses are displayed by stages of a hangman figure.

## Gameplay Instructions
1. Players take turns guessing one lowercase letter at a time. Multiple letters or capital letters are not accepted.
2. If a letter appears multiple times in the word, guessing it once will reveal all instances.
3. Each player has up to 6 incorrect guesses.
4. If one player runs out of attempts, the other player continues until they either win or also run out of attempts.
5. **Winning Terms**: The first player to guess the word correctly wins. If both players run out of guesses without solving the word, it’s a draw.

## How to Download and Use
1. **Download**: Clone this repository by running:
   ```
   git clone <repository-url>
   ```
2. **Run the Game**: Open a terminal, navigate to the project directory, and run the script with:
   ```
   python main.py
   ```

## Sample Game
**Player 1's Turn**  
*The word is: p y _ _ _ n*  
Guess a letter: r  
*r is not in the word. Player 1 has 0 attempts remaining.*

```plaintext
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
```

Player 1 runs out of guesses!

**Player 2's Turn**  
*The word is: p y t _ _ n*  
Guess a letter: o  
*Good guess! The word is: p y t h o n*

Congratulations! **Player 2 wins!**

--- 
