import json
import os
import argparse

TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a task
def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(f"✅ Task added: {description}")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    print("\n📋 Your Tasks:")
    for idx, task in enumerate(tasks, start=1):
        status = "✅" if task["completed"] else "❌"
        print(f"{idx}. {task['description']} [{status}]")

# Mark a task as completed
def complete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["completed"] = True
        save_tasks(tasks)
        print(f"✔️ Task marked as completed: {tasks[index - 1]['description']}")
    else:
        print("❌ Invalid task number.")

# Delete a task
def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Task deleted: {removed['description']}")
    else:
        print("❌ Invalid task number.")

# Main command line parser
def main():
    parser = argparse.ArgumentParser(description="📝 Simple To-Do List CLI App")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add = subparsers.add_parser("add", help="Add a new task")
    add.add_argument("description", type=str, help="Task description")

    # View command
    subparsers.add_parser("view", help="View all tasks")

    # Complete command
    complete = subparsers.add_parser("complete", help="Mark a task as completed")
    complete.add_argument("index", type=int, help="Task number to mark complete")

    # Delete command
    delete = subparsers.add_parser("delete", help="Delete a task")
    delete.add_argument("index", type=int, help="Task number to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "view":
        view_tasks()
    elif args.command == "complete":
        complete_task(args.index)
    elif args.command == "delete":
        delete_task(args.index)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
