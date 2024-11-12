from cell import Cell
from stone import Stone
import copy
class Board:
    def __init__(self, size: int ,step: int):
        self.step = step
        self.size = size
        self.grid = [[Cell(cell_type='normal') for _ in range(size)] for _ in range(size)]

    def place_cell(self, x: int, y: int, cell_type: str):
        if 0 <= x < self.size and 0 <= y < self.size:
            self.grid[x][y] = Cell(cell_type=cell_type)
        else:
            raise IndexError("Cell position out of board bounds")

    def place_stone(self, x: int, y: int, stone: Stone):
        if 0 <= x < self.size and 0 <= y < self.size:
            cell = self.grid[x][y]
            cell.add_stone(stone)
        else:
            raise IndexError("Stone position out of board bounds")

    def move_stone(self, x1: int, y1: int, x2: int, y2: int):
        board_copy = copy.deepcopy(self)
        
        if board_copy.step == 0:
            raise IndexError("You can't move the stone...")
           
        if 0 <= x1 < board_copy.size and 0 <= y1 < board_copy.size and 0 <= x2 < board_copy.size and 0 <= y2 < board_copy.size:
            start_cell = board_copy.grid[x1][y1]
            end_cell = board_copy.grid[x2][y2]

            if start_cell.stone and end_cell.is_empty:
                stone_type = start_cell.stone.stone_type
                
                end_cell.add_stone(start_cell.stone)
                start_cell.remove_stone()
                
                if stone_type == '+':
                    board_copy._apply_repulsion(x2, y2)
                elif stone_type == '-':
                    board_copy._apply_attraction(x2, y2)
            else:
                raise IndexError("Cannot move stone: destination is not empty or no stone to move")
                
        else:
            raise IndexError("Stone position out of board bounds")
        
        if board_copy.step == 0:
            raise IndexError("No more moves left.")
        board_copy.step -= 1
        return board_copy
        
    def check_win(self) -> bool:
        """Check if all goal cells are not empty."""
        for row in self.grid:
            for cell in row:
                if cell.cell_type == 'goal' and cell.is_empty:
                    return False
        return True

    def _apply_repulsion(self, x: int, y: int):
        # Right
        start = y + 1
        while start < self.size and not self.grid[x][start].stone:
            start += 1

        if start < self.size:
            end = start
            while end < self.size and (self.grid[x][end].stone or self.grid[x][end].cell_type == 'block'):
                end += 1

            if end < self.size:
                while end != start:
                    start_cell = self.grid[x][end - 1]
                    end_cell = self.grid[x][end]

                    if start_cell.stone and end_cell.is_empty and end_cell.cell_type != 'block':
                        end_cell.add_stone(start_cell.stone)
                        start_cell.remove_stone()
                    end -= 1

        # Left 
        start = y - 1
        while start >= 0 and not self.grid[x][start].stone :
            start -= 1

        if start >= 0:
            end = start
            while end >= 0 and (self.grid[x][end].stone or self.grid[x][end].cell_type == 'block'):
                end -= 1

            if end >= 0:
                while end != start:
                    start_cell = self.grid[x][end + 1]
                    end_cell = self.grid[x][end]

                    if start_cell.stone and end_cell.is_empty and end_cell.cell_type != 'block':
                        end_cell.add_stone(start_cell.stone)
                        start_cell.remove_stone()
                    end += 1

        # Below 
        start = x + 1
        while start < self.size and not self.grid[start][y].stone :
            start += 1
        if start < self.size:
            end = start
            while end < self.size and (self.grid[end][y].stone or self.grid[end][y].cell_type == 'block'):
                end += 1

            if end < self.size:
                while end != start:
                    start_cell = self.grid[end - 1][y]
                    end_cell = self.grid[end][y]

                    if start_cell.stone and end_cell.is_empty and end_cell.cell_type != 'block':
                        end_cell.add_stone(start_cell.stone)
                        start_cell.remove_stone()
                    end -= 1

        # Above
        start = x - 1
        while start >= 0 and not self.grid[start][y].stone:
            start -= 1

        if start >= 0:
            end = start
            while end >= 0 and (self.grid[end][y].stone or self.grid[end][y].cell_type == 'block'):
                end -= 1

            if end >= 0:
                while end != start:
                    start_cell = self.grid[end + 1][y]
                    end_cell = self.grid[end][y]

                    if start_cell.stone and end_cell.is_empty and end_cell.cell_type != 'block':
                        end_cell.add_stone(start_cell.stone)
                        start_cell.remove_stone()
                    end += 1

    def _apply_attraction(self, x: int, y: int):
        # Right
        start = y + 1
        while start < self.size - 1:
            if (self.grid[x][start].cell_type != "block" and 
                self.grid[x][start].is_empty and 
                self.grid[x][start + 1].stone):
                
                start_cell = self.grid[x][start + 1]
                end_cell = self.grid[x][start]

                if start_cell.stone and end_cell.is_empty and end_cell.cell_type != "block":
                    end_cell.add_stone(start_cell.stone)
                    start_cell.remove_stone()

            start += 1

        # Left
        start = y - 1
        while start > 0:  
            if (self.grid[x][start].cell_type != "block" and 
                self.grid[x][start].is_empty and 
                self.grid[x][start - 1].stone):
                
                start_cell = self.grid[x][start - 1]
                end_cell = self.grid[x][start]

                if start_cell.stone and end_cell.is_empty and end_cell.cell_type != "block":
                    end_cell.add_stone(start_cell.stone)
                    start_cell.remove_stone()

            start -= 1

        # Below
        start = x + 1
        while start < self.size - 1:
            if (self.grid[start][y].cell_type != "block" and 
                self.grid[start][y].is_empty and 
                self.grid[start + 1][y].stone):
                
                start_cell = self.grid[start + 1][y]
                end_cell = self.grid[start][y]

                if start_cell.stone and end_cell.is_empty and end_cell.cell_type != "block":
                    end_cell.add_stone(start_cell.stone)
                    start_cell.remove_stone()

            start += 1

        # Above
        start = x - 1
        while start > 0:
            if (self.grid[start][y].cell_type != "block" and 
                self.grid[start][y].is_empty and 
                self.grid[start - 1][y].stone):
                
                start_cell = self.grid[start - 1][y]
                end_cell = self.grid[start][y]

                if start_cell.stone and end_cell.is_empty and end_cell.cell_type != "block":
                    end_cell.add_stone(start_cell.stone)
                    start_cell.remove_stone()

            start -= 1

    def find_x(self,magnet):
        for i in range(self.size):
            for j in range(self.size):
                cell = self.grid[i][j]
                stone = cell.stone
                if stone is not None and stone.stone_type == magnet:
                    return i
        return None
                
                
                
    def find_y(self,magnet):
        for i in range(self.size):
            for j in range(self.size):
                cell = self.grid[i][j]
                stone = cell.stone
                if stone is not None and stone.stone_type ==magnet:
                    return j    
        return None  


    def display(self):
        print("the steps =",self.step,"\n")
        for row in self.grid:
            print(" | ".join(str(cell) for cell in row))
            print("-" * (self.size * 15 - 1))

            