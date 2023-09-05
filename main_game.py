import random
from tkinter import *
from Hangman import Hangman
# attempts = 5
# random_words = ["animal",
#                 "boiling",
#                 "ocean",
#                 "harmony",
#                 "discussion",
#                 "scandalous",
#                 "complete",
#                 "cobweb",
#                 "sister",
#                 "gray",
#                 "thirsty",
#                 "stew"]
# word_to_guess = None
# underscores = None
used_letters = []


# print(' '.join(underscores))
# while "_" in underscores:
#     print(f"Used letters: {', '.join(used_letters)}")
#     print(' '.join(underscores))
#     guessed_letter = input("Guess the letter: ")
#     if guessed_letter in used_letters or guessed_letter == " ":
#         print("You already used this letter")
#         continue
#     if guessed_letter in word_to_guess:
#         for index, letter in enumerate(word_to_guess):
#             if letter == guessed_letter:
#                 underscores[index] = guessed_letter
#         used_letters.append(guessed_letter)
#     else:
#         attempts -= 1
#         used_letters.append(guessed_letter)
#         print(F"Letter {guessed_letter} is incorrect, remaining attempts: {attempts}")
#         if attempts == 0:
#             print(f"Game over. The word was: {word_to_guess}")
#             break
def choose_difficulty():
    hangman.unpack_widgets([easy_radio_button, medium_radio_button, hard_radio_button,
                            welcome_label, confirm_difficulty_button])
    display_underscores()
    guess_letter_entry.pack()


def display_underscores():
    difficulty_flag = radio_var.get()
    if difficulty_flag == 'easy':
        filtered_words = [word for word in hangman.random_words if len(word) <= 4]
    elif difficulty_flag == 'medium':
        filtered_words = [word for word in hangman.random_words if 5 <= len(word) <= 7]
    elif difficulty_flag == 'hard':
        filtered_words = [word for word in hangman.random_words if 8 <= len(word) <= 12]
    # hangman.word_to_guess = random.choice(filtered_words)
    hangman.word_to_guess = 'banana'
    hangman.update_underscores()
    underscores_label.config(text=f"{' '.join(hangman.underscores)}")
    hangman.pack_widgets([underscores_label, confirm_letter_button])


def check_letter():
    guessed_letter = guess_letter_entry.get()
    if guessed_letter in hangman.word_to_guess:
        for index, letter in enumerate(hangman.word_to_guess):
            if letter == guessed_letter:
                hangman.underscores[index] = guessed_letter
        underscores_label.config(text=f"{' '.join(hangman.underscores)}")
    if "_" not in hangman.underscores:
        finish_game()

def finish_game():
    hangman.unpack_widgets([underscores_label, guess_letter_entry, confirm_letter_button])
    finish_label.pack(side=TOP, anchor=NE)



# Set the window and background image of Hangman
window = Tk()
window.geometry("600x400")
radio_var = StringVar(value=" ")
hangman = Hangman(attempts=5, difficulty=radio_var)

# Labels
welcome_label = Label(text="Welcome to Hangman game, please select the difficulty level and click start :)",
                      font=("Arial", 10, "normal"))
underscores_label = Label(text="")
finish_label = Label(text="Congrats, you won!")

# radio buttons
easy_radio_button = Radiobutton(window, text="Easy", variable=radio_var, value='easy')
medium_radio_button = Radiobutton(window, text="Medium", variable=radio_var, value='medium')
hard_radio_button = Radiobutton(window, text="Hard", variable=radio_var, value='hard')

# buttons
confirm_difficulty_button = Button(window, text="Start a game", command=choose_difficulty)
confirm_letter_button = Button(window, text="Check the letter", command=check_letter)

# Entry for inserting letter
guess_letter_entry = Entry(width=5)

# Layout creator
hangman.pack_widgets([welcome_label, easy_radio_button, medium_radio_button,
                      hard_radio_button, confirm_difficulty_button])

# Main loop
window.mainloop()
