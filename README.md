# PythonScaffold

A Python desktop application developed for university programming coursework at UTS. This project demonstrates my growing understanding of OOP, GUI design, event-driven programming, and project organisation in Python.

## Overview

This project uses Python and Tkinter to create a graphical user interface for a card-based application. My written program is just the top files

## Overview

PythonScaffold is built around a card game structure with players, a dealer, cards, hands, and different GUI views. Instead of running only through the terminal, the program uses Tkinter to create a visual interface where users can log in as players, view cards, interact with their hand, and access different parts of the game through buttons, windows, and visual card displays.

The project demonstrates how a Python program can be split into different responsibilities. The model files handle the underlying game objects and logic, while the view files control what the user sees on screen. This helped me practise object-oriented programming, GUI development, and organising a larger program across multiple files.

## What the Program Does

The program creates a GUI-based card game environment. It includes:

* A login screen for setting up or accessing players
* A dealer interface for managing game actions
* Player windows that display player-related information
* Card display screens that show individual cards visually
* Error windows that provide feedback when something goes wrong
* Win/result screens for game outcomes
* Image-based card assets to make the interface more visual

The overall purpose of the program is to simulate a card-game application where different users can interact with cards through a graphical interface rather than typed commands.

## Main Components

### LoginView.py

Handles the starting screen of the program. This view is responsible for allowing players to enter or access the game before the main card interface is shown.

### DealerView.py

Represents the dealer side of the application. This part of the program manages dealer-related actions and connects the game logic to the interface.

### PlayerView.py

Creates the player interface. This allows a player to view their cards, interact with the game, and receive updates through the GUI.

### CardView.py

Displays an individual card visually. This helps make the program more user-friendly because users can see card information through a window instead of only reading text output.

### DeckView.py

Displays or manages deck-related information in the interface. This supports the card-game structure by connecting the deck logic to the GUI.

### ErrorView.py

Shows error messages in a separate window when invalid actions occur. This improves the user experience by giving clear feedback instead of letting the program fail silently or crash without explanation.

### PlayerWinView.py

Displays the result or winning outcome for a player. This provides a clearer ending or success state within the GUI.

### TkUtils.py

Contains helper functions used to make the interface more consistent. Instead of rewriting the same Tkinter styling and widget setup code repeatedly, this file helps keep the GUI more organised.

### model folder

Contains the underlying classes and logic used by the program. These files represent the non-visual parts of the application, such as players, cards, decks, hands, or game rules.

### image folder

Stores image assets used by the GUI, including card images and other visual elements.

## Technologies Used

* Python
* Tkinter

## What I Learned

Through this project, I developed a better understanding of how to structure a Python application across multiple files. I also gained experience using classes, building user interface components, handling user interactions, and organising code so that different parts of the program have clear responsibilities.

This project also helped me practise using GitHub as a portfolio tool by uploading coursework and documenting what the project does.

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code or another Python IDE.
3. Make sure Python is installed.
4. Run the main application file.

```bash
python LoginView.py
```

Note: The exact file used to start the program may depend on the final project structure.

## Future Improvements

* Improve comments and documentation
* Next time actually use Github for it
* Add screenshots of the interface
* Clean up unused files such as cache folders
* Add more detailed explanation of each class
* Practise using branches and commits for future changes

## Author

Adrian Dwyer
Bachelor of Computer Science (Honours), University of Technology Sydney
