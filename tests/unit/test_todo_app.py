"""
Unit tests for the TodoApp class.
This module tests the TodoApp functionality.
"""
import unittest
from src.todo_app import TodoApp


class TestTodoApp(unittest.TestCase):
    """
    Test cases for the TodoApp class.
    """
    
    def setUp(self):
        """
        Set up a fresh TodoApp instance for each test.
        """
        self.app = TodoApp()
    
    def test_initial_state(self):
        """
        Test that TodoApp initializes with empty tasks and next_id of 1.
        """
        self.assertEqual(len(self.app.tasks), 0)
        self.assertEqual(self.app.next_id, 1)
    
    def test_add_task_success(self):
        """
        Test adding a valid task.
        """
        result = self.app.add_task("Test Task")
        
        self.assertEqual(len(self.app.tasks), 1)
        self.assertEqual(self.app.tasks[0].title, "Test Task")
        self.assertEqual(self.app.tasks[0].id, 1)
        self.assertEqual(self.app.next_id, 2)
        self.assertIn("Task 'Test Task' added successfully", result)
    
    def test_add_task_empty_title(self):
        """
        Test adding a task with an empty title.
        """
        result = self.app.add_task("")
        
        self.assertEqual(len(self.app.tasks), 0)
        self.assertIn("Error: Task title cannot be empty", result)
    
    def test_add_task_whitespace_title(self):
        """
        Test adding a task with a whitespace-only title.
        """
        result = self.app.add_task("   ")
        
        self.assertEqual(len(self.app.tasks), 0)
        self.assertIn("Error: Task title cannot be empty", result)
    
    def test_view_tasks_empty_list(self):
        """
        Test viewing tasks when the list is empty.
        """
        result = self.app.view_tasks()
        
        self.assertIn("Your task list is empty", result)
    
    def test_view_tasks_with_tasks(self):
        """
        Test viewing tasks when the list has tasks.
        """
        self.app.add_task("First Task")
        self.app.add_task("Second Task")
        
        result = self.app.view_tasks()
        
        self.assertIn("First Task", result)
        self.assertIn("Second Task", result)
        self.assertIn("ID", result)
        self.assertIn("Status", result)
        self.assertIn("Title", result)
    
    def test_update_task_success(self):
        """
        Test updating a task with a valid ID and new title.
        """
        self.app.add_task("Original Task")
        task_id = self.app.tasks[0].id
        
        result = self.app.update_task(task_id, "Updated Task")
        
        self.assertEqual(self.app.tasks[0].title, "Updated Task")
        self.assertIn("updated from 'Original Task' to 'Updated Task'", result)
    
    def test_update_task_invalid_id(self):
        """
        Test updating a task with an invalid ID.
        """
        self.app.add_task("Original Task")
        
        result = self.app.update_task(999, "Updated Task")
        
        self.assertIn("does not exist", result)
    
    def test_update_task_empty_title(self):
        """
        Test updating a task with an empty title.
        """
        self.app.add_task("Original Task")
        task_id = self.app.tasks[0].id
        
        result = self.app.update_task(task_id, "")
        
        self.assertIn("Error: Task title cannot be empty", result)
    
    def test_delete_task_success(self):
        """
        Test deleting a task with a valid ID.
        """
        self.app.add_task("Task to Delete")
        task_id = self.app.tasks[0].id
        
        result = self.app.delete_task(task_id)
        
        self.assertEqual(len(self.app.tasks), 0)
        self.assertIn("deleted successfully", result)
    
    def test_delete_task_invalid_id(self):
        """
        Test deleting a task with an invalid ID.
        """
        self.app.add_task("Existing Task")
        
        result = self.app.delete_task(999)
        
        self.assertEqual(len(self.app.tasks), 1)
        self.assertIn("does not exist", result)
    
    def test_mark_task_complete_success(self):
        """
        Test marking a task as complete with a valid ID.
        """
        self.app.add_task("Task to Complete")
        task_id = self.app.tasks[0].id
        
        result = self.app.mark_task_complete(task_id)
        
        self.assertTrue(self.app.tasks[0].completed)
        self.assertIn("marked as complete", result)
    
    def test_mark_task_complete_already_completed(self):
        """
        Test marking a task that is already completed.
        """
        self.app.add_task("Completed Task")
        task_id = self.app.tasks[0].id
        self.app.mark_task_complete(task_id)  # Mark as complete first
        
        result = self.app.mark_task_complete(task_id)  # Try to mark again
        
        self.assertIn("already marked as complete", result)
    
    def test_mark_task_complete_invalid_id(self):
        """
        Test marking a task as complete with an invalid ID.
        """
        self.app.add_task("Existing Task")
        
        result = self.app.mark_task_complete(999)
        
        self.assertFalse(self.app.tasks[0].completed)
        self.assertIn("does not exist", result)


if __name__ == '__main__':
    unittest.main()