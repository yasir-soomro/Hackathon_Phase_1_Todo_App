"""
Main entry point for the Python Todo App.
This module contains the main menu system and user interaction logic.
"""
import sys
from todo_app import TodoApp


def main():
    """
    Main function to run the Todo App.
    Displays menu and handles user input.
    """
    app = TodoApp()
    
    while True:
        print("\n" + "="*40)
        print("           PYTHON TODO APP")
        print("="*40)
        print("1. Add Task")
        print("2. View Task List")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Exit")
        print("-"*40)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            title = input("Enter task title: ").strip()
            result = app.add_task(title)
            print(result)
        elif choice == '2':
            tasks = app.view_tasks()
            print(tasks)
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to update: "))
                new_title = input("Enter new title: ").strip()
                result = app.update_task(task_id, new_title)
                print(result)
            except ValueError:
                print("Invalid task ID. Please enter a number.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to delete: "))
                result = app.delete_task(task_id)
                print(result)
            except ValueError:
                print("Invalid task ID. Please enter a number.")
        elif choice == '5':
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                result = app.mark_task_complete(task_id)
                print(result)
            except ValueError:
                print("Invalid task ID. Please enter a number.")
        elif choice == '6':
            print("Thank you for using Python Todo App. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1-6.")
        
        # Display updated task list after each operation
        print("\nCurrent Task List:")
        print(app.view_tasks())


if __name__ == "__main__":
    main()