📘 To-Do List CLI App
A simple and lightweight Command Line Interface (CLI) To-Do list application built with Python. It allows you to manage your tasks—add, view, complete, and delete—all from the terminal. Tasks are stored persistently using a JSON file.

✨ Features
✅ Add new tasks

📋 View all tasks with status

✔️ Mark tasks as completed

🗑️ Delete tasks

💾 Tasks are saved automatically in tasks.json

🐍 Built entirely in Python with no external dependencies

📦 Requirements
Python 3.x

Git (for version control)

🚀 Getting Started
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/Bhavesh7-code/todo-cli-app.git
cd todo-cli-app
2. Run the script using Python
bash
Copy
Edit
python todo.py <command> [arguments]
🛠️ Available Commands
Command	Description	Example
add	Add a new task	python todo.py add "Buy groceries"
view	View all tasks	python todo.py view
complete	Mark a task as completed (by number)	python todo.py complete 1
delete	Delete a task (by number)	python todo.py delete 1

📂 Project Structure
bash
Copy
Edit
todo-cli-app/
├── todo.py         # Main CLI application
├── tasks.json      # Task storage (auto-generated)
└── README.md       # Project documentation
📸 Example Output
bash
Copy
Edit
$ python todo.py view
📋 Your Tasks:
1. Buy groceries [❌]
2. Finish assignment [✅]