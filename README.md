# Baseball Team Manager -- CPRO 2201 Midterm

## About This Project

This project is my midterm assignment for CPRO 2201 (Python Programming
II). The program allows a baseball team manager to manage a team lineup
using a menu-driven console application.

I followed Sections 1--3 of the Murach Baseball Team Manager case study.
The project uses object-oriented programming and separates the user
interface, business logic, and file handling into different modules.

------------------------------------------------------------------------

## What the Program Can Do

The program allows the user to:

1.  Display the current lineup\
2.  Add a new player\
3.  Remove a player\
4.  Move a player to a new lineup position\
5.  Edit a player's position\
6.  Edit a player's stats (at-bats and hits)\
7.  Exit the program

The lineup data is stored in a CSV file, so changes remain after
restarting the program.

------------------------------------------------------------------------

## Project Structure

The project is organized into the following files:

-   main.py -- Controls the overall flow of the program\
-   ui.py -- Handles all user input and output\
-   objects.py -- Contains the Player and Lineup classes\
-   db.py -- Handles reading from and writing to the CSV file\
-   players.csv -- Stores player data

This structure follows the layered design approach from the textbook.

------------------------------------------------------------------------

## Object-Oriented Design

### Player Class

The Player class stores: - First name\
- Last name\
- Position\
- At-bats\
- Hits

It also calculates the batting average. If a player has 0 at-bats, the
batting average returns 0.0 to avoid division errors.

Validation ensures: - Hits cannot be greater than at-bats\
- Stats cannot be negative\
- Only valid positions are accepted

------------------------------------------------------------------------

### Lineup Class

The Lineup class manages a list of Player objects. It allows adding,
removing, and moving players within the lineup.

------------------------------------------------------------------------

## How to Run the Program

1.  Make sure all project files are in the same folder.
2.  Open the folder in PyCharm.
3.  Run main.py.

------------------------------------------------------------------------

## Summary

This project demonstrates object-oriented programming, input validation,
file handling with CSV, and proper separation of program layers.
