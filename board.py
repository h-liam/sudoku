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
        self.board = [self.initialize_row() for _ in range(self.board_size * self.board_size)]
        
    def initialize_row(self):
        return [_ + 1 for _ in range(self.board_size * self.board_size)]
        
    
    def initialize_grid(self):
        self.grid = list(range(1, self.grid_size * self.grid_size + 1))
        
    def create_board_from_grids(self):
        self.initialize_grid()
        self.initialize_board_grid()
    
    def create_board_from_rows(self):
        self.initialize_board_row()

    def calculate_grid_number(self, x, y):
        # Works for 9*9 boards, Not sure if it works for different size boards. 
        x_percent = x / (self.board_size * self.board_size) * self.board_size
        x_percent = x_percent.__ceil__()
        y_percent = y / (self.board_size * self.board_size) * self.board_size
        
        grid_number = (x_percent + (y_percent.__floor__() * self.board_size))-1
        return grid_number
        # if the x is 0-2 and y is 0-2 then grid is 0
        # if the y is 0-2 it should be plus 0, if 
        
    def get_row(self, row_num:int) -> list:
        return self.board[row_num]
    
    def get_col(self, col_num:int) -> list:
        col = [self.board[i][col_num] for i in range(len(self.board))]
        return col
    
    def get_grid(self, grid_num) -> list:
        # for now this function only does 9x9 boards
        
        
        row_start = (grid_num // 3) * 3
        col_start = (grid_num % 3) * 3
        
        # Initialize an empty list to store the grid elements
        grid_elements = []
        
        # Loop through each row in the grid
        for row in range(row_start, row_start + 3):
            # Extract the elements for this row based on the calculated column indices
            grid_elements.extend(self.board[row][col_start:col_start + 3])
        
        return grid_elements
    
    def validate_num_row(self, num:int, row_num) -> bool:
        """Validate if the current number is allowed in the row"""
        if num in self.get_row(row_num):
            return False
        return True
            
    def validate_num_col(self, num:int, col_num) -> bool:
        """Validate if the current numbers is allowed in the column"""
        if num in self.get_col(col_num):
            return False
        return True
    

    def validate_num_grid(self, num:int, grid_num:int) -> bool:
        """validate if the current number is allowed in the current grid"""
        if num in self.get_grid(grid_num):
            return False
        return True
        
    def show_normal_board(self):
        if self.grid != None:
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
        else:
            for row in self.board:
                print(*row)   
                
                
 
    def show_board(self):
        # this funciton will print the board regardless of its size
        ...
    
    def show_row_board(self):
        """
        This function prints the contents of self.board in a formatted way representing a Sudoku board.
        """
        grid_size = self.board_size // (self.board_size // 3)  # Get the size of a sub-grid (e.g., 3 for 9x9)
        box_line = "+".join(["-" * (grid_size * 2) for _ in range(self.board_size // 3 + 1)]) + "+"

        # Loop through each row in the board
        for row in self.board:
            # Print the separator line at the beginning of each grid row
            if row == self.board[0] or (self.board.index(row) % grid_size == 0):
                print(box_line)
            
            # Print each element in the row with appropriate spacing and box separators
            for i, element in enumerate(row):
                end = " | " if (i + 1) % grid_size != 0 else " |"
                print("{:^2}".format(element if element != 0 else " "), end=end)
            print()  # Print a newline after each row

        # Print the final separator line
        print(box_line)
        
    
    def insert_number(self, x,y, number):
        if number > pow(self.board_size, 2):
            print("Wrong")
            return 0
        self.board[x][y] = number
        

        
        
        
        


if __name__ == "__main__":
    sudoku_test = Sudoku(grid_size=3, board_size=3)
    sudoku_test.create_board_from_rows()
    sudoku_test.show_row_board()
    print()
    sudoku_test.insert_number(1,1,4)
    sudoku_test.show_row_board()
    
    