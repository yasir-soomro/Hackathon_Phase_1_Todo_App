
# Hackathon Phase I - Python Todo App

🚀 **Phase I of Hackathon Todo App** – A lightweight, console-based task manager built in **Python** with **in-memory storage**. Designed to manage tasks efficiently while following the **Spec-Kit Plus methodology** for structured development.

---

## Features

- **Add Task** – Create new todo items
- **Delete Task** – Remove tasks from the list
- **Update Task** – Modify existing task details
- **View Task List** – Display all tasks with status
- **Mark as Complete** – Toggle task completion status

---

## Project Structure

Hackathon_Phase_1_Todo_App/
│
├── specs/
│ └── 001-todo-app/
│ ├── spec.md
│ ├── plan.md
│ ├── tasks.md
│ └── implementation.md
│
├── sp.constitution
├── specification
├── plan
├── tasks
├── sp.implementation
│
└── src/
├── app.py # Main console application
├── todo.py # In-memory CRUD operations
└── memory.py # Storage for tasks

yaml
Copy code

---

## Getting Started

### Prerequisites

- Python 3.9+
- (Optional) Virtual environment

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yasir-soomro/Hackathon_Phase_1_Todo_App.git
cd Hackathon_Phase_1_Todo_App
Create and activate a virtual environment (optional but recommended):

bash
Copy code
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux
Install dependencies (if any):

bash
Copy code
pip install -r requirements.txt
Note: This Phase I console app is pure Python and does not require external libraries.

Running the App
Run the console app:

bash
Copy code
python src/app.py
You will see a menu:

markdown
Copy code
PYTHON TODO APP
========================================
1. Add Task
2. View Task List
3. Update Task
4. Delete Task
5. Mark Task as Complete
6. Exit
Follow prompts to manage your tasks in-memory.

Example Usage
yaml
Copy code
Enter your choice (1-6): 1
Enter task title: Learn FastAPI
Task added successfully!

Enter your choice (1-6): 5
Enter task ID to mark as complete: 1
Task 'Learn FastAPI' marked as complete.
Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

Future Enhancements
Add FastAPI endpoints for API-based Todo management

Persistent storage using SQLite/PostgreSQL

Web-based UI using FastAPI + React

Advanced features like task priorities and deadlines

License
This project is licensed under the MIT License.

🔗 GitHub Repository: https://github.com/yasir-soomro/Hackathon_Phase_1_Todo_App

yaml
Copy code

---

If you want, I can also **create a visually appealing version** with **badges (Python version, license, repo stars, etc.)** and a **short project summary at the top**, which looks **professional for GitHub**.  

Do you want me to do that?







