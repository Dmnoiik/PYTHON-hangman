import random
from tkinter import *
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
# # word_to_guess = random.choice(random_words)
# word_to_guess = 'banana'
# underscores = ["_" for letter in word_to_guess]
# used_letters = []
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

# Set the window and background image of Hangman
window = Tk()
window.geometry("600x400")
# bg_image = PhotoImage(file="assets/hangman_bg.png")
# bg_label = Label(image=bg_image)
# bg_label.place(relx=0.5, rely=0.5, anchor='center')

welcome_label = Label(text="Welcome to Hangman game, please select the difficulty level and click start :)", font=("Arial", 10, "normal"))
welcome_label.grid(row=0, column=1)
radio_var = IntVar()
easy_radio_button = Radiobutton(window, text="Easy", variable=radio_var, value=1).grid(row=1, column=1, sticky="N")
medium_radio_button = Radiobutton(window, text="Medium", variable=radio_var, value=2).grid(row=2, column=1, sticky="N")
hard_radio_button = Radiobutton(window, text="Hard", variable=radio_var, value=3).grid(row=3, column=1, sticky="N")

# Main loop
window.mainloop()