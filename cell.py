from stone import Stone

class Cell:
    def __init__(self, cell_type: str, is_empty: bool = True):
        if cell_type not in ('goal', 'block', 'normal'):
            raise ValueError("cell_type must be 'goal', 'block', or 'normal'")

        self.cell_type = cell_type
        self.is_empty = is_empty
        self.stone = None

    def add_stone(self, stone: Stone):
        if self.cell_type == 'block':
            raise ValueError("Cannot place a stone in a block cell")
        self.stone = stone
        self.is_empty = False

    def remove_stone(self):
        self.stone = None
        self.is_empty = True

    def __str__(self):
        type_char = {'goal': 'G', 'block': 'B', 'normal': 'N'}.get(self.cell_type, 'N')
        state = 'empty' if self.is_empty else 'notEm'
        stone_type = self.stone.stone_type if self.stone else " "
        return f"{type_char}, {state}, {stone_type}"
    
    def find_cell_position(board, target_cell):
        for i in range(board.size):
            for j in range(board.size):
                if board.grid[i][j] == target_cell:
                    return (i, j)
        return None 