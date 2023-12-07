from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this; use this task reference for the below requirements
    # update lastActivity with the current datetime value
    # set the name, description, and due date (all must be provided)
    # due date must match one of the formats mentioned in str_to_datetime()
    # add the new task to the tasks list
    # output a message confirming the new task was added or if the addition was rejected due to missing data based on the prior checks
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # make sure any checks/conditions clearly display an appropriate message of what failed
    if not (name and description and due):
        print("Missing data (name, description, or due date)")
        return
    due_date = str_to_datetime(due)
    if due_date is None:
        print("Invalid due date format")
        return
    task['name'] = name
    task['description'] = description
    task['due'] = due_date
    task['lastActivity'] = datetime.now()
    tasks.append(task)
    print("New task added successfully")
    #PSK 10/08/2023
    save()
    """
    It begins by checking if the name, description, and due parameters are all provided. If any of them are missing (i.e., one or more is empty), it prints a message ("Missing data (name, description, or due date)") and returns without adding the task.

    It then attempts to convert the due string into a datetime object using a function called str_to_datetime. If the conversion is successful, it assigns the resulting datetime object to the due field of the task dictionary. If the conversion fails (returns None), it prints a message ("Invalid due date format") and returns without adding the task.

    If both the checks in steps 1 and 2 pass, it proceeds to update the task dictionary with the provided name, description, and the converted due datetime.

    It also updates the lastActivity field of the task dictionary with the current date and time using datetime.now().

    The updated task is then appended to a list called tasks.

    Finally, it prints a message ("New task added successfully") to confirm that the new task was added successfully, and it calls a save function (which is not defined in this code snippet but presumably saves the updated list of tasks).
    """

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # show the existing value of each property where the TODOs are marked in the text of the inputs below (replace the TODO related text with the found tasks's data)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index < 0 or index >= len(tasks):
        print("Invalid index. Task not found.")
        return
    task = tasks [index]
    print (f"Existing task data:")
    print (f"Name: {task['name']}")
    print (f"Description: {task['description']}")
    print (f"Due: {task['due']}")
    #PSK 10/08/2023

    name = input(f"What's the name of this task? (TODO name) \n").strip()
    desc = input(f"What's a brief descriptions of this task? (TODO description) \n").strip()
    due = input(f"When is this task due (format: m/d/y H:M:S) (TODO due) \n").strip()
    update_task(index, name=name, description=desc, due=due)
    """
    It checks if the provided index is within the valid range (between 0 and the length of the tasks list). If it's not a valid index, it prints "Invalid index. Task not found." and returns.

    If the index is valid, it retrieves the task at that index from the tasks list.

    It then displays the existing task data for name, description, and due.

    It prompts the user for new values for name, description, and due using input().

    It calls the update_task function with the updated values for the task at the given index.
    """

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    # update lastActivity with the current datetime value
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index < 0 or index >= len(tasks):
        print("Invalid index. Task not found.")
        return
    task = tasks[index]
    if name:
        task['name'] = name
    if description:
        task['description'] = description
    if due:
        task['due'] = due
    task['lastActivity'] = datetime.now()
    if name or description or due:
        print("Task updated successfully")
    else:
        print("Task was not updated. No changes provided.")
    #PSK 10/08/2023
    
    save()
    """It checks if the provided index is within the valid range (between 0 and the length of the tasks list). If it's not a valid index, it prints "Invalid index. Task not found." and returns.

    If the index is valid, it retrieves the task at that index from the tasks list.

    It updates the task's properties (name, description, and due) if new values are provided.

    It updates the lastActivity field with the current datetime.

    It checks if any of the task properties were updated. If so, it prints "Task updated successfully." If no changes were provided, it prints "Task was not updated. No changes provided."""

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # if it's not currently marked as done, record the current datetime as the value (don't just set it as true)
    # if it is currently done, print a message saying it's already been completed
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index < 0 or index >= len(tasks):
        print("Invalid index. Task not found.")
        return
    task = tasks[index]
    if task['done'] != False:
        print("Task is already marked as done.")
    else:
        # If it's not marked as done, record the current datetime as the value
        task['done'] = datetime.now()
        print("Task marked as done successfully.")
    #PSK 10/08/2023

    save()
    """
    It checks if the provided index is within the valid range (between 0 and the length of the tasks list). If it's not a valid index, it prints "Invalid index. Task not found." and returns.

    If the index is valid, it retrieves the task at that index from the tasks list.

    It checks if the done property is already present in the task. If it is, it prints "Task is already marked as done."

    If the task is not marked as done, it records the current datetime as the value of the done property.

    It prints "Task marked as done successfully."
"""

def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # utilize the given print statement when a task is found
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index < 0 or index >= len(tasks):
        print("Invalid index. Task not found.")
        return
    task = tasks[index]
    #PSK 10/08/2023

    print(f"""
        [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))
    """
    It checks if the provided index is within the valid range (between 0 and the length of the tasks list). If it's not a valid index, it prints "Invalid index. Task not found." and returns.

    If the index is valid, it retrieves the task at that index from the tasks list.

    It prints detailed information about the task, including its name, description, last activity, due date, and whether it is completed or not. The format of the output is formatted to be more readable.
    """

def delete_task(index):
    """ deletes a task from the tasks list by index """
    # delete/remove task from list by index
    # message should show if it was successful or not
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index < 0 or index >= len(tasks):
        print("Invalid index. Task not found.")
        return
    removed_task = tasks.pop(index)
    if removed_task:
        print("Task deleted successfully.")
    else:
        print("Task deletion failed.")
    #PSK 10/08/2023
    
    save()
    """
    It checks if the provided index is within the valid range (between 0 and the length of the tasks list). If it's not a valid index, it prints "Invalid index. Task not found." and returns.

    If the index is valid, it removes the task at that index using the pop method and stores the removed task in the removed_task variable.

    It checks if the removal was successful (i.e., if removed_task is not None). If it was successful, it prints "Task deleted successfully." If it was not successful, it prints "Task deletion failed."
    """

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    _tasks = [task for task in tasks if task['done'] is False] # <-- this is a placeholder to populate based on the above requirements
    list_tasks(_tasks)
    #PSK 10/08/2023

    """
    It creates a new list _tasks using a list comprehension to filter tasks from the tasks list where the done property is explicitly False.

    It passes the _tasks list to the list_tasks function to print the incomplete tasks.
    """

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than "now" and that are not complete (i.e., not done)
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    _tasks = [task for task in tasks if task['done'] is False and 'due' in task and task['due'] < datetime.now()] # <-- this is a placeholder to populate based on the above requirements
    list_tasks(_tasks)
    #PSK 10/08/2023

    """
    It creates a new list _tasks using a list comprehension to filter tasks from the tasks list based on the following conditions:

    The task should not be marked as done (task['done'] is False).
    The task should have a due property.
    The due property's value should be less than the current datetime (i.e., it's in the past).
    It passes the _tasks list to the list_tasks function to print the overdue tasks.
    """

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # get the days, hours, minutes, seconds between the due date and now
    # display the remaining time via print in a clear format showing X days, X hours, X minutes, X seconds (time components must be clearly separated)
    # example: 1 day, 0 hours, 0 minutes, 0 seconds remaining
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is overdue (clearly note that it's overdue, values should be positive)
    # example: 0 days, 2 hours, 5 minutes, 10 seconds overdue (note there's no negative values)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index < 0 or index >= len(tasks):
        print("Invalid index. Task not found.")
        return
    task = tasks[index]
    if 'due' not in task:
        print("Due date not set for this task.")
        return
    due_date = task['due']
    due_date = datetime.strptime(task['due'], '%Y-%m-%d %H:%M:%S')
    current_time = datetime.now()
    time_difference = due_date - current_time
    if time_difference.total_seconds() < 0:
        overdue = True
        time_difference = abs(time_difference)
    else:
        overdue = False
    days = time_difference.days
    seconds = time_difference.seconds
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    if not overdue:
        print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds remaining")
    else:
        print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds overdue")
    #PSK 10/08/2023
    
    """
    It checks if the provided index is within the valid range (between 0 and the length of the tasks list). If it's not a valid index, it prints "Invalid index. Task not found." and returns.
    It retrieves the task at the specified index from the tasks list.
    It checks if the task has a due property. If it doesn't, it prints "Due date not set for this task." and returns.
    It parses the due date into a datetime object and calculates the time difference between the due date and the current time.
    If the calculated time difference is negative, it indicates that the task is overdue, so it sets the overdue flag to True and takes the absolute value of the time difference.
    It calculates the number of days, hours, minutes, and seconds from the time difference.
    If the task is not overdue, it prints the time remaining in the format "X days, X hours, X minutes, X seconds remaining." If it's overdue, it prints the time overdue in the format "X days, X hours, X minutes, X seconds overdue."
    """

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()