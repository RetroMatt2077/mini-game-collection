"""
Hangman Deluxe
Author: Retro Matt / ChatGPT
"""

import random

WORDS = [
    "python", "dragon", "wizard", "castle", "adventure",
    "treasure", "knight", "dungeon", "phoenix", "galaxy",
    "retro", "fantasy", "monster", "magic", "computer"
]

HANGMAN = [
"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
"""
]

def play():
    word = random.choice(WORDS)
    guessed = set()
    wrong = 0

    while wrong < 6:
        print(HANGMAN[wrong])
        display = " ".join(c if c in guessed else "_" for c in word)
        print("Word:", display)
        print("Guessed:", " ".join(sorted(guessed)))

        if all(c in guessed for c in word):
            print("\n🎉 You guessed the word!")
            return True

        guess = input("\nGuess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter one letter.")
            continue

        if guess in guessed:
            print("Already guessed.")
            continue

        guessed.add(guess)

        if guess not in word:
            wrong += 1
            print("❌ Wrong!")

    print(HANGMAN[6])
    print(f"You lost! The word was: {word}")
    return False


wins = 0
losses = 0

print("="*40)
print("      HANGMAN DELUXE")
print("="*40)

while True:
    if play():
        wins += 1
    else:
        losses += 1

    print(f"\nScore: {wins} Wins | {losses} Losses")

    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        break

print("\nThanks for playing Hangman Deluxe!")
