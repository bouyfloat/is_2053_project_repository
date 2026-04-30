# import randint to generate random integers for creating the ships
from random import randint

# -----------------------------
# BOARD SETUP
# List comprehension used for this to create an 8x8 board
# -----------------------------

def new_board():
    return [[" "] * 8 for _ in range(8)]


# -----------------------------
# BOARD DISPLAY
# Using a for loop
# -----------------------------

def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


letters_to_numbers = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3,
    'E': 4, 'F': 5, 'G': 6, 'H': 7
}


# -----------------------------
# SHIP PLACEMENT
# Randomly assign ship placements on the board
# -----------------------------

def create_ships(board):
    for _ in range(8):
        ship_row, ship_column = randint(0, 7), randint(0, 7)

        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 7), randint(0, 7)

        board[ship_row][ship_column] = "X"


# -----------------------------
# USER INPUT
# Ask user for input on row and column to check if ship is hit
# -----------------------------

def get_ship_location():
    row = input("Enter the row of the ship (1-8): ").strip()

    while row not in [str(i) for i in range(1, 9)]:
        print("Not a valid row. Please enter a number 1-8.")
        row = input("Enter the row of the ship (1-8): ").strip()

    column = input("Enter the column of the ship (A-H): ").strip().upper()

    while column not in "ABCDEFGH":
        print("Not a valid column. Please enter a letter A-H.")
        column = input("Enter the column of the ship (A-H): ").strip().upper()

    print()
    return int(row) - 1, letters_to_numbers[column]


# -----------------------------
# MAIN GAME
# Main game setup and rules
# -----------------------------

def main():
    hidden_board = new_board()
    guess_board = new_board()

    print("Welcome to Battleship!")
    print("----------------------")
    print("The computer has placed 8 hidden ships.")
    print("Your goal is to find them in 10 turns.\n")

    create_ships(hidden_board)

    turns = 10
    hits = 0

    while turns > 0:
        print("Guess a battleship location!")
        print_board(guess_board)

        row, column = get_ship_location()

        if guess_board[row][column] == "-":
            print("You already guessed that location. Try again.\n")
            continue

        if hidden_board[row][column] == "X":
            print("Nice! You hit an enemy ship!")
            guess_board[row][column] = "X"
            hits += 1
        else:
            print("Miss!")
            guess_board[row][column] = "-"

        turns -= 1

        if hits == 8:
            print("You win! You sank all the ships!")
            print(f"You hit {hits} out of 8 ships.")
            break

        print(f"You have {turns} turns left.\n")

    if turns == 0:
        print("Game over! You ran out of turns.")
        print(f"You hit {hits} out of 8 ships.")


# -----------------------------
# REPLAY FUNCTION 
# Allow users to keep playing if they'd like
# -----------------------------

def play_game():
    while True:
        main()

        again = input("\nDo you want to play again? (y/n): ").strip().lower()

        while again not in ["y", "n"]:
            again = input("Please enter 'y' or 'n': ").strip().lower()

        if again == "n":
            print("Thanks for playing Battleship!")
            break


# -----------------------------
# ENTRY POINT
# -----------------------------

if __name__ == "__main__":
    play_game()
