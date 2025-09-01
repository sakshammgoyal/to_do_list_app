import tkinter as tk
from tkinter import messagebox

# File to store tasks
TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            for task in f.readlines():
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass  # If file doesn't exist, start fresh

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as f:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

# Add a new task
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Delete selected task
def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# GUI setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.configure(bg="#f2f2f2")

# Entry field
task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", font=("Arial", 12), bg="#4CAF50", fg="white", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", font=("Arial", 12), bg="#f44336", fg="white", command=delete_task)
delete_button.pack(pady=5)

# Task list
task_listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
task_listbox.pack(pady=10)

# Load tasks at startup
load_tasks()

# Run GUI
root.mainloop()
