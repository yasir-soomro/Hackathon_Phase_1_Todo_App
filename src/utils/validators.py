"""
Input validation utilities.
This module contains functions to validate user inputs.
"""


def validate_task_title(title):
    """
    Validate the task title.
    
    Args:
        title (str): The title to validate
        
    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    if not title or not title.strip():
        return False, "Error: Task title cannot be empty."
    
    if len(title.strip()) > 200:  # Reasonable length limit
        return False, "Error: Task title cannot exceed 200 characters."
    
    return True, ""


def validate_task_id(task_id, tasks):
    """
    Validate the task ID.
    
    Args:
        task_id (int): The ID to validate
        tasks (list): The list of existing tasks
        
    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    if task_id <= 0:
        return False, "Error: Task ID must be a positive integer."
    
    # Check if the task ID exists in the current task list
    if not any(task.id == task_id for task in tasks):
        return False, f"Error: Task with ID {task_id} does not exist."
    
    return True, ""