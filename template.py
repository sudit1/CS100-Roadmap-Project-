while True:
    print("\nPlayMaze OS")
    print("1: Game Engine")
    print("2: Calculator Engine")
    print("3: Show Credits")
    print("0: Exit")

    main_choice = input("Select an option: ")

    if main_choice == "1":
        print("\nGame Engine")
        print("1: Pong")
        print("2: Snake")
        print("3: Tic-Tac-Toe")
        print("4: Rock-Paper-Scissors")
        print("5: BINGO")
        input("Select a game (or press Enter to return): ")

    elif main_choice == "2":
        print("\nCalculator Engine")
        print("1: Quadratic Formula")
        print("2: Basic Calculator")
        print("3: Circle Equations")
        print("4: Power Function")
        print("5: Square Root")
        print("6: Number Multiplier")
        print("7: Trigonometric Functions")
        print("8: Number Sequence Addition")
        print("9: BMI Calculator")
        print("10: Conversions")
        print("11: Salary Calculator")
        print("12: Random Number Generator")
        print("13: Quadratic Graphing")
        print("14: Interest Rate Calculator")
        print("16: Extraterrestrial Weight Conversion")
        print("17: Clock")
        input("Select an option (or press Enter to return): ")

    elif main_choice == "3":
        print("\nCredits")
        input("Press Enter to return to the menu: ")

    elif main_choice == "0":
        print("Program terminated.")
        break

    else:
        print("Invalid selection.")

    restart = input("\nReturn to the main menu? (y/n): ").lower()
    if restart != "y":
        print("Program terminated.")
        break