# Playmaze - Puzzle Games for Entertainment + CS Learning

Playmaze is a terminal-based virtual arcade that combines classic puzzle
and strategy games with introductory computer science concepts. Designed
for students who want to practice fundamental CS skills in an
interactive environment, Playmaze turns concepts such as data types,
arithmetic operations, and binary representation into part of the
gameplay.

Players can choose from three games: **2048, Minesweeper, and Connect
Four**. The project is developed in Python for the FA26 CS100H03 Roadmap
Project.

## Features

### Main Menu and Game Selection

-   Navigate the Playmaze terminal interface through menu options.
-   Select from the available games.
-   Validate user input and handle invalid menu selections.
-   Access an administrative menu for running input-validation tests.

### 2048 - Data Types and Typecasting

-   Play on a 4 × 4 game board.
-   Move tiles using directional keyboard input.
-   Work with tiles containing different Python data types, including
    integers, floats, and strings.
-   Explore type compatibility through tile merging. Compatible values
    can be combined, while incompatible types are handled through error
    checking.

### Minesweeper - Arithmetic Expressions

-   Play on a minefield displayed in the terminal.
-   Use the surrounding cells to determine the number of adjacent mines.
-   Interpret arithmetic expressions displayed on cells rather than
    relying only on conventional numeric clues.
-   Practice arithmetic evaluation while identifying safe cells and
    mines.

### Connect Four - Binary Representation

-   Play Connect Four on a shared game board.
-   Use a target integer and binary representation as part of the
    planned educational gameplay.
-   Practice converting decimal integers into binary and applying binary
    logic to the game.

### Planned Stretch Goal: CS Trivia and Credits

-   Load computer science trivia questions and answers from text files.
-   Randomize questions to reduce repetition.
-   Use timed questions to add a speed-based challenge.
-   Award additional game credits for correct answers.
-   Use file handling to save and retrieve player scores and game
    statistics.

> **Development note:** The trivia and credit system, cross-game score
> persistence, and some of the educational game mechanics were
> identified as development goals in the project milestones. Their
> availability depends on the final implementation.

## How to Play

1.  Start the program using the instructions below.
2.  Navigate the main menu using the displayed options.
3.  Select a game from the game selection menu.
4.  Follow the prompts displayed in the terminal to enter moves and
    interact with the game.
5.  Use valid menu choices and game inputs. Invalid entries are handled
    by the program.

The project design includes an arcade-style credit system in which
players begin with credits to access games and can earn more by
answering CS trivia questions.

## Getting Started

### Prerequisites

-   Python 3
-   A terminal or command-line interface
-   Git (optional, for cloning the repository)

### Installation

Clone the repository:

``` bash
git clone https://github.com/HS0524/CS100-Roadmap-Project-.git
```

Navigate into the project directory:

``` bash
cd CS100-Roadmap-Project-
```

Run the main driver program:

``` bash
python driver.py
```

If your system uses `python3` to run Python, use:

``` bash
python3 driver.py
```

## Computer Science Concepts

Playmaze applies concepts introduced in CS100, including:

-   **Variables and Data Types:** Store scores, turns, game states, and
    tile values.
-   **Lists and Nested Lists:** Represent game data and two-dimensional
    game boards.
-   **Loops and Conditional Statements:** Control gameplay, process
    moves, and evaluate game outcomes.
-   **Functions:** Organize menu navigation, game logic, board creation,
    input processing, and win/loss detection.
-   **User Input and Validation:** Process menu selections, player
    moves, and quiz answers.
-   **Dictionaries:** Organize menu options, functions, questions,
    answers, and score information.
-   **Python Modules:** Use modules such as `random` and `time` for
    randomized gameplay and timed features.
-   **File I/O:** Support loading trivia questions and saving player
    statistics.

## Project Structure

The project is organized around a main driver program and separate game
implementations.

``` text
CS100-Roadmap-Project-/
│
├── driver.py          # Main program, menus, and game navigation
├── connect4.py        # Connect Four game
├── minesweeper.py     # Minesweeper game
├── 2048.py            # 2048 game implementation (if named this way)
├── README.md          # Project documentation
└── ...
```

The exact filenames may vary depending on the final repository
structure.

## Team Members

  -----------------------------------------------------------------------
  Team Member                         Contributions
  ----------------------------------- -----------------------------------
  **Jennifer Nguyen**                 Minesweeper implementation and
                                      flowchart; function breakdown and
                                      AI/resources documentation.

  **Suditi Choudhury**                2048 implementation and flowchart;
                                      function breakdown and test plan.

  **Harshil Shah**                    Main driver program, menu systems,
                                      administrative menu,
                                      input-validation tests, and Connect
                                      Four flowchart.
  -----------------------------------------------------------------------

## Testing

The project design includes tests for the following scenarios:

  -----------------------------------------------------------------------
  Test Category           Example                 Expected Result
  ----------------------- ----------------------- -----------------------
  Typical Input           Select a game with      The program accepts the
                          sufficient credits.     selection and launches
                                                  the game.

  Invalid Input           Enter an invalid menu   The program displays an
                          option.                 error message and
                                                  returns to the menu.

  Unusual Input           Attempt to launch a     The program prevents
                          game with insufficient  access and displays an
                          credits.                appropriate message.

  Stretch Goal            Answer CS trivia        The program awards
                          questions correctly.    additional credits.
  -----------------------------------------------------------------------

## Development Tools and Resources

-   **Python** - Main programming language.
-   **Git and GitHub** - Version control and team collaboration.
-   **ChatGPT** - Used as a thinking partner for brainstorming,
    planning, debugging, code review, and feedback.
-   **Python documentation and course materials** - Used as programming
    references.

AI tools supported the development process but were not intended to
replace the team's problem-solving or generate complete game
implementations. Team members are responsible for understanding and
explaining the code they submit.

## Repository

[CS100 Roadmap Project -
GitHub](https://github.com/HS0524/CS100-Roadmap-Project-)

------------------------------------------------------------------------

*FA26-CS100H03 \| Roadmap Project \| Group 3*
