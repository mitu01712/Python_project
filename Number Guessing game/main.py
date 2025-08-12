import random

def user_guess():
    number = random.randint(1, 100)
    guess = None

    while guess != number:
        user_input = input("Guess the number (1-100): ")
        try:
            guess = int(user_input)
        except ValueError:
            print("Please enter a number, it must be a number!")
            continue

        if guess < number:
            print("Too Low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! The number was {number}.")


def computer_guess():
    low = 1
    high = 100
    feedback = ""

    while feedback != "C":
        guess = (low + high) // 2
        print(f"Computer guesses: {guess}")
        feedback = input("H = Too Hight, L = Too Low, C = Correct: ").upper().strip()

        if feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1
        
    print("Computer guessed your number!")

def main():
    while True:
        print("\n Choose an option:")
        print("1. You guess the number")
        print("2. computer guesses your number")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            user_guess()
        elif choice == "2":
            computer_guess()
        elif choice == "3":
            print("Goodlick!")
            break
        else:
            print("Invalid choice! Please enter 1, 3, or 3.")
if __name__ =="__main__":
    main()


