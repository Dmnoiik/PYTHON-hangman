import random

attempts = 5
random_words = ["animal",
                "boiling",
                "ocean",
                "harmony",
                "discussion",
                "scandalous",
                "complete",
                "cobweb",
                "sister",
                "gray",
                "thirsty",
                "stew"]
# word_to_guess = random.choice(random_words)
word_to_guess = 'banana'
underscores = ["_" for letter in word_to_guess]
used_letters = []
print(' '.join(underscores))
while "_" in underscores:
    print(f"Used letters: {', '.join(used_letters)}")
    print(' '.join(underscores))
    guessed_letter = input("Guess the letter: ")
    if guessed_letter in used_letters or guessed_letter == " ":
        print("You already used this letter")
        continue
    if guessed_letter in word_to_guess:
        for index, letter in enumerate(word_to_guess):
            if letter == guessed_letter:
                underscores[index] = guessed_letter
        used_letters.append(guessed_letter)
    else:
        attempts -= 1
        used_letters.append(guessed_letter)
        print(F"Letter {guessed_letter} is incorrect, remaining attempts: {attempts}")
        if attempts == 0:
            print(f"Game over. The word was: {word_to_guess}")
            break
