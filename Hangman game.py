import random

def choose_word():
    words = ["python", "hangman", "program", "computer", "keyboard", "mouse", "monitor"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while attempts_left > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts_left -= 1
            print("Incorrect guess. Attempts left:", attempts_left)
        else:
            print("Correct guess!")

        if "_" not in display_word(word, guessed_letters):
            print("\nCongratulations! You guessed the word:", word)
            break

    if attempts_left == 0:
        print("\nSorry, you ran out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
