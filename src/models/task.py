"""
Task model definition.
This module defines the Task entity with its properties and validation.
"""


class Task:
    """
    Represents a single todo item in the application.

    Attributes:
        id (int): Unique identifier for the task
        title (str): The description of the task
        completed (bool): Status indicating whether the task is completed
    """

    def __init__(self, task_id, title, completed=False):
        """
        Initialize a Task instance.

        Args:
            task_id (int): Unique identifier for the task
            title (str): The description of the task
            completed (bool): Status indicating whether the task is completed (default: False)
        """
        self.id = task_id
        self.title = title
        self.completed = completed

    @property
    def title(self):
        """Get the task title."""
        return self._title

    @title.setter
    def title(self, value):
        """Set the task title with validation."""
        if not value or not value.strip():
            raise ValueError("Task title cannot be empty")
        if len(value.strip()) > 200:  # Reasonable length limit
            raise ValueError("Task title cannot exceed 200 characters")
        self._title = value.strip()

    def __str__(self):
        """
        String representation of the Task.

        Returns:
            str: Formatted string representation of the task
        """
        status = "Completed" if self.completed else "Pending"
        return f"Task {self.id}: {self.title} [{status}]"

    def __repr__(self):
        """
        Developer-friendly representation of the Task.

        Returns:
            str: Detailed representation of the task
        """
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"