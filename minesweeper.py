import random

letters = "ABCDEFGHIJKLMNO"
# Each level stores: board size, minimum mines, maximum mines.
difficulties = {"1": (5, 5, 8), "2": (10, 15, 25), "3": (15, 30, 50)}


def show_tutorial():
    """Explain normal Minesweeper rules and our arithmetic variation."""
    print("\nReveal every safe square without hitting a mine.")
    print("Each clue counts mines in the eight surrounding squares,")
    print("including diagonals. Our clues are arithmetic expressions:")
    print("2 * 2 means FOUR adjacent mines; 6 // 3 means TWO.")
    print("// is integer division and % gives the remainder.")
    print("A dot (.) means zero adjacent mines and opens nearby safe squares.")
    print("Your first reveal is always safe.")
    print("\nEnter A1 to reveal column A, row 1 (lowercase works too).")
    print("Enter F A1 to flag/unflag a suspected mine; flags block reveals.")
    print("Flags are reminders: you win by revealing all safe squares.")
    print("Enter Q to return to the arcade. '-' means an unopened square.\n")


def create_board(size, value):
    """Make independent rows, so changing one row cannot change another."""
    return [[value for col in range(size)] for row in range(size)]


def validate_input(coordinate, size):
    """Return zero-based (row, column), or False for invalid coordinates."""
    coordinate = coordinate.strip().upper()
    if len(coordinate) < 2 or coordinate[0] not in letters[:size]:
        return False
    # Check digits before int(), including two-digit rows such as A10.
    digits = coordinate[1:]
    if not digits.isascii() or not digits.isdigit() or len(digits) > 2:
        return False
    row = int(digits) - 1
    col = letters.index(coordinate[0])
    if row < 0 or row >= size:
        return False
    return row, col


def neighbors(row, col, size):
    """List valid surrounding coordinates without wrapping across edges."""
    result = []
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if 0 <= r < size and 0 <= c < size:
                if (r, c) != (row, col):
                    result.append((r, c))
    return result


def place_mines(size, mine_count, first_row, first_col):
    """Place exactly mine_count mines, excluding the first reveal."""
    real_field = create_board(size, 0)
    available = []
    for row in range(size):
        for col in range(size):
            if (row, col) != (first_row, first_col):
                available.append((row, col))
    # sample chooses distinct positions, so mines cannot overlap.
    for row, col in random.sample(available, mine_count):
        real_field[row][col] = '*'
    return real_field


def adjacent_mines(real_field, row, col):
    """Count mines in the up-to-eight squares surrounding a position."""
    count = 0
    for r, c in neighbors(row, col, len(real_field)):
        if real_field[r][c] == '*':
            count += 1
    return count


def arithmetic_op(x):
    """Return a random Python arithmetic expression whose value is x."""
    addend = random.randint(0, x)
    extra = random.randint(1, 8)
    factor = random.randint(2, 4)
    choices = [f"{addend} + {x - addend}", f"{x + extra} - {extra}",
               f"{x} * 1", f"{x * factor} // {factor}",
               f"{x + 9} % 9"]
    # Add more interesting multiplication when x has integer factors.
    for divisor in range(2, x + 1):
        if x % divisor == 0:
            choices.append(f"{divisor} * {x // divisor}")
    return random.choice(choices)


def reveal_square(real_field, user_field, row, col):
    """Reveal a square and connected empty areas; return False on a mine.

    A list of pending squares replaces recursive function calls. Flags and
    existing clues are left alone. Each clue is generated only once.
    """
    if user_field[row][col] != '-':
        return True
    if real_field[row][col] == '*':
        user_field[row][col] = '*'
        return False

    pending = [(row, col)]
    while pending:
        r, c = pending.pop()
        if user_field[r][c] != '-':
            continue
        count = adjacent_mines(real_field, r, c)
        if count > 0:
            user_field[r][c] = arithmetic_op(count)
        else:
            user_field[r][c] = '.'
            for next_row, next_col in neighbors(r, c, len(real_field)):
                if user_field[next_row][next_col] == '-':
                    if real_field[next_row][next_col] != '*':
                        pending.append((next_row, next_col))
    return True


def check_win(real_field, user_field):
    """Flags never substitute for revealing a safe square."""
    for row in range(len(real_field)):
        for col in range(len(real_field)):
            if real_field[row][col] != '*':
                if user_field[row][col] in ('-', 'F'):
                    return False
    return True


def count_revealed(user_field):
    """Score: one point per safe square revealed, including empty squares."""
    score = 0
    for row in user_field:
        for cell in row:
            if cell not in ('-', 'F', '*'):
                score += 1
    return score


def display_board(user_field, mine_count, real_field=None):
    """Print aligned expression cells; optionally show mines after a loss."""
    width = 1
    flags = 0
    for row in user_field:
        for cell in row:
            width = max(width, len(cell))
            if cell == 'F':
                flags += 1
    print(f"\nMines: {mine_count} | Flags: {flags} | Score: {count_revealed(user_field)}")
    print("    " + " | ".join(letter.center(width) for letter in letters[:len(user_field)]))
    for row in range(len(user_field)):
        cells = []
        for col in range(len(user_field)):
            cell = user_field[row][col]
            if real_field is not None:
                if real_field[row][col] == '*':
                    cell = '*'
                elif cell == 'F':
                    cell = 'X'  # A misplaced flag on a safe square.
            cells.append(cell.center(width))
        print(f"{row + 1:>2}  " + " | ".join(cells))
    print()


def play_game():
    """Play one round; return a result dictionary for future arcade scoring.

    status is 'won', 'lost', or 'quit'. Credits and saved scores belong to
    the arcade driver; this module does not deduct credits or write files.
    """
    print("\nWelcome to Arithmetic Minesweeper!")
    while True:
        choice = input("Show tutorial? (Y/N, Q to return): ").strip().upper()
        if choice == 'Q':
            return {"status": "quit", "score": 0}
        if choice in ('Y', 'N'):
            if choice == 'Y':
                show_tutorial()
            break
        print("Invalid input. Please enter Y, N, or Q.")

    while True:
        level = input("Choose difficulty: 1 Easy, 2 Medium, 3 Hard (Q to return): ").strip().upper()
        if level == 'Q':
            return {"status": "quit", "score": 0}
        if level in difficulties:
            break
        print("Invalid input. Please enter 1, 2, 3, or Q.")

    size, minimum, maximum = difficulties[level]
    mine_count = random.randint(minimum, maximum)
    user_field = create_board(size, '-')
    # Delay mine placement until the first valid, unflagged reveal.
    real_field = None
    print("\nReveal: A1 | Flag/unflag: F A1 | Help: H | Return: Q")
    while True:
        display_board(user_field, mine_count)
        command = input("Your move: ").strip().upper()
        if command == 'Q':
            return {"status": "quit", "score": count_revealed(user_field)}
        if command == 'H':
            show_tutorial()
            continue
        parts = command.split()
        flag_move = len(parts) == 2 and parts[0] == 'F'
        if flag_move:
            coordinate = parts[1]
        elif len(parts) == 1:
            coordinate = parts[0]
        else:
            print("Use a coordinate such as A1, or F A1 to flag/unflag.")
            continue
        position = validate_input(coordinate, size)
        if position is False:
            print(f"Invalid coordinate. Use A1 through {letters[size - 1]}{size}.")
            continue
        row, col = position
        cell = user_field[row][col]
        if flag_move:
            if cell == '-':
                user_field[row][col] = 'F'
            elif cell == 'F':
                user_field[row][col] = '-'
            else:
                print("You cannot flag an already revealed square.")
            continue
        if cell == 'F':
            print("Unflag that square before revealing it (F " + coordinate + ").")
            continue
        if cell != '-':
            print("That square is already revealed.")
            continue
        if real_field is None:
            real_field = place_mines(size, mine_count, row, col)
        if not reveal_square(real_field, user_field, row, col):
            display_board(user_field, mine_count, real_field)
            print("You hit a mine! * shows mines; X shows misplaced flags.")
            print(f"Final score: {count_revealed(user_field)}")
            return {"status": "lost", "score": count_revealed(user_field)}
        if check_win(real_field, user_field):
            display_board(user_field, mine_count)
            print("You win! You revealed every safe square.")
            print(f"Final score: {count_revealed(user_field)}")
            return {"status": "won", "score": count_revealed(user_field)}


if __name__ == '__main__':
    play_game()
