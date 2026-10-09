# Python Project Setup, Git, and GitHub Workflow

## Project Description

This project demonstrates Python project organization, Git version control, GitHub collaboration, and basic Python functions.

## Project Structure

* `main.py` — Runs the program and asks the user for input.
* `utils.py` — Contains reusable functions for squaring numbers, checking even numbers, converting Celsius to Fahrenheit, and greeting users.
* `config.py` — Reserved for project configuration settings.
* `README.txt` — Project text file.
* `.gitignore` — Excludes Python cache files, compiled `.pyc` files, and `.env` files from Git tracking.
* `src/` — Contains the initial Python source files.
* `tests/` — Reserved for test files.
* `docs/` — Contains project documentation, including `README.md`.

## Features

1. Calculates the square of a number.
2. Checks whether a number is even or odd.
3. Converts Celsius to Fahrenheit.
4. Greets the user by name.

## How to Run

1. Install Python 3.

2. Open a terminal in the project folder.

3. Run the program:

   `python main.py`

4. Enter your name and a whole number when prompted.

## Git and GitHub Workflow

The project uses Git to track changes and record commits. The `main` branch contains the original project, while the `feature/add-greeting` branch contains the personalized greeting feature. The greeting changes are submitted through a pull request for review.

## What I Learned

This assignment helped me practise creating folders and files using the command line, writing reusable Python functions, importing functions between modules, and testing a program with different inputs. I learned how `.gitignore` excludes unnecessary files and how Git commits record project changes. I also practised pushing a local repository to GitHub, creating a feature branch, and opening a pull request. Separating source code, tests, and documentation makes a project easier to maintain and understand.
