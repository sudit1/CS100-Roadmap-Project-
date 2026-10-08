while True:
    print("\nPlayMaze OS")
    print("1: Game Engine")
    print("2: Show Credits")
    print("0: Exit")

    main_choice = input("Select an option: ")

    if main_choice == "1":
        print("\nGame Engine")
        print("1: Game 1")
        print("2: Game 2")
        print("3: Game 3")
        print("4: Game 4")
        print("5: Game 5")
        
        input("Select a game (or press Enter to return): ")

    
    elif main_choice == "2":
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