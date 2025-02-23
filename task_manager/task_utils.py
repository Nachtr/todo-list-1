# Import validation functions
from task_manager import validation

# Define tasks list
tasks = []
# Define completed tasks list
completed_tasks = []

# Implement add_task function
def add_task(title, description, due_date): # We need to use validate functions to check if the title, description, and due date are valid
    global tasks
    # print("Debugging Statement, comment out later")

    title_true = validation.validate_task_title(title)
    description_true = validation.validate_task_description(description)
    due_date_true = validation.validate_due_date(due_date)

    # print(f"Debugging: title_valid = {title_true}, description_true = {description_true}, due_date_true = {due_date_true}")

    if not title_true: # We are going to try to use if not statements this time instead of validating within an if statement
        # print("Title Validation Failed")
        return

    if not description_true:
        # print("Description Validation Failed")
        return

    if not due_date_true:
        # print("Due Date Validation Failed")
        return True

    # Formating for the task

    task = {
        "Title": title,
        "Description": description,
        "Due_Date": due_date,
        "Completed": False
    }

    # Appending the task
    tasks.append(task)
    # print("Debug: Current Tasks list after adding: ", tasks)
    # print("Debugging Statement: Task appended successfully!")
    return True

# Make sure to comment this out as this is for testing only!
# add_task("Hello", "Hellllo", "2025-02-22")
# print("Debugging tasks list:", tasks)

# Implement mark_task_as_complete function
def mark_task_as_complete(index):
    global tasks, completed_tasks # define the tasks as global to ensure that we are modifying the global list

    # Let's check if the index is within range of the task list
    if index < 0 or index >= len(tasks):
        print("invalid task index!")
        return

    # Accessing the task instead of looping and del
    task = tasks.pop(index)
    task["Completed"] = True
    # Move the task over
    completed_tasks.append(task)
    # Print statement
    print(f"Task '{task['Title']}' has been moved to completed tasks!")

# Index has to be used in python notation of 0 = 1, 1 = 2, etc...
# mark_task_as_complete(0)
# print(tasks)
# Mark out after test is complete!

# Implement view_pending_tasks function
def view_pending_tasks():
    global tasks

    if not tasks:
        print("No current tasks!") # Created this so that if there was no tasks in the to do list it would print that
        return

    print("Pending tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}, {task['Title']} - Due: {task['Due_Date']} - Completed: {task['Completed']}") # i + 1 to create a list that has all of the assigned tasks.
         # skip over the description so that we can prohibit unnecessary wording.

# Implement calculate_progress function
def calculate_progress():
    global tasks, completed_tasks

    total_tasks = len(tasks) + len(completed_tasks)
    if total_tasks == 0:
        return 0.0

    # Was going to do whole thing about pulling what was true or false in the list but decided to just refer to completed list
    progress = (len(completed_tasks) / total_tasks) * 100 # We will use the calculation of completed/total * 100 to get percentage
    return float(progress)

# print(calculate_progress())