import random


def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Guess the number between 1 and 100")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > secret_number:
            print("Too High")
        elif guess < secret_number:
            print("Too Low")
        else:
            print("Correct!")
            print(f"You guessed the number in {attempts} attempts.\n")
            break


while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing!")
        break
