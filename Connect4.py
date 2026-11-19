# Simple terminal Connect Four game. Enter a column number to drop a disc

# Constants
ROWS = 6
COLUMNS = 7

# Colors using ANSI code
RESET = "\033[0m"
BLUE = "\033[94m"
RED = "\033[91m"
YELLOW = "\033[93m"
DIM = "\033[90m"
BRIGHT = "\033[1m"


def print_board(board, player):
    print("\033[2J\033[H", end="")
    player_color = RED if player == 1 else YELLOW
    player_name = "Player 1 • Red" if player == 1 else "Player 2 • Yellow"
    print(f"{BRIGHT}                 CONNECT FOUR{RESET}")
    print("           Get four discs in a row to win.\n")
    print(f"  {player_color}{BRIGHT}{player_name}'s turn{RESET}\n")
    print("        " + "     ".join(str(column) for column in range(1, COLUMNS + 1)))
    print("      " + BLUE + "┌" + "─────┬" * (COLUMNS - 1) + "─────┐" + RESET)
    
    for row in board:
        cells = []

        for piece in row:
            if piece == "X":
                cells.append(f"{RED}●{RESET}")
            elif piece == "O":
                cells.append(f"{YELLOW}●{RESET}")
            else:
                cells.append(f"{DIM}·{RESET}")
        print(
            "      "
            + BLUE
            + "│"
            + RESET
            + "  "
            + "  │  ".join(cells)
            + "  "
            + BLUE
            + "│"
            + RESET
        )
    print("      " + BLUE + "└" + "─────┴" * (COLUMNS - 1) + "─────┘" + RESET)
    print("\n  Enter a column number (1–7) to drop a disc  •  Q to quit\n")


def check_winner(board, piece):
    # Check for four pieces next to each other horizontally or vertically.
    for row in range(ROWS):
        for column in range(COLUMNS):
            if column <= COLUMNS - 4:
                if all(board[row][column + offset] == piece for offset in range(4)):
                    return True
            if row <= ROWS - 4:
                if all(board[row + offset][column] == piece for offset in range(4)):
                    return True

    # Check the two diagonal directions.
    for row in range(ROWS - 3):
        for column in range(COLUMNS - 3):
            if all(
                board[row + offset][column + offset] == piece for offset in range(4)
            ):
                return True
    for row in range(ROWS - 3):
        for column in range(3, COLUMNS):
            if all(
                board[row + offset][column - offset] == piece for offset in range(4)
            ):
                return True

    return False


def play_game():
    board = [[" " for column in range(COLUMNS)] for row in range(ROWS)]
    player = 1
    pieces = {1: "X", 2: "O"}

    while True:
        print_board(board, player)
        choice = input(
            f"Player {player} ({pieces[player]}), choose a column (1-7): "
        ).strip()

        if choice.lower() in ("q", "quit"):
            print("Thanks for playing!")
            return
        if not choice.isdigit() or not 1 <= int(choice) <= COLUMNS:
            print("Please enter a number from 1 to 7 (or Q to quit).")
            continue

        column = int(choice) - 1
        if board[0][column] != " ":
            print("That column is full. Choose another one.")
            continue

        # Start at the bottom and place the piece in the first empty spot.
        for row in range(ROWS - 1, -1, -1):
            if board[row][column] == " ":
                board[row][column] = pieces[player]
                break

        if check_winner(board, pieces[player]):
            print_board(board, player)
            print(f"Player {player} ({pieces[player]}) wins!")
            return

        # If the top row is full, every column is full and the game is a draw.
        if all(board[0][column] != " " for column in range(COLUMNS)):
            print_board(board, player)
            print("It's a draw!")
            return

        if player == 1:
            player = 2
        else:
            player = 1


if __name__ == "__main__":
    print("CONNECT FOUR")
    print("Get four pieces in a row to win. Enter Q to quit.")
    play_game()
