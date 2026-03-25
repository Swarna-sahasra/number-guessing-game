import random
from colorama import Fore, Style, init

init(autoreset=True)

def choose_difficulty():
    print(Fore.CYAN + "\nChoose Difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        return 50, 10
    elif choice == "2":
        return 100, 7
    elif choice == "3":
        return 200, 5
    else:
        print(Fore.RED + "Invalid choice! Defaulting to Medium.")
        return 100, 7


def play_game():
    max_range, max_attempts = choose_difficulty()
    number = random.randint(1, max_range)
    attempts = 0

    print(Fore.YELLOW + f"\nGuess a number between 1 and {max_range}")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print(Fore.BLUE + "Too low!")
            elif guess > number:
                print(Fore.MAGENTA + "Too high!")
            else:
                score = (max_attempts - attempts + 1) * 10
                print(Fore.GREEN + f"\n🎉 Correct! You guessed it in {attempts} attempts.")
                print(Fore.GREEN + f"🏆 Your score: {score}")
                return

        except ValueError:
            print(Fore.RED + "Please enter a valid number!")

    print(Fore.RED + f"\n❌ Game Over! The number was {number}")


def main():
    print(Fore.GREEN + "🎮 Welcome to Advanced Number Guessing Game!")

    while True:
        play_game()
        replay = input(Fore.CYAN + "\nDo you want to play again? (y/n): ").lower()
        if replay != 'y':
            print(Fore.YELLOW + "Thanks for playing! 👋")
            break


if __name__ == "__main__":
    main()