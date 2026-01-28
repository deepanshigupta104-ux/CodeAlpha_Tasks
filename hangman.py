import random

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time. You have 6 incorrect attempts.\n")

# List of 5 predefined words
words = ["python", "coding", "laptop", "keyboard", "developer"]
word_to_guess = random.choice(words)  # Randomly select a word
guessed_letters = []
attempts_left = 6

# Function to display current word state
def display_word():
    display = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# Game loop
while attempts_left > 0:
    print("\nWord: " + display_word())
    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print(f"Good job! '{guess}' is in the word ✅")
    else:
        attempts_left -= 1
        print(f"Oops! '{guess}' is not in the word ❌. Attempts left: {attempts_left}")

    # Check if all letters are guessed
    if all(letter in guessed_letters for letter in word_to_guess):
        print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
        break
else:
    print("\n💀 Game Over! The word was:", word_to_guess)