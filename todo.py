tasks = []

print("Welcome! Keep track of all your tasks big or small, we'll make a list and check it all!")

while True:
    option = input("\nPlease select an Action (add/view/delete/quit) ").lower()

    if option == "add":
        while True:
            task = input("Enter the task you want to add: ")
            tasks.append(task)
            print(f'"{task}" has been added to the Your List.')
            add_another = input("Would you like to add another task? (yes/no) ").lower()
            if add_another.lower() != "yes":
                break

    elif option == "view":
        if len(tasks) == 0:
            print("Your List is empty.")
            add_task = input("Would you like to add a task? (yes/no) ").lower()
            if add_task == "yes":
                task = input("Enter the task you want to add: ")
                tasks.append(task)
                print(f'"{task}" has been added to the Your List.')
                while True:
                    add_another = input("Would you like to add another task? (yes/no) ").lower()
                    if add_another.lower() == "yes":
                        task = input("Enter the task you want to add: ")
                        tasks.append(task)
                        print(f'"{task}" has been added to the Your List.')
                    else:
                        break
                
        else:
            print("Your List:")
            i = 1
            for task in tasks:
                print(f"{i}. {task}")
                i += 1
            add_another = input("Would you like to add another task? (yes/no) ").lower()
            if add_another.lower() == "yes":
                while True:
                    task = input("Enter the task you want to add: ")
                    tasks.append(task)
                    print(f'"{task}" has been added to the Your List.')
                    if input("Add another? (yes/no) ").lower() != "yes":
                        break

    elif option == "delete":
        if len(tasks) == 0:
            print("Your List is empty. There's nothing to delete.")
        else:
            while True:
                print("Your List:")
                i = 1
                for task in tasks:
                    print(f"{i}. {task}")
                    i += 1
                task_number = int(input("Enter the number of the task you want to delete: "))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f'"{removed_task}" was deleted.')
                else:
                    print("Invalid task number.")
                delete_another = input("Would you like to delete another task? (yes/no) ").lower()
                if delete_another.lower() != "yes":
                    break
                
    elif option == "quit":
        print("Goodbye!")
        break 

    else:
        print("Invalid option — try again.")
                    


