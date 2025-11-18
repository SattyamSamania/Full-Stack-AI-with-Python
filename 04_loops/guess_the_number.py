import random

print("Number Guessing Game!")
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    print(f"\nAttempt {attempts + 1} of {max_attempts}")
    
    guess = input("Enter your guess (between 1 and 100), or type 'quit' to exit: ")
    
    if guess.lower() == 'quit':
        print("You quit the game.")
        break
    
    # Input validation
    if not guess.isdigit() or not (1 <= int(guess) <= 100):
        print("Invalid input. Please enter a number between 1 and 100.")
        continue
    
    guess = int(guess)
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")    
    else:
        print(f" Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break

else:
    # This runs only if the loop did NOT break
    print(f"\n Sorry, you've used all your attempts. The number was {secret_number}.")

print("\nThank you for playing! Goodbye.")
