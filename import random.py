import random
def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("Welcome to the Number Guessing Game!")
    print(f"I have selected a number between 1 and 100. You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
        
        if attempts == max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
def number_guessing_game():
    while True:
        # Generate a random number between 1 and 100
        number_to_guess = random.randint(1, 100)
        attempts = 0
        max_attempts = 10
        
        print("Welcome to the Number Guessing Game!")
        print(f"I have selected a number between 1 and 100. You have {max_attempts} attempts to guess it.")
    
        while attempts < max_attempts:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1
    
                if guess < number_to_guess:
                    print("Too low!")
                elif guess > number_to_guess:
                    print("Too high!")
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
            
            if attempts == max_attempts:
                print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
        
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thank you for playing! Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    number_guessing_game()
