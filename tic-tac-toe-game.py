"""
Tic-Tac-Toe Deluxe
Author: Retro Matt / ChatGPT
"""

import random

board = [" "] * 9
player_score = 0
computer_score = 0
ties = 0


def draw():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---+---+---")
    print()


def winner(mark):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(board[a]==board[b]==board[c]==mark for a,b,c in wins)


def full():
    return " " not in board


def reset():
    global board
    board = [" "] * 9


print("="*35)
print(" TIC-TAC-TOE DELUXE ")
print("="*35)

while True:
    reset()

    while True:
        draw()

        try:
            move = int(input("Choose a square (1-9): ")) - 1
        except ValueError:
            print("Enter a number.")
            continue

        if move not in range(9) or board[move] != " ":
            print("Invalid move.")
            continue

        board[move] = "X"

        if winner("X"):
            draw()
            print("🎉 You win!")
            player_score += 1
            break

        if full():
            draw()
            print("It's a tie!")
            ties += 1
            break

        while True:
            cpu = random.randint(0,8)
            if board[cpu] == " ":
                board[cpu] = "O"
                break

        if winner("O"):
            draw()
            print("Computer wins!")
            computer_score += 1
            break

        if full():
            draw()
            print("It's a tie!")
            ties += 1
            break

    print(f"\nScore")
    print(f"You      : {player_score}")
    print(f"Computer : {computer_score}")
    print(f"Ties     : {ties}")

    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        break

print("\nThanks for playing Tic-Tac-Toe Deluxe!")
