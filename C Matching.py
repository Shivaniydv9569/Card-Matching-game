import tkinter as tk
import random
from tkinter import messagebox

class MemoryGame:
    def __init__(self, root):  # ✅ Fixed from _init_ to __init__
        self.root = root
        self.root.title("Card Matching Game 🃏")
        self.root.resizable(False, False)

        # Setup game variables
        self.buttons = []
        self.first_card = None
        self.second_card = None
        self.card_symbols = []
        self.matched = []
        self.moves = 0

        # Create game board
        self.create_board()

    def create_board(self):
        symbols = ['🍎', '🍌', '🍒', '🍇', '🍉', '🥝', '🍋', '🍍']
        self.card_symbols = symbols * 2  # 16 cards total
        random.shuffle(self.card_symbols)

        # Create buttons (4x4 grid)
        for i in range(4):
            row = []
            for j in range(4):
                btn = tk.Button(self.root, text=" ", width=8, height=4,
                                 command=lambda x=i, y=j: self.flip_card(x, y),
                                 font=("Arial", 18, "bold"), bg="lightblue")
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

        # Move counter label
        self.move_label = tk.Label(self.root, text="Moves: 0", font=("Arial", 14, "bold"))
        self.move_label.grid(row=4, column=0, columnspan=4, pady=10)

    def flip_card(self, x, y):
        index = x * 4 + y
        btn = self.buttons[x][y]

        # Ignore if card already matched or opened
        if btn["text"] != " " or index in self.matched:
            return

        btn["text"] = self.card_symbols[index]

        if not self.first_card:
            self.first_card = (x, y)
        else:
            self.second_card = (x, y)
            self.root.after(800, self.check_match)
            self.moves += 1
            self.move_label.config(text=f"Moves: {self.moves}")

    def check_match(self):
        x1, y1 = self.first_card
        x2, y2 = self.second_card

        index1 = x1 * 4 + y1
        index2 = x2 * 4 + y2

        btn1 = self.buttons[x1][y1]
        btn2 = self.buttons[x2][y2]

        # Check if match
        if self.card_symbols[index1] == self.card_symbols[index2]:
            self.matched.extend([index1, index2])
            btn1.config(bg="lightgreen")
            btn2.config(bg="lightgreen")
        else:
            btn1.config(text=" ")
            btn2.config(text=" ")

        self.first_card = None
        self.second_card = None

        # Win condition
        if len(self.matched) == len(self.card_symbols):
            messagebox.showinfo("Congratulations!", f"You Win! 🏆\nTotal Moves: {self.moves}")

# Run game
if __name__ == "__main__":  # ✅ Fixed from _name_ to __name__
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
