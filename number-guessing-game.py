import random

print("🔢 NUMBER GUESSING GAME")
print("I'm thinking of a number between 1 and 100...\n")

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Enter your guess (or Q to quit): ")

    if guess.lower() == "q":
        print("Game ended.")
        break

    if not guess.isdigit():
        print("Enter a valid number!")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret:
        print("📉 Higher!\n")
    elif guess > secret:
        print("📈 Lower!\n")
    else:
        print(f"🎉 Correct! You got it in {attempts} tries!\n")
        break
