# Task 4: Closure Practice
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        display = ''
        all_guessed = True

        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += '_'
                all_guessed = False

        print(display)
        return all_guessed
    return hangman_closure

if __name__ == '__main__':
    secret_word = input("Enter the secret word: ").lower()
    game = make_hangman(secret_word)

    print("\nWelcome to Hangman!")

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            # Invalid input check breakdown v
            # len(guess) != 1 checks if the input is a single character
            # not guess.isalpha() checks if the input is a letter
            # continue - skips the rest of the loop and prompts for input again
            print("Please enter a single letter.")
            continue

        complete = game(guess)
        if complete:
            print("\nCongratulations! You've guessed the word:", secret_word)
            break
        else:
            print("Keep guessing!")