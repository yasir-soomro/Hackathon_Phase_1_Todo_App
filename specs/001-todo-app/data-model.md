# Data Model: Python Todo App

## Task Entity

**Definition**: Represents a single todo item in the application

**Properties**:
- `id` (integer): Unique identifier for the task
- `title` (string): The description of the task
- `completed` (boolean): Status indicating whether the task is completed

**Validation Rules**:
- `id` must be a positive integer
- `title` must be a non-empty string
- `completed` must be a boolean value (default: false)

**State Transitions**:
- `pending` → `completed`: When user marks task as complete
- `completed` → `pending`: When user marks task as incomplete (if this feature is implemented)

## TodoList Entity

**Definition**: Represents the collection of tasks in the application

**Properties**:
- `tasks` (list of Task objects): The collection of tasks
- `next_id` (integer): The next available ID for new tasks

**Validation Rules**:
- `tasks` must be a list containing only Task objects
- Each task in the list must have a unique ID
- `next_id` must be greater than the highest existing task ID

**State Transitions**:
- Task added to list: When user adds a new task
- Task removed from list: When user deletes a task
- Task updated in list: When user updates a task title or completion status