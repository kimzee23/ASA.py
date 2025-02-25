
def display_menu():
	print("\n Semicolon To-do list")
	print("1. Add a task")
	print("2. View all task")
	print("3. Mark a task as complete")
	print("4. Delete a task")
	print("5. Exit: \U0001F600")

def add_your_list(todoList, tasks):

    try:
        todoList.append({ "tasks": tasks, "status": "[ ]" })
        return "Task added!"
    except ValueError:
        return "Invalid Time or Date entered . Please enter a number."


def view_your_task(todoList ):
    for item,  task  in enumerate(todoList ):
        print(f"{item+1}. { todoList ['status']} { todoList ['task']}")

def mark_task_complete(todoList):
    if 0 < task_number <= len(tasks):
        tasks[task_number-1]["status"] = "[X]"

def delete_task(task_number):
    if 0 < task_number <= len(todoList):
        tasks.pop(task_number-1)



def main_test():
    todoList = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            task = input("Enter your task: ")
            time = input("Enter Time: ")
            print(add_your_list(todoList, task ))
        elif choice == "2":
            print(view_your_task(todoList )) 
        elif choice == "3":
            task_number = int(input("Enter task number to mark as complete: "))
            mark_task_complete(task_number)
            print("Task marked as complete!")

        elif choice == "4":
            print("   ")
        elif choice == "5":
            print("<<<<<Exiting the To-do list app>>>>>")
            break
        else:
            print("Invalid Input. Please try again.")
if __name__ == "__main__":
   	main_test()
