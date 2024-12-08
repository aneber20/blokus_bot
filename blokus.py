import tkinter as tk
from threading import Thread

class BoardGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Blokus Game")

        # Create game board (e.g., a 20x20 grid)
        self.board_frame = tk.Frame(self.root, width=800, height=600)
        self.board_frame.pack()

        # Add buttons or other interactive elements to the board
        self.buttons = []
        for i in range(20):
            row = []
            for j in range(20):
                button = tk.Button(self.board_frame, text="", command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        # Define the players and their current turn
        self.players = [1, 2, 3, 4]
        self.current_player_index = 0

        # Create a label to display whose turn it is
        self.current_player_label = tk.Label(self.board_frame, text="Current Player: ")
        self.current_player_label.grid(row=21, column=0, columnspan=20)

    def on_click(self, i, j):
        print(f"Button at position ({i}, {j}) clicked by player {self.players[self.current_player_index]}!")
        self.next_turn()


    def next_turn(self):
        current_player = self.players[self.current_player_index]
        print(f"Now it's player {current_player}'s turn...")

        # Update the UI to show whose turn it is (e.g., display a label with their name)
        self.current_player_label.config(text=f"Current Player: {current_player}")

        # Make the current player make their move
        # Add code here to handle the player's move (e.g., update the board state, play sound effects, etc.)

        # Switch to the next player
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        if self.game_loop_running:
            self.root.after(1000)  # Call next_turn after a short delay

    def start_game(self):
        self.game_loop_running = True
        self.root.mainloop()

if __name__ == "__main__":
    game = BoardGame()
    game.start_game()