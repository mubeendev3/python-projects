import random


def get_user_guess(min_value: int, max_value: int) -> int:
    """
    Prompt the user to enter a valid integer guess within the given range.
    """
    while True:
        try:
            guess = int(input(f"Enter your guess ({min_value}–{max_value}): "))
            if min_value <= guess <= max_value:
                return guess
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def play_number_guessing_game(min_value: int = 1, max_value: int = 100) -> None:
    """
    Runs the number guessing game logic.
    """
    secret_number = random.randint(min_value, max_value)
    attempts = 0

    print("🎯 Welcome to the Number Guessing Game!")
    print(f"I have selected a number between {min_value} and {max_value}.")

    while True:
        guess = get_user_guess(min_value, max_value)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
            break


if __name__ == "__main__":
    play_number_guessing_game()
