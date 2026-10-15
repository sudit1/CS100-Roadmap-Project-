# This file is a template and not main driver for program

GAMES = (
    (1, "Game 1"),
    (2, "Game 2"),
    (3, "Game 3"),
    (4, "Game 4"),
    (5, "Game 5"),
)

def show_game_menu():
    print("\nGame Engine")
    for number, name in GAMES:
        print(f"{number}: {name}")

    return input("Select a game (or press Enter to return or exit): ")


def show_credits():
    print("\nCredits")
    input("Press Enter to return to the menu: ")


def controller():
    while True:
        print("\nPlayMaze OS")
        print("1: Game Engine")
        print("2: Show Credits")
        print("0: Exit")

        choice = input("Select an option: ").strip().lower()

        if choice in ("1", "game engine"):
            show_game_menu()

        elif choice in ("2", "show credits"):
            show_credits()

        elif choice in ("0", "exit"):
            print("Program terminated.")
            break

        else:
            print("Invalid selection.")
            continue

        restart = input("\nReturn to the main menu? (y/n): ").strip().lower()
        if restart != "y":
            print("Program terminated.")
            break


controller()