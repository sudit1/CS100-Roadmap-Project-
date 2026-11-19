import random

def create_board():
    """Initializes a 4x4 grid with empty cells and spawns two starting tiles."""
    board = [[{"value": 0, "type": "empty"} for _ in range(4)] for _ in range(4)]
    
    # Spawn the first two starting tiles
    spawn_tile(board)
    spawn_tile(board)
    
    return board

def spawn_tile(board):
    """Finds available empty cells and spawns a random int, float, or str tile."""
    empty_cells = []
    for r in range(4):
        for c in range(4):
            if board[r][c]["type"] == "empty":
                empty_cells.append((r, c))
    
    if not empty_cells:
        return
    
    r, c = random.choice(empty_cells)
    tile_type = random.choice(["int", "float", "str"])
    
    if tile_type == "int":
        board[r][c] = {"value": 2, "type": "int"}
    elif tile_type == "float":
        board[r][c] = {"value": 1.5, "type": "float"}
    else:
        board[r][c] = {"value": "A", "type": "str"}

def print_board(board, score=0):
    """Renders the 4x4 board showing ONLY the values, keeping data types hidden from the player!"""
    print(f"\nScore: {score}")
    print("-" * 25)
    for row in board:
        row_str = "|"
        for cell in row:
            if cell["type"] == "empty":
                row_str += "     |"
            else:
                # Only prints the value, concealing whether it's an int, float, or str
                row_str += f" {str(cell['value']):^3} |"
        print(row_str)
        print("-" * 25)

def play_game():
    # Test your board creation and printing!
    board = create_board()
    print_board(board)

if __name__ == "__main__":
    play_game()