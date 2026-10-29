# import Minesweeper  # connect to the Minesweeper program
# import game2048   # connect to the 2048 game program
import Connect4  # connect to the Connect4 program

import os  # Used for clearing terminal for readability
import sys  # Used to terminate program

def end_game():
    """Terminate Program"""
    sys.exit("\nProgram Terminated, Thanks For Playing\n")


def clear_terminal():
    """Clears the terminal when called"""
    os.system("cls" if os.name == "nt" else "clear")


def test_menu_template(menu_function, test_input, expected_result):
    """Run a menu test and print PASS in green or FAIL in red."""

    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    result = menu_function(test_input)
    status = result == expected_result

    if status:
        message = f"{GREEN}PASS{RESET}"
    else:
        message = f"{RED}FAIL{RESET}"

    print(
        f"{message} | "
        f"Input: {test_input!r} | "
        f"Expected: {expected_result} | "
        f"Actual: {result}"
    )

    return status


def admin_run_test():
    # Replace actions temporarily so no games launch during tests
    FUNCTIONS["1"]["func"] = lambda: None
    FUNCTIONS["2"]["func"] = lambda: None
    FUNCTIONS["3"]["func"] = lambda: None
    FUNCTIONS["0"]["func"] = lambda: None

    GAMES["1"]["func"] = lambda: None
    GAMES["2"]["func"] = lambda: None
    GAMES["3"]["func"] = lambda: None

    # Test main menu
    test_menu_template(show_main_menu, "1", True)
    test_menu_template(show_main_menu, "game engine", True)
    test_menu_template(show_main_menu, " 1 ", True)
    test_menu_template(show_main_menu, "Show Scores", True)
    test_menu_template(show_main_menu, "Answer Questions: Get More Credits", True)
    test_menu_template(show_main_menu, "0", True)
    test_menu_template(show_main_menu, "Exit", True)

    # Invalid main menu inputs
    test_menu_template(show_main_menu, "invalid", False)
    test_menu_template(show_main_menu, "99", False)
    test_menu_template(show_main_menu, "-1", False)
    test_menu_template(show_main_menu, "Game", False)
    test_menu_template(show_main_menu, "engine", False)
    test_menu_template(show_main_menu, "", False)
    test_menu_template(show_main_menu, "1.0", False)
    test_menu_template(show_main_menu, "None", False)

    # Test game menu
    test_menu_template(show_game_menu, "1", True)
    test_menu_template(show_game_menu, "Connect Four", True)
    test_menu_template(show_game_menu, " 1 ", True)
    test_menu_template(show_game_menu, "2", True)
    test_menu_template(show_game_menu, "minesweeper", True)
    test_menu_template(show_game_menu, "2048", True)

    # Invalid game menu inputs
    test_menu_template(show_game_menu, "invalid", False)
    test_menu_template(show_game_menu, "-1", False)
    test_menu_template(show_game_menu, "Connect", False)
    test_menu_template(show_game_menu, "Mine", False)
    test_menu_template(show_game_menu, "", False)
    test_menu_template(show_game_menu, " ", False)
    test_menu_template(show_game_menu, "1.0", False)
    test_menu_template(show_game_menu, "abc123", False)


# A dictionary containing the name and the function reference for game storage
# When adding games please follow the function naming convention for clear code
# "{menu number}": {"name": "{game name}", "func": {gameRef.function}},
GAMES = {
    "1": {"name": "Connect Four", "func": Connect4.play_game},
    "0": {"name": "Exit", "func": end_game},
    "2": {"name": "Minesweeper", "func": lambda: print("\nMinesweeper program runs")},
    "3": {"name": "2048", "func": lambda: print("\n2048 program runs")},
    # "4": {"name": "Game 4",       "func": play_game_4},
    # "5": {"name": "Game 5",       "func": play_game_5},
}


def show_game_menu(test_input=None):
    """
    Runs the continuous terminal menu loop for the game selection menu.

    This function dynamically displays available game options from the global
    GAMES dictionary and accepts user input through the command line. It matches
    the input to game names or numbers and executes the corresponding function if
    a valid option is selected.

    Returns -> None: This function exits the loop and returns if the user presses
    Enter without a choice, otherwise it runs until a valid game completes.
    """

    while True:
        print("\nGame Engine")

        for number, game_data in GAMES.items():
            print(f"    {number}: {game_data['name']}")

        if test_input is not None:
            choice = str(test_input).strip()
        else:
            choice = input("Select a game (or press Enter to return): ").strip()

        if choice == "":
            if test_input is not None:
                return False
            clear_terminal()
            return

        selected_game = None

        for number, game_data in GAMES.items():
            if choice == number or choice.casefold() == game_data["name"].casefold():
                selected_game = game_data
                break

        if selected_game is not None:
            # During testing, validate only; do not launch the game.
            if test_input is not None:
                return True

            selected_game["func"]()
        else:
            print("That game is not available yet.")

            if test_input is not None:
                return False


ADMIN = {
    "1": {"name": "Test Menu Inputs", "func": admin_run_test},
    "0": {"name": "Exit", "func": end_game},
    # "5": {"name": "Game 5",       "func": play_game_5},
}


def show_admin_menu():
    """
    Runs the continuous terminal menu loop for Admin.

    This function displays a command-line menu by dynamically iterating through
    a global dictionary of options and names. It accepts user input, validates it
    against the available numbers or names, and executes the corresponding function.

    Returns -> None: This function runs with password and does not return a value.
    """

    adminPass = "admin123"
    password = input("Enter admin password: ")

    clear_terminal()

    if password != adminPass:
        print("password invalid")
        return

    while password == adminPass:
        print("\nAdmin Menu\n")

        for number, option_data in ADMIN.items():
            name = option_data["name"]
            print(f"{number}: {name}")

        choice = input("\nSelect an option (number or name): ").strip()

        selected_option = None

        # Loop through values in FUNCTIONS dictionary and determine execution
        for number, option_data in ADMIN.items():
            if choice == number or choice.casefold() == option_data["name"].casefold():
                selected_option = option_data
                break

        # Run the chosen function
        if selected_option:
            selected_option["func"]()  # Add () to execute the stored function
        else:
            print("\n Invalid choice. Please try again.")


# A dictionary containing the name and the function reference for game storage
# When adding menu items please follow the function naming convention for clear code
# "{menu number}": {"name": "{item name}", "func": {function}},
FUNCTIONS = {
    "1": {"name": "Game Engine", "func": show_game_menu},
    "2": {"name": "Show Scores", "func": lambda: print("\nScores")},
    "3": {
        "name": "Answer Questions: Get More Credits",
        "func": lambda: print("\ncredits"),
    },
    "4": {
        "name": "Admin Controls",
        "func": show_admin_menu,
    },
    "0": {"name": "Exit", "func": end_game},
    # "5": {"name": "Game 5",       "func": play_game_5},
}


def show_main_menu(test_input=None):
    """Display the main menu or test a single input."""

    while True:
        print("\nPlayMaze OS\n")

        for number, option_data in FUNCTIONS.items():
            print(f"{number}: {option_data['name']}")

        if test_input is not None:
            choice = str(test_input).strip()
        else:
            choice = input("Select an option: ").strip()

        selected_option = None

        for number, option_data in FUNCTIONS.items():
            if choice == number or choice.casefold() == option_data["name"].casefold():
                selected_option = option_data
                break

        if selected_option is not None:
            # During testing, validate only; do not execute the action.
            if test_input is not None:
                return True

            selected_option["func"]()
        else:
            print("Invalid choice. Please try again.")

            if test_input is not None:
                return False


if __name__ == "__main__":
    show_main_menu()
