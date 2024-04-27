class Sudoku:

    def __init__(self, grid_size=3, board_size=3):
        self.grid_size = grid_size
        self.board_size = board_size
        self.board = None
        self.grid = None
        self.row = None

    def initialize_board_grid(self):
        """Create board out of list of grids"""
        self.board = [self.grid] * self.board_size * self.board_size

    def initialize_board_row(self):
        """Create board out of list of rows"""
        self.board = [
            self.row for _ in range(self.board_size * self.board_size)
        ]

    def initialize_row(self):
        self.row = [_ + 1 for _ in range(self.board_size * self.board_size)]

    def initialize_grid(self):
        self.grid = list(range(1, self.grid_size * self.grid_size + 1))

    def create_board_from_grids(self):
        self.initialize_grid()
        self.initialize_board_grid()

    def create_board_from_rows(self):
        self.initialize_row()
        self.initialize_board_row()

    def calculate_grid_number(self, x, y):
        print(self.board_size / x)
        x_percent = x / (self.board_size * self.board_size) * 3
        return x_percent
        # if the x is 0-2 and y is 0-2 then grid is 0

    def get_row(self, row_num: int) -> list:
        return self.board[row_num]

    def get_col(self, col_num: int) -> list:
        col = [self.board[i][col_num] for i in range(len(self.board))]
        return col

    def get_grid(self) -> list:
        current_grid = []
        return current_grid

    def validate_num_row(self, num: int, row_num) -> bool:
        """Validate if the current number is allowed in the row"""
        if num in self.get_row(row_num):
            return False
        return True

    def validate_num_col(self, num: int, col_num) -> bool:
        """Validate if the current numbers is allowed in the column"""
        if num in self.get_col(col_num):
            return False
        return True

    def validate_num_grid(self, num: int, grid_num: int) -> bool:
        """validate if the current number is allowed in the current grid"""
        ...

    def show_normal_board(self):
        if self.grid != None:
            print(self.board[0][0:3], "|", self.board[1][0:3], "|",
                  self.board[2][0:3])
            print(self.board[0][3:6], "|", self.board[1][3:6], "|",
                  self.board[2][3:6])
            print(self.board[0][6:9], "|", self.board[1][6:9], "|",
                  self.board[2][6:9])
            print("", "-" * 30)
            print(self.board[3][0:3], "|", self.board[4][0:3], "|",
                  self.board[5][0:3])
            print(self.board[3][3:6], "|", self.board[4][3:6], "|",
                  self.board[5][3:6])
            print(self.board[3][6:9], "|", self.board[4][6:9], "|",
                  self.board[5][6:9])
            print("", "-" * 30)
            print(self.board[6][0:3], "|", self.board[7][0:3], "|",
                  self.board[8][0:3])
            print(self.board[6][3:6], "|", self.board[7][3:6], "|",
                  self.board[8][3:6])
            print(self.board[6][6:9], "|", self.board[7][6:9], "|",
                  self.board[8][6:9])
        else:
            for row in self.board:
                print(*row)

    def show_board(self):
        # this funciton will print the board regardless of its size
        ...


if __name__ == "__main__":
    sudoku_test = Sudoku()
    sudoku_test.create_board_from_rows()
    sudoku_test.show_normal_board()
    print(sudoku_test.get_row(0))
    print(sudoku_test.calculate_grid_number(6, 3))
