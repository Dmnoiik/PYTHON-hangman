import random
from tkinter import *

# attempts = 5
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
# word_to_guess = 'banana'
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
    """
    Get the difficulty level, remove all radiobuttons, labels and button itself
    :return:
    """
    easy_radio_button.pack_forget()
    medium_radio_button.pack_forget()
    hard_radio_button.pack_forget()
    welcome_label.pack_forget()
    confirm_difficulty_button.pack_forget()
    display_underscores()


def display_underscores(words_list):

    if radio_var.get() == 'easy':
        filtered_words = [word for word in words_list if len(word) <= 4]
    elif radio_var.get() == 'medium':
        filtered_words = [word for word in words_list if 5 <= len(word) <= 7]
    elif radio_var.get() == 'hard':
        filtered_words = [word for word in words_list if 8 <= len(word) <= 12]
    word_to_guess = random.choice(random_words)
    underscores = ["_" for letter in word_to_guess]
    underscores_label = Label(text=f"{' '.join(underscores)}")
    underscores_label.pack()


# Set the window and background image of Hangman
window = Tk()
window.geometry("600x400")
radio_var = StringVar(value=" ")
# radiobuttons and button for the first window
welcome_label = Label(text="Welcome to Hangman game, please select the difficulty level and click start :)",
                      font=("Arial", 10, "normal"))
# radio buttons
easy_radio_button = Radiobutton(window, text="Easy", variable=radio_var, value='easy')
medium_radio_button = Radiobutton(window, text="Medium", variable=radio_var, value='medium')
hard_radio_button = Radiobutton(window, text="Hard", variable=radio_var, value='hard')

# buttons
confirm_difficulty_button = Button(window, text="Start a game", command=choose_difficulty)
# Layout creator
welcome_label.pack()
easy_radio_button.pack()
medium_radio_button.pack()
hard_radio_button.pack()
confirm_difficulty_button.pack()

# Main loop
window.mainloop()
