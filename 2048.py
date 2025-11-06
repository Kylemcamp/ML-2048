import numpy as np

class game2048:
    def __init__(self, board_size: int = 4, seed: int | None = None):
        self.board_size = board_size
        self.score = 0
        self.board = np.zeros((board_size, board_size), dtype=np.int16)
        self.game_over = False

        # likelihood of spawning each num
        self.two_percentage = 0.9
        self.four_percentage = 0.1

        # RNG for reproducibility and batching compatibility
        self.rng = np.random.default_rng(seed)

        # start with 2 tiles on board
        self.spawn_tile()
        self.spawn_tile()

    def display_board(self):
        for i in range(self.board_size):
            print(self.board[i])

    def reset(self, seed: int | None = None):
        if seed is not None:
            self.rng = np.random.default_rng(seed)
        self.board.fill(0)
        self.score = 0
        self.game_over = False
        self.spawn_tile()
        self.spawn_tile()
        return self.board.copy()

    def spawn_tile(self) -> bool:
        # choose 2 with prob two_percentage else 4
        tile_val = 2 if self.rng.random() < self.two_percentage else 4

        empty = np.argwhere(self.board == 0)
        if empty.size == 0:
            return False
        idx = self.rng.integers(0, len(empty))
        r, c = empty[idx]
        self.board[r, c] = tile_val
        return True

    def move(self, direction):
        pass  # Movement logic to be implemented, remember to update score

    def game_over(self):
        pass  # Game over logic to be implemented

def main():
    game = game2048()
    game.display_board()

if __name__ == "__main__":
    main()