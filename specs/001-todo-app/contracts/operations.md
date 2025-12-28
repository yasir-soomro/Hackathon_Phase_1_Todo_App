# API Contracts: Python Todo App

Since this is a console application with in-memory operations, traditional API contracts don't apply. Instead, we define the interface contracts for the core operations:

## Core Operations Interface

### Add Task
- **Input**: Task title (string)
- **Output**: Success message with new task ID or error message
- **Preconditions**: Title is not empty
- **Postconditions**: New task added to the list with pending status
- **Side effects**: Task list updated, next_id incremented

### View Task List
- **Input**: None
- **Output**: Formatted list of all tasks with ID, title, and completion status
- **Preconditions**: None
- **Postconditions**: Task list displayed to user
- **Side effects**: None

### Update Task
- **Input**: Task ID (integer), new title (string)
- **Output**: Success message or error message
- **Preconditions**: Task with given ID exists, new title is not empty
- **Postconditions**: Task title updated in the list
- **Side effects**: Task list updated

### Delete Task
- **Input**: Task ID (integer)
- **Output**: Success message or error message
- **Preconditions**: Task with given ID exists
- **Postconditions**: Task removed from the list
- **Side effects**: Task list updated

### Mark Task as Complete
- **Input**: Task ID (integer)
- **Output**: Success message or error message
- **Preconditions**: Task with given ID exists
- **Postconditions**: Task completion status set to true
- **Side effects**: Task list updated