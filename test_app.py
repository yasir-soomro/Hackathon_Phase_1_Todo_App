"""
Simple test script to verify the Todo App functionality.
"""
from src.todo_app import TodoApp


def test_app():
    """
    Test the basic functionality of the Todo App.
    """
    app = TodoApp()
    
    print("Testing Todo App functionality...")
    
    # Test adding a task
    result = app.add_task("Test task 1")
    print(f"Add task: {result}")
    
    # Test viewing tasks
    result = app.view_tasks()
    print(f"View tasks:\n{result}")
    
    # Test updating a task
    task_id = app.tasks[0].id
    result = app.update_task(task_id, "Updated test task")
    print(f"Update task: {result}")
    
    # Test marking as complete
    result = app.mark_task_complete(task_id)
    print(f"Mark complete: {result}")
    
    # Test viewing tasks again
    result = app.view_tasks()
    print(f"View tasks after marking complete:\n{result}")
    
    # Test deleting a task
    result = app.delete_task(task_id)
    print(f"Delete task: {result}")
    
    # Test viewing tasks after deletion
    result = app.view_tasks()
    print(f"View tasks after deletion:\n{result}")
    
    print("All tests passed!")


if __name__ == "__main__":
    test_app()