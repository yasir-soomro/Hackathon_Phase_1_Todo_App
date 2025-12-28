"""
Unit tests for the Task model.
This module tests the Task class functionality.
"""
import unittest
from src.models.task import Task


class TestTask(unittest.TestCase):
    """
    Test cases for the Task model.
    """
    
    def test_task_initialization(self):
        """
        Test that a Task is properly initialized with given parameters.
        """
        task = Task(task_id=1, title="Test Task", completed=False)
        
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.completed, False)
    
    def test_task_default_completion_status(self):
        """
        Test that a Task is initialized with completed=False by default.
        """
        task = Task(task_id=1, title="Test Task")
        
        self.assertEqual(task.completed, False)
    
    def test_task_str_representation(self):
        """
        Test the string representation of a Task.
        """
        task = Task(task_id=1, title="Test Task", completed=False)
        expected_str = "Task 1: Test Task [Pending]"
        
        self.assertEqual(str(task), expected_str)
    
    def test_task_completed_str_representation(self):
        """
        Test the string representation of a completed Task.
        """
        task = Task(task_id=1, title="Test Task", completed=True)
        expected_str = "Task 1: Test Task [Completed]"
        
        self.assertEqual(str(task), expected_str)
    
    def test_task_repr_representation(self):
        """
        Test the developer-friendly representation of a Task.
        """
        task = Task(task_id=1, title="Test Task", completed=False)
        expected_repr = "Task(id=1, title='Test Task', completed=False)"
        
        self.assertEqual(repr(task), expected_repr)


if __name__ == '__main__':
    unittest.main()