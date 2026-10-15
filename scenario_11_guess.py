SECRET_NUMBER = 42
MAX_ATTEMPTS = 7

player_name = input("Enter player name: ")
attempts = 0
won = False

print(f"Welcome {player_name}! Guess the secret number between 1 and 100. You have {MAX_ATTEMPTS} attempts.")

while attempts < MAX_ATTEMPTS:
    guess = int(input(f"Attempt {attempts + 1}/{MAX_ATTEMPTS}: Enter your guess: "))

    if guess < 1 or guess > 100:
        print("Out of range! Guess must be between 1 and 100. This attempt does not count.")
        continue

    attempts += 1

    if guess == SECRET_NUMBER:
        print(f"Congratulations {player_name}! You guessed the secret number in {attempts} attempt(s)!")
        won = True
        break
    elif guess < SECRET_NUMBER:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

if not won:
    print(f"\nGame Over, {player_name}! You've exhausted all {MAX_ATTEMPTS} attempts.")
    print(f"The secret number was: {SECRET_NUMBER}")