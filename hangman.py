# Hangman Game (Simple)
# Predefined 5 words, max 6 incorrect guesses.
# Run: python hangman.py

import random

WORDS = ["python", "apple", "hangman", "program", "developer"]

def play_hangman():
    word = random.choice(WORDS)
    guessed = set()
    wrong = set()
    max_wrong = 6

    while True:
        display = ''.join([c if c in guessed else '_' for c in word])
        print("\\nWord:", ' '.join(display))
        if display == word:
            print("Congratulations! You guessed the word:", word)
            break
        print(f"Wrong guesses ({len(wrong)}/{max_wrong}):", ', '.join(sorted(wrong)))
        guess = input("Enter a letter (or type 'quit' to exit): ").lower().strip()
        if guess == 'quit':
            print("Game exited. The word was:", word)
            break
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue
        if guess in guessed or guess in wrong:
            print("You already tried that letter.")
            continue
        if guess in word:
            guessed.add(guess)
            print("Good guess!")
        else:
            wrong.add(guess)
            print("Wrong guess!")
        if len(wrong) >= max_wrong:
            print("Sorry, you've reached the maximum wrong guesses.")
            print("The word was:", word)
            break

if __name__ == "__main__":
    print("=== Welcome to Hangman ===")
    play_hangman()
