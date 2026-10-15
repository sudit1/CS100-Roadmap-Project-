import Connect4  # connection to the Connect4 program
import os  # Used for clearing terminal for readability


def clear_terminal():
    # supports windoes and mac terminal support
    os.system("cls" if os.name == "nt" else "clear")


# A dictionary containing the name and the function reference for game storage
# When adding games please follow the function naming convention for clear code
GAMES = {
    "1": {"name": "Connect Four", "func": Connect4.play_game},
    "2": {"name": "Minesweeper", "func": lambda: print("\nMinesweeper program runs")},
    "3": {"name": "2048", "func": lambda: print("\n2048 program runs")},
    # "4": {"name": "Game 4",       "func": play_game_4},
    # "5": {"name": "Game 5",       "func": play_game_5},
}


def show_game_menu():
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
            name = game_data["name"]
            print(f"{number} -> {name}")

        choice = input("Select a game (or press Enter to return): ").strip()

        if choice == "":
            clear_terminal()
            return

        # Loop through values in FUNCTIONS GAMES and determine execution
        for num, game_data in GAMES.items():
            if choice == num or choice.casefold() == game_data["name"].casefold():
                selected_game = game_data
                break

        # Run the chosen function
        if selected_game:
            selected_game["func"]()  # Add () to execute the stored function
        else:
            clear_terminal()
            print("That game is not available yet.")


# A dictionary containing the name and the function reference for game storage
# When adding games please follow the function naming convention for clear code
FUNCTIONS = {
    "1": {"name": "Game Engine", "func": show_game_menu},
    "2": {"name": "Show Scores", "func": lambda: print("\nScores")},
    "3": {
        "name": "Answer Questions: Get More Credits",
        "func": lambda: print("\ncredits"),
    },
    "0": {"name": "Exit", "func": lambda: print("\nProgram terminated")},
    # "5": {"name": "Game 5",       "func": play_game_5},
}


def main_menu_control():
    """
    Runs the continuous terminal menu loop for PlayMaze OS.

    This function displays a command-line menu by dynamically iterating through
    a global dictionary of options and names. It accepts user input, validates it
    against the available numbers or names, and executes the corresponding function.

    Returns -> None: This function runs indefinitely and does not return a value.
    """

    while True:
        print("\nPlayMaze OS\n")

        for number, option_data in FUNCTIONS.items():
            name = option_data["name"]
            print(f"{number}: {name}")

        choice = input("\nSelect an option (number or name): ").strip()

        selected_option = None

        # Loop through values in FUNCTIONS dictionary and determine execution
        for number, option_data in FUNCTIONS.items():
            if choice == number or choice.casefold() == option_data["name"].casefold():
                selected_option = option_data
                break

        # Run the chosen function
        if selected_option:
            selected_option["func"]()  # Add () to execute the stored function
        else:
            print("\n Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu_control()
