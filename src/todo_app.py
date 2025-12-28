"""
Core TodoApp class with all operations.
This module handles all business logic for the Todo application.
"""
import sys
import os
# Add the src directory to the path so we can import from models and utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.task import Task
from utils.validators import validate_task_title, validate_task_id


class TodoApp:
    """
    Main application class that manages all todo tasks.
    Stores tasks in memory using Python data structures.
    """
    
    def __init__(self):
        """
        Initialize the TodoApp with an empty task list and next ID counter.
        """
        self.tasks = []
        self.next_id = 1
    
    def add_task(self, title):
        """
        Add a new task to the list.

        Args:
            title (str): The title of the task

        Returns:
            str: Success or error message
        """
        # Validate the title
        is_valid, error_msg = validate_task_title(title)
        if not is_valid:
            return error_msg

        # Create a new task
        task = Task(task_id=self.next_id, title=title, completed=False)
        self.tasks.append(task)

        # Increment the next ID
        self.next_id += 1

        return f"Task '{title}' added successfully with ID {task.id}."
    
    def view_tasks(self):
        """
        Display all tasks with their titles and completion status.
        
        Returns:
            str: Formatted list of tasks or message if empty
        """
        if not self.tasks:
            return "Your task list is empty. Add some tasks!"
        
        result = "Your Tasks:\n"
        result += "-" * 50 + "\n"
        result += f"{'ID':<4} {'Status':<8} {'Title':<30}\n"
        result += "-" * 50 + "\n"
        
        for task in self.tasks:
            status = "✓" if task.completed else "○"
            result += f"{task.id:<4} {status:<8} {task.title:<30}\n"
        
        return result
    
    def update_task(self, task_id, new_title):
        """
        Update the title of an existing task.
        
        Args:
            task_id (int): The ID of the task to update
            new_title (str): The new title for the task
            
        Returns:
            str: Success or error message
        """
        # Validate the task ID
        is_valid, error_msg = validate_task_id(task_id, self.tasks)
        if not is_valid:
            return error_msg
        
        # Validate the new title
        is_valid, error_msg = validate_task_title(new_title)
        if not is_valid:
            return error_msg
        
        # Find and update the task
        for task in self.tasks:
            if task.id == task_id:
                old_title = task.title
                task.title = new_title
                return f"Task ID {task_id} updated from '{old_title}' to '{new_title}'."
        
        return f"Task with ID {task_id} not found."
    
    def delete_task(self, task_id):
        """
        Delete a task by its ID.
        
        Args:
            task_id (int): The ID of the task to delete
            
        Returns:
            str: Success or error message
        """
        # Validate the task ID
        is_valid, error_msg = validate_task_id(task_id, self.tasks)
        if not is_valid:
            return error_msg
        
        # Find and remove the task
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                deleted_title = task.title
                self.tasks.pop(i)
                return f"Task '{deleted_title}' (ID {task_id}) deleted successfully."
        
        return f"Task with ID {task_id} not found."
    
    def mark_task_complete(self, task_id):
        """
        Mark a task as complete by its ID.
        
        Args:
            task_id (int): The ID of the task to mark as complete
            
        Returns:
            str: Success or error message
        """
        # Validate the task ID
        is_valid, error_msg = validate_task_id(task_id, self.tasks)
        if not is_valid:
            return error_msg
        
        # Find and update the task status
        for task in self.tasks:
            if task.id == task_id:
                if task.completed:
                    return f"Task '{task.title}' (ID {task_id}) is already marked as complete."
                else:
                    task.completed = True
                    return f"Task '{task.title}' (ID {task_id}) marked as complete."
        
        return f"Task with ID {task_id} not found."