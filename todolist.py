"""
This is way out of my expertise, but I am going to try to learn how to do this anyways!

My goal is to create a simple todo list that runs on a while loop.

Step 1: Understanding the fundamentals of the program
1. Show a menu with options such as add, remove, view, and exit
2. Let the user pick an option from the list by typing a number.
3. If the user wants to add a task, ask them for the task and save it. If they want to remove, show list.

Step 2: Store and Manage Tasks
1. Since tasks are multiple items, we should use a collection to store them. The best option is probably a list.
2. Lets think of a list as a notebook.

Step 3: Use a loop to keep it running
1. The program shouldnt stop after one action.
2. Lets use a loop to keep it running until the user chooses to exit the program.
3. The loop should take the user back to the menu.

Step 4: Handling input and making it interactive for the user
1. Ask the user what they want to do
2. If they enter something invalid, show an error and ask again.
3. Make sure the program doesnt crash if they remove something that doesnt exist!!

Step 5: Bonus features that I can add.
1. Save tasks to a file
2. Adding timestamps
3. Allowing marking tasks as done instead of simply deleting them
"""

# Step 1: Understanding the fundamentals of the program
menu = {
    1: "add",
    2: "remove",
    3: "list",
    4: "exit"
}

user_input = int(input("Please input where you would like to go: "))
action = menu.get(user_input, "Invalid")
print(f"You have chosen to: {action}")

# Step 2: Store and Manage Tasks
# Step 3: Use a loop to keep it running
# Step 4: Handling input and making it interactive
# Bonus stuff