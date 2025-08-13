# 📝 To-Do List Program (Python)

## 📌 Description
This is a simple **Command-Line To-Do List** application built in Python.  
It allows the user to manage daily tasks by **viewing**, **adding**, and **removing** them.  
The program uses a **menu-driven approach**, runs in a continuous loop until the user chooses to exit,  
and handles empty list scenarios to avoid errors.

---

## 🖥 Technologies Used
- **Language:** Python 3
- **IDE:** Visual Studio Code (VS Code) / Any Python-supported editor
- **Libraries Used:** None (only Python built-ins)
- **Input Method:** `input()` function
- **Looping:** `while True` with `break` for exit
- **Data Type:** List to store tasks

---

## ✨ Features
- **View Tasks** – Displays all tasks with their index numbers or shows a message if the list is empty.  
- **Add Task** – Appends a new task to the list.  
- **Remove Task** – Removes a task by its index number (1-based indexing) with validation for invalid inputs.  
- **Exit Option** – Quits the program when the user chooses to exit.  
- **Error Handling** – Shows a message for invalid menu choices or wrong index numbers.

---

## 🛠 What I Did
- Created a **menu-driven program** using `while True` to run continuously until the user exits.  
- Used a **Python list** to store all tasks.  
- Implemented **empty list checks** before viewing or removing tasks.  
- Used list methods: `.append()` for adding and `.pop()` for removing tasks by index.  
- Added **user-friendly prompts** and messages for better interaction.  
- Tested the program in **VS Code** to ensure all options work smoothly.

---

## 🚀 How to Run
1. Save the file as `todo.py`.  
2. Open a terminal in VS Code or a command prompt in the file's folder.  
3. Run the script:
   ```bash
   python todo.py
