📝 To-Do List Application

Overview
    This is a simple command-line To-Do List application built in Python. Users can add, view, and delete tasks interactively. The project demonstrates Python concepts such as functions, control flow, loops, input validation, and error handling.

Table of Contents
Features
Installation and Runniing Program
Example Interaction
Code Structure
Error Handling
Notes

Features
- Add Tasks: Users can add one or multiple tasks. Empty tasks are not allowed.
- View Tasks: Displays all tasks in a numbered list. Alerts if the list is empty.
- Delete Tasks: Users can delete tasks by specifying the task number. Handles invalid input and empty lists gracefully.
- Quit: Exit the application cleanly.
- Input Validation: Ensures all user inputs are valid and provides clear feedback for errors.


Installation and Running the Program
1. Make sure Python 3 is installed on your system.
2. Download the todo_list.py file.
3. Open a terminal or command prompt in the folder containing the file.
4. Run the program by executing: python todo_list.py
5. You will see a menu prompting you to select an action: Please select an Action (add/view/delete/quit)
6. Type add to add tasks. Type view to see all tasks. Type delete to remove a task. Type quit to exit the program.
7. The program will guide you with prompts and error messages if any input is invalid.

Example Interation
    Welcome! Keep track of all your tasks big or small, we'll make a list and check it all!

    Please select an Action (add/view/delete/quit): add
    Enter the task you want to add: Finish homework
    "Finish homework" has been added to the Your List.
    Would you like to add another task? (yes/no): no

    Please select an Action (add/view/delete/quit): view
    Your List:
    1. Finish homework
    Would you like to add another task? (yes/no): no

    Please select an Action (add/view/delete/quit): delete
    Your List:
    1. Finish homework
    Enter the number of the task you want to delete: 1
    "Finish homework" was deleted.
    Would you like to delete another task? (yes/no): no

    Please select an Action (add/view/delete/quit): quit
    Goodbye!

Code Structure

    Functions
        - add_task(tasks): Adds tasks to the list with validation.
        - view_tasks(tasks): Displays tasks and prompts to add more if the list is empty.
        - delete_task(tasks): Deletes tasks by number and handles invalid input.
        - yes_no_prompt(message): Reusable function to validate yes/no input.

    Main loop: Continuously prompts user for actions until they quit.

Error Handling
* Alerts for empty input.
* Alerts for invalid task number when deleting.
* Alerts if trying to view or delete tasks when the list is empty.
* Ensures valid menu option selection.

Notes
- Tasks are stored in a Python list (in-memory) and are not saved after the program exits.
- Designed for learning Python basics: functions, loops, conditionals, and error handling.
- CLI-based, no external libraries required.