from datetime import datetime

def get_name():
    """Get the user's name from input."""
    return input("What's your name? ").strip()

def get_time_of_day():
    """Determine the time of day based on current hour."""
    hour = datetime.now().hour
    if hour < 12:
        return "morning"
    elif hour < 17:
        return "afternoon"
    else:
        return "evening"

def greet(name):
    """Generate a personalized greeting."""
    time_of_day = get_time_of_day()
    return f"Hello, {name}! Hope you're having a great {time_of_day}!"
def show_number_sequence():
    """Demonstrate list comprehension with numbers."""
    numbers = [i for i in range(1, 6)]
    print(f"First 5 numbers: {numbers}")

def show_word_manipulation():
    """Demonstrate string manipulation."""
    words = ["hello", "world", "python"]
    capitalized = list(map(str.capitalize, words))
    print(f"Capitalized words: {capitalized}")

def play_number_game():
    """Play a simple number guessing game."""
    import random
    number = random.randint(1, 10)
    tries = 0
    max_tries = 3
    
    print("\nI'm thinking of a number between 1 and 10.")
    print(f"Can you guess it in {max_tries} tries?")
    
    while tries < max_tries:
        try:
            guess = int(input("Enter your guess: "))
            tries += 1
            
            if guess == number:
                print(f"Congratulations! You got it in {tries} tries!")
                return
            elif guess < number:
                print("Too low!")
            else:
                print("Too high!")
                
            if tries < max_tries:
                print(f"Tries left: {max_tries - tries}")
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"\nGame over! The number was {number}.")

def main():
    # Basic Hello World and greeting
    print("Hello, World!")
    name = get_name()
    greeting = greet(name)
    print(greeting)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Number sequence")
        print("2. Word manipulation")
        print("3. Play number guessing game")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            show_number_sequence()
        elif choice == "2":
            show_word_manipulation()
        elif choice == "3":
            play_number_game()
        elif choice == "4":
            print(f"\nGoodbye, {name}! Have a great {get_time_of_day()}!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
