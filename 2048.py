import math
import random

class game2048:
    def __init__(self):
        self.board_size = 4
        self.score = 0
        self.board = [[0] * 4 for _ in range(4)]
        self.game_over = False

        # likelihood of spawning each num
        self.two_percentage = 0.9
        self.four_percentage = 0.1

        # game starts with 2 tiles on board
        self.add_tile()
        self.add_tile()

    def display_board(self):
        for i in range(self.board_size):
            if i % self.board_size == 0 and i != 0:
                print()
            print(self.board[i])

    def add_tile(self):
        if random.random() < self.two_percentage:
            tile_val = 2
        else:
            tile_val = 4

        # Find an empty spot on the board
        # empty_spots = [(row, col) for row in range(self.board_size) for col in range(self.board_size) if self.board[row][col] == 0]
        # if empty_spots:
        #     row, col = random.choice(empty_spots)
        #     self.board[row][col] = tile_val

        row = random.randint(0, self.board_size - 1)
        col = random.randint(0, self.board_size - 1)

        while self.board[row][col] != 0:
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
            
        self.board[row][col] = tile_val

    def move(self, direction):
        pass  # Movement logic to be implemented, remember to update score

    def game_over(self):
        pass  # Game over logic to be implemented

def main():
    game = game2048()
    game.display_board()

if __name__ == "__main__":
    main()