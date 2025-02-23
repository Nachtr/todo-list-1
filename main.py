# Import functions from task_manager.task_utils package
from task_manager import task_utils

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1": # Add Task
            title = input("Please enter the title for the task which should be added: ") # take the title, desc, and dd to create the task
            description = input("Please enter the description for the task which should be added: ")
            due_date = input("Please enter when it should be due (format in YYYY-MM-DD): ")
            description = description.strip()

            if not title or not description or not due_date:
                print("Error: Task title, description, and due date cannot be empty. Please try again..")
                print("")
                continue

            success = task_utils.add_task(title, description, due_date) # Assign to success variable for debugging purposes
            if not success:
                print("Error: Task failed to add. Please check input values!")
                print("")
            else:
                print(f"Task: {title} due on {due_date} was successfully added!")
                print("")


        elif choice == "2": # Mark Task as complete
            if task_utils.tasks:
                task_utils.view_pending_tasks()
                print("")

                try:
                    index = int(input("Which task would you like to complete?: ")) - 1 # Minus one to make sure that its proper indexing.
                    if index < 0 or index >= len(task_utils.tasks):
                        print("Error: Invalid task number. Please try again.")
                        print("")
                    else: # Implementing fail safes above and below this!
                        task_utils.mark_task_as_complete(index)
                        print("Task successfully completed!")
                        print("")
                except ValueError:
                    print("Error: Please enter a valid number")
                    print("")
            else: # after checking if there are tasks, if there are none then return to menu and alert the user
                print("No tasks available to complete!")
                print("")

        elif choice == "3": # View pending tasks
            if task_utils.tasks:
                task_utils.view_pending_tasks()
                print("")
            else:
                print("No tasks available to complete!")
                print("")

        elif choice == "4": # Progress
            progress = task_utils.calculate_progress()
            print(f"Current Completion Progress: {progress:.2f}%")
            print("")


        elif choice == "5": # Exit
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

        
if __name__ == "__main__":
    main()
