class Hangman:
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


    def __init__(self, attempts: int, difficulty):
        self.attempts = attempts
        self.difficulty = difficulty
        self.word_to_guess = []
        self.underscores = []

    def unpack_widgets(self, list_of_widgets: list):
        for widget in list_of_widgets:
            widget.pack_forget()

    def pack_widgets(self, list_of_widgets: list):
        for widget in list_of_widgets:
            widget.pack()

    def update_underscores(self):
        self.underscores = ["_" for letter in self.word_to_guess]

