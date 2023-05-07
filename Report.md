# Simple Login System

#### This is a Practice Project i made while learning Python

The provided code is a simple login system implemented using the tkinter library in Python.  
It allows users to register new accounts and login to existing accounts.  

## Module Dependencies
- `tkinter`: Used for creating the graphical user interface (GUI) and handling user interactions.
- `tkinter.messagebox`: Provides message boxes for displaying information, warnings, and error messages.

## Global Variables
- `root`: The main tkinter window.
- `btn_bg_color`: Custom color for button backgrounds.
- `btn_fg_color`: Custom color for button foregrounds (text color).
- `bg_color`: Custom color for the background of the GUI.
- `label_font`: Font configuration for labels.
- `button_font`: Font configuration for buttons.
- `x`: Dictionary to store user account information (username and password).

## Functions
1. `new()`: Clears the GUI and displays the initial welcome screen with login, register, and exit buttons.
2. `login()`: Clears the GUI and displays the login screen with username and password entry fields.
    - `login1()`: Validates the entered username and password and performs the login operation. Shows appropriate messages based on the login result.
3. `register()`: Clears the GUI and displays the registration screen with username, password, and confirm password entry fields.
    - `register1()`: Validates the entered username and password, checks for existing usernames, and performs the registration operation. Shows appropriate messages based on the registration result.
4. `close()`: Closes the tkinter window and terminates the program.

## GUI Elements
### Labels
- "Welcome to 101": Displays a welcome message.
- "User Name": Label for the username entry field.
- "Password": Label for the password entry field.
- "Confirm": Label for the confirm password entry field.

### Entry Fields
- `name`: Entry field for entering the username.
- `password`: Entry field for entering the password.
- `confirm`: Entry field for confirming the password during registration.

### Buttons
- "Login": Triggers the login process.
- "Register": Triggers the registration process.
- "Exit": Closes the tkinter window.

## Execution Flow
1. The main tkinter window is created with the specified title and dimensions.
2. The GUI elements (labels, buttons, and entry fields) are configured and placed within the window.
3. The `new()` function is called to display the initial welcome screen.
4. User interactions (clicking buttons, entering data) trigger the corresponding functions to handle login, registration, and exit operations.
5. The GUI elements are updated, and appropriate message boxes are shown based on the operation results.
6. The program continues to run until the tkinter window is closed.

##### Please note that the code provides basic functionality and does not include features such as data persistence, password encryption, or user authentication.
