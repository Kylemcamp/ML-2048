import numpy as np

class game2048:
    '''Class to represent the 2048 game environment
       Note: if this iwsn't fast enoguht look into numba jit'''

    def __init__(self, board_size: int = 4, seed: int | None = None):
        self.board_size = board_size
        self.score = 0
        self.board = np.zeros((board_size, board_size), dtype=np.int16)
        self.game_over = False

        # likelihood of spawning each num
        self.two_percentage = 0.9
        self.four_percentage = 0.1

        # rand number gen for reproducibility 
        self.rng = np.random.default_rng(seed)

        # start with 2 tiles on board
        self.spawn_tile()
        self.spawn_tile()

    def display_board(self):
        for i in range(self.board_size):
            print(self.board[i])
        print(f"Score: {self.score}\n")

    def reset(self, seed: int | None = None):
        if seed is not None:
            self.rng = np.random.default_rng(seed)
        self.board.fill(0)
        self.score = 0
        self.game_over = False
        self.spawn_tile()
        self.spawn_tile()
        return self.board.copy()

    def spawn_tile(self):
        # choose 2 with prob two_percentage else 4
        tile_val = 2 if self.rng.random() < self.two_percentage else 4

        empty = np.argwhere(self.board == 0)
        
        idx = self.rng.integers(0, len(empty))
        r, c = empty[idx]
        self.board[r, c] = tile_val
    
    def check_game_over(self):
        if 0 in self.board:
            self.game_over = False
        elif np.any(self.board[:-1, :] == self.board[1:, :]) or np.any(self.board[:, :-1] == self.board[:, 1:]):
            # check adjacent tiles for matches
            self.game_over = False 
        else:
            self.game_over = True  # game is over

    def move(self, direction):
        '''Move and update score'''
        if direction == 'w':
            self.push_up()
            score = self.merge_up()
            self.push_up()
        elif direction == 's':
            self.push_down()
            score = self.merge_down()
            self.push_down()
        elif direction == 'a':
            self.push_left()
            score = self.merge_left()
            self.push_left()
        elif direction == 'd':
            self.push_right()
            score = self.merge_right()
            self.push_right()
        else:
            raise ValueError("Invalid direction")

        self.score += score

    def game_over(self):
        print("GAME OVER")

    def merge_right(self):
        score = 0
        for i in range(self.board_size):
            for j in range(0, self.board_size-1)[::-1]:
                if self.board[i][j] == self.board[i][j+1]:
                    self.board[i][j+1] *= 2
                    self.board[i][j] = 0
                    score += self.board[i][j+1]
        return score

    def merge_left(self):
        score = 0
        for i in range(self.board_size):
            for j in range(0, self.board_size-1):
                if self.board[i][j] == self.board[i][j+1]:
                    self.board[i][j] *= 2
                    self.board[i][j+1] = 0
                    score += self.board[i][j]
        return score

    def merge_up(self):
        score = 0
        for i in range(self.board_size):
            for j in range(0, self.board_size-1):
                if self.board[j][i] == self.board[j+1][i]:
                    self.board[j][i] *= 2
                    self.board[j+1][i] = 0
                    score += self.board[j][i]
        return score

    def merge_down(self):
        score = 0
        for i in range(self.board_size):
            for j in range(0, self.board_size-1)[::-1]:
                if self.board[j][i] == self.board[j+1][i]:
                    self.board[j+1][i] *= 2
                    self.board[j][i] = 0
                    score += self.board[j+1][i]
        return score

    def push_left(self):
        idx = np.argsort(self.board == 0, axis=1, kind='stable') 
        self.board = np.take_along_axis(self.board, idx, axis=1)

    def push_right(self):
        idx = np.argsort(self.board != 0, axis=1, kind='stable')
        self.board = np.take_along_axis(self.board, idx, axis=1)

    def push_up(self):
        idx = np.argsort(self.board == 0, axis=0, kind='stable')
        self.board = np.take_along_axis(self.board, idx, axis=0)

    def push_down(self):
        idx = np.argsort(self.board != 0, axis=0, kind='stable')
        self.board = np.take_along_axis(self.board, idx, axis=0)

def main():
    game = game2048()
    game.board = np.array([[0, 0, 0, 0],
                           [0, 0, 0, 2],
                           [0, 0, 0, 2],
                           [2, 2, 2, 8]])

    while not game.game_over:
        game.display_board()
        move = input("Enter move: ")
        game.move(move)
        game.check_game_over()
        game.spawn_tile()

        # [0 0 0 0]
        # [0 0 0 2]
        # [0 0 0 2]
        # [2 2 2 8]

        # move: d (right)
        # [0 0 0 0]
        # [0 2 0 2]
        # [0 0 0 2]
        # [0 4 2 8]

if __name__ == "__main__":
    main()