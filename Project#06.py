import random

def display_menu():
    print("\nWelcome to the Number Guessing Game!")
    print("1. Start Game")
    print("2. Exit")

def start_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100. Can you guess it?")

    while True:
        guess = input("Enter your guess: ")
        attempts += 1

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-2): ")

        if choice == '1':
            start_game()
        elif choice == '2':
            print("Exiting the Number Guessing Game. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()
