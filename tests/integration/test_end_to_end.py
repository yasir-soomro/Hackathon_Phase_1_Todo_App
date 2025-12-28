"""
Integration tests for complete user workflows.
This module tests end-to-end user workflows in the Todo application.
"""
import unittest
import sys
from io import StringIO
from unittest.mock import patch
from src.todo_app import TodoApp


class TestEndToEnd(unittest.TestCase):
    """
    Test cases for complete user workflows.
    """
    
    def setUp(self):
        """
        Set up a fresh TodoApp instance for each test.
        """
        self.app = TodoApp()
    
    def test_complete_workflow(self):
        """
        Test a complete workflow: add, view, update, mark complete, delete.
        """
        # Add a task
        result = self.app.add_task("Complete workflow test")
        self.assertIn("added successfully", result)
        
        # View tasks
        result = self.app.view_tasks()
        self.assertIn("Complete workflow test", result)
        self.assertIn("○", result)  # Check for pending indicator
        
        # Update the task
        task_id = self.app.tasks[0].id
        result = self.app.update_task(task_id, "Updated workflow test")
        self.assertIn("updated from", result)
        
        # Mark as complete
        result = self.app.mark_task_complete(task_id)
        self.assertIn("marked as complete", result)
        
        # View tasks again to confirm completion
        result = self.app.view_tasks()
        self.assertIn("Updated workflow test", result)
        self.assertIn("✓", result)  # Check for completion indicator
        
        # Delete the task
        result = self.app.delete_task(task_id)
        self.assertIn("deleted successfully", result)
        
        # Verify task list is empty
        result = self.app.view_tasks()
        self.assertIn("empty", result)
    
    def test_multiple_tasks_workflow(self):
        """
        Test workflow with multiple tasks.
        """
        # Add multiple tasks
        result1 = self.app.add_task("First task")
        result2 = self.app.add_task("Second task")
        result3 = self.app.add_task("Third task")
        
        self.assertIn("added successfully", result1)
        self.assertIn("added successfully", result2)
        self.assertIn("added successfully", result3)
        
        # View all tasks
        result = self.app.view_tasks()
        self.assertIn("First task", result)
        self.assertIn("Second task", result)
        self.assertIn("Third task", result)
        self.assertEqual(len(self.app.tasks), 3)
        
        # Mark second task as complete
        second_task_id = self.app.tasks[1].id
        result = self.app.mark_task_complete(second_task_id)
        self.assertIn("marked as complete", result)
        
        # View tasks to confirm one is complete
        result = self.app.view_tasks()
        self.assertEqual(result.count("✓"), 1)  # One task should be marked complete
        self.assertEqual(result.count("○"), 2)  # Two tasks should be pending
        
        # Update the first task
        first_task_id = self.app.tasks[0].id
        result = self.app.update_task(first_task_id, "Updated first task")
        self.assertIn("updated from", result)
        
        # Delete the third task
        third_task_id = self.app.tasks[2].id
        result = self.app.delete_task(third_task_id)
        self.assertIn("deleted successfully", result)
        
        # Verify only 2 tasks remain
        self.assertEqual(len(self.app.tasks), 2)
    
    def test_error_handling_workflow(self):
        """
        Test that error handling works correctly.
        """
        # Try to update a non-existent task
        result = self.app.update_task(999, "Non-existent task")
        self.assertIn("does not exist", result)

        # Try to delete a non-existent task
        result = self.app.delete_task(999)
        self.assertIn("does not exist", result)

        # Try to mark complete a non-existent task
        result = self.app.mark_task_complete(999)
        self.assertIn("does not exist", result)
        
        # Try to add an empty task
        result = self.app.add_task("")
        self.assertIn("Error: Task title cannot be empty", result)
        
        # Verify no tasks were added
        self.assertEqual(len(self.app.tasks), 0)


if __name__ == '__main__':
    unittest.main()