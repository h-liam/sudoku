class Sudoku:
    def __init__(self, grid_size=3, board_size=3):
        self.grid_size = grid_size
        self.board_size = board_size
        self.board = None
        self.grid = None
        
    
    
    
    def initialize_board(self):
        self.board = [self.grid] * self.board_size * self.board_size
        
    def initialize_grid(self):
        self.grid = list(range(1, self.grid_size * self.grid_size + 1))
        
    def create_board(self):
        self.initialize_grid()
        self.initialize_board()
        
    def show_board(self):
        # this funciton will print the board regardless of its size
        ...
        
    def get_row(self, row_num:int) -> list:
        row = self.board
        
        return row
    
    def get_col(self, col_num:int) -> list:
        col = []
        return col
    
    def validate_num_row(self, num:int) -> bool:
        ...
        for i in range(self.board_size):
            
            ...
            
    def validate_num_col(self, num:int) -> bool:
        ...
    
    def validate_num_grid(self, num:int, grid_num:int) -> bool:
        ...
    
    def show_normal_board(self):
        print(self.board[0][0:3], "|",  self.board[1][0:3], "|",  self.board[2][0:3])
        print(self.board[0][3:6], "|",  self.board[1][3:6], "|",  self.board[2][3:6])
        print(self.board[0][6:9], "|",  self.board[1][6:9], "|",  self.board[2][6:9])
        print("", "-"*30)
        print(self.board[3][0:3], "|",  self.board[4][0:3], "|",  self.board[5][0:3])
        print(self.board[3][3:6], "|",  self.board[4][3:6], "|",  self.board[5][3:6])
        print(self.board[3][6:9], "|",  self.board[4][6:9], "|",  self.board[5][6:9])
        print("", "-"*30)
        print(self.board[6][0:3], "|",  self.board[7][0:3], "|",  self.board[8][0:3])
        print(self.board[6][3:6], "|",  self.board[7][3:6], "|",  self.board[8][3:6])
        print(self.board[6][6:9], "|",  self.board[7][6:9], "|",  self.board[8][6:9])  
            
        
        
        
        


if __name__ == "__main__":
    sudoku_test = Sudoku()
    sudoku_test.create_board()
    sudoku_test.show_normal_board()
    print(sudoku_test.board)
    