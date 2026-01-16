import random
words = ["apple", "banana", "orange", "grape", "mango"]
word_to_guess = random.choice(words)


guessed_letters = []   
incorrect_guesses = 0 
max_incorrect = 6     

display_word = ["_" for _ in word_to_guess]

while incorrect_guesses < max_incorrect and "_" in display_word:
    print("\nWord to guess: " + " ".join(display_word))
    print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good guess!")
    
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                display_word[i] = guess
    else:
        print("Wrong guess!")
        incorrect_guesses += 1


if "_" not in display_word:
    print(f"\nCongratulations! You guessed the word: {word_to_guess}")
else:
    print(f"\nGame Over! The word was: {word_to_guess}")
