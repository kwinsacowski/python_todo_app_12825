tasks = []

#welcome message
print("\nWelcome! Keep track of all your tasks big or small, we'll make a list and check it all!")



#Functions
def add_task(tasks):
    while True:
        task = input("Enter the task you want to add: ")
        if task == "":
            print("Task cannot be empty. Please enter a valid task.")
            continue

        tasks.append(task)
        print(f'"{task}" has been added to the Your List.')

        if not yes_no_prompt("Would you like to add another task? (yes/no) "):
            return

def view_tasks(tasks):
    if not tasks:
        print("Your List is empty.")
        if yes_no_prompt("Would you like to add a task? (yes/no) "):
            add_task(tasks)
        return
   
    else:
        print("Your List:")
        i = 1
        for task in tasks:
            print(f"{i}. {task}")
            i += 1
        if yes_no_prompt("Would you like to add another task? (yes/no) "):
            add_task(tasks)

def delete_task(tasks):
    while True:
        if len(tasks) == 0:
            print("Your List is empty. There are no tasks to delete.")
            break
        print("Your List:")
        i = 1
        for task in tasks:
            print(f"{i}. {task}")
            i += 1
        task_number = input("Enter the number of the task you want to delete: ")
        if task_number == "":
            print("Input cannot be empty. Please enter a valid task number.")
            continue
        try:
            task_number = int(task_number)
        except ValueError:
            print("Please enter a valid task number.")
            continue
        else: 
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f'"{removed_task}" was deleted.')
            else:
                print("Invalid task number.")
                continue
            if not yes_no_prompt("Would you like to delete another task? (yes/no) "):
                return

def yes_no_prompt(message):
    while True:
        answer = input(message).strip().lower()
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")



#Main Loop
while True:
    option = input("Please select an Action (add/view/delete/quit) ").lower().strip()
    if option == "":
        print("Input cannot be empty. Please enter a valid option.")
        continue
    if option == "add":
        add_task(tasks)
    elif option == "view":
        view_tasks(tasks)
    elif option == "delete":
        delete_task(tasks)
    elif option == "quit":
        print("Goodbye!")
        break 

    else:
        print("Invalid option — try again.")
                    


