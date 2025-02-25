import unittest
import To-DoListManager

def add_your_list(todoList, task):
    try:
        todoList.append({"task": task, "status": "[ ]"})
        return "Task added!"
    except Exception:
        return "Error adding task."

def view_your_task(todoList):
    return [f"{idx+1}. {task['status']} {task['task']}" for idx, task in enumerate(todoList)]


def delete_task(todoList, task_number):
    if 0 < task_number <= len(todoList):
        del todoList[task_number-1]
        return "Task deleted!"
    return "Invalid task number."

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todoList = []
    
    def test_add_your_list(self):
        result = add_your_list(self.todoList, "Buy groceries")
        self.assertEqual(result, "Task added!")
        self.assertEqual(len(self.todoList), 1)
    
    def test_view_your_task(self):
        add_your_list(self.todoList, "Buy groceries")
        self.assertEqual(view_your_task(self.todoList), ["1. [ ] Buy groceries"])
    
    def test_mark_task_complete(self):
        add_your_list(self.todoList, "Buy groceries")
        result = mark_task_complete(self.todoList, 1)
        self.assertEqual(result, "Task marked as complete!")
        self.assertEqual(self.todoList[0]["status"], "[X]")
    
    def test_delete_task(self):
        add_your_list(self.todoList, "Buy groceries")
        result = delete_task(self.todoList, 1)
        self.assertEqual(result, "Task deleted!")
        self.assertEqual(len(self.todoList), 0)
    
    def test_invalid_mark_complete(self):
        result = mark_task_complete(self.todoList, 1)
        self.assertEqual(result, "Invalid task number.")
    
    def test_invalid_delete_task(self):
        result = delete_task(self.todoList, 1)
        self.assertEqual(result, "Invalid task number.")

if __name__ == "__main__":
    unittest.main()
