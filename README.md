# SimplePython-Calculator
This is a simple yet well-structured Python calculator that I built as one of my first programming projects.  
It supports basic arithmetic operations and includes strong input validation and error handling, making it a reliable console-based tool.

---

## Features
- Input validation for numeric values  
- Error handling for:
  - Invalid input (`ValueError`)
  - Division by zero (`ZeroDivisionError`)
- Modular design using reusable functions
- Clear English prompts and clean code structure
- Repeats until valid inputs are provided
- Beginner-friendly and easy to read

---

## What I Learned
While building this project, I learned how to:
- Write reusable functions  
- Use `while True` loops effectively  
- Validate user input  
- Handle exceptions using `try` and `except`  
- Structure code in a clean and readable way  
- Build a basic interactive console application  

This project helped me understand the foundations of real programming logic.

---

## Code Structure

- **`get_operation()`**  
  Asks the user to choose a valid operation (`+`, `-`, `*`, `/`).

- **`get_number(message)`**  
  Asks the user for a valid numeric input with a customizable prompt.

- **`calculator()`**  
  Main function that runs the program, handles errors, and performs the operation.


  ---
  
##  Future Improvements
- Add more operations (exponent, square root, modulus)
- Allow multiple calculations without restarting the program
- Add a menu system
- Add color to console output
- Improve input validation
- Create a GUI version using Tkinter
- Convert this calculator into a small web app using Flask or FastAPI
- Add automated tests (unittest)


