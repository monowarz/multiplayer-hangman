import random

def select_word():
    """Word Collections with hints! You can add more"""
    words_with_hints = {
        "apple": "a type of fruit",
        "python": "a programming language",
        "elephant": "a large animal with a trunk",
        "guitar": "a musical instrument",
        "ocean": "a large body of water",
        "emily": "Awesome CS Professor",
        "weis": "Best College House",
    }
    word, hint = random.choice(list(words_with_hints.items()))
    return word, hint[:15] + "..."

def display_word(word, guessed_letters):
    """Will show correct guessed words and empty blanks (as underscore)"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def display_hangman(incorrect_guesses):
    """Show players' hangman situation"""
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]
    return stages[incorrect_guesses]

def check_game_won(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def player_turn(player_num, word, guessed_letters, incorrect_guesses):
    """Take guesses (inputs), validate it, update incorrect guess number!"""
    print(f"Player {player_num}'s turn")
    print(f"The word is: {display_word(word, guessed_letters)}\n")

    guess = input("Guess a letter: ")

    if len(guess) != 1: #checking if input is valid.
        print("Please enter a single valid letter.\n")
        return incorrect_guesses

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        return incorrect_guesses

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print(f"Good guess! The word is: {display_word(word, guessed_letters)}")
    else:
        incorrect_guesses += 1
        print(f"{guess} is not in the word. Player {player_num} has {6 - incorrect_guesses} attempts remaining.")
    
    print(display_hangman(incorrect_guesses))
    
    return incorrect_guesses

def main():
    selected_word, hint = select_word()
    guessed_letters = []
    incorrect_guesses_p1 = 0
    incorrect_guesses_p2 = 0
    max_attempts = 6
    game_won = False
    current_player = 1

    print("Welcome to Multiplayer Hangman!\n\n")
    print(f"Hint: {hint}")

    for turn in range(100): # Can be used while True loop!
        if current_player == 1 and incorrect_guesses_p1 != 6:
            incorrect_guesses_p1 = player_turn(1, selected_word, guessed_letters, incorrect_guesses_p1)
            if check_game_won(selected_word, guessed_letters):
                print("Congratulations! Player 1 wins!")
                game_won = True
                break
            if incorrect_guesses_p1 == 6:
                print("Player one run out of guesses!")

        elif current_player == 2 and incorrect_guesses_p2 != 6:
            incorrect_guesses_p2 = player_turn(2, selected_word, guessed_letters, incorrect_guesses_p2)
            if check_game_won(selected_word, guessed_letters):
                print("Congratulations! Player 2 wins!")
                game_won = True
                break

            if incorrect_guesses_p2 == 6:
                print("Player two run out of guesses!") 

        # Switch players 
        if incorrect_guesses_p1 == 6 and incorrect_guesses_p2 == 6:
            break
        elif current_player == 1 and incorrect_guesses_p2 == 6:
            current_player = 1
        elif current_player == 2 and incorrect_guesses_p1 == 6:
            current_player = 1
        elif current_player == 1:
            current_player = 2
        elif current_player == 2:
            current_player = 1

    if not game_won: #draw
        print(f"The game ends with no winners! The word was: {selected_word}\n")

if __name__ == "__main__":
    main()
