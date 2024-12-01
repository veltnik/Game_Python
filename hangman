import random

def hangman():
    # Словари для разных тем с большим количеством слов
    categories = {
        "animals": ["dog", "cat", "elephant", "giraffe", "lion", "tiger", "zebra", "kangaroo", "rabbit", "dolphin"],
        "fruits": ["apple", "banana", "cherry", "grape", "orange", "kiwi", "mango", "pineapple", "strawberry", "blueberry"],
        "countries": ["canada", "brazil", "france", "japan", "india", "germany", "italy", "spain", "australia", "mexico"],
        "colors": ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white"],
        "sports": ["soccer", "basketball", "tennis", "cricket", "hockey", "baseball", "football", "golf", "swimming", "rugby"],
        "movies": ["inception", "titanic", "avatar", "gladiator", "matrix", "joker", "interstellar", "frozen", "spiderman", "batman"],
        "food": ["pizza", "sushi", "burger", "pasta", "salad", "tacos", "steak", "icecream", "chocolate", "noodles"]
    }

    # Выбор темы
    print("Choose a category or type 'random' for a random category:")
    for category in categories:
        print(f"- {category}")

    chosen_category = input("Enter the category you want to play: ").lower()
    
    if chosen_category == 'random':
        chosen_category = random.choice(list(categories.keys()))
        print(f"You have chosen the random category: {chosen_category.capitalize()}")
    elif chosen_category not in categories:
        print("Invalid category. Please restart the game.")
        return
    else:
        print(f"You have chosen the category: {chosen_category.capitalize()}")

    secret_word = random.choice(categories[chosen_category])
    guessed_letters = []
    attempts = 6
    word_completion = "_" * len(secret_word)

    print("Try to guess the word!")

    while attempts > 0 and "_" in word_completion:
        print("\nWord to guess: ", " ".join(word_completion))
        print(f"Attempts remaining: {attempts}")
        print("Guessed letters: ", " ".join(guessed_letters))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            word_completion = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word.")

    if "_" not in word_completion:
        print(f"Congratulations! You've guessed the word: {secret_word}")
    else:
        print(f"Game over! The word was: {secret_word}")

 
hangman()
