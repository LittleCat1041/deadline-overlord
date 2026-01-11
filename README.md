# Deadline Overlord

A powerful Command-Line Interface (CLI) Task Manager built with **Python**, featuring a beautiful terminal UI powered by the **Rich** library. This project focuses on efficient task tracking, data persistence, and clean code architecture.

## Video Demo

*(Click the link below to watch the project demonstration)*

[**▶️ Watch the Demo Video Here**](https://youtu.be/eh_n842N5tM)

---

## Key Features

- **Rich Terminal UI:** utilized the `rich` library to render color-coded tables and formatted text, making the CLI experience modern and readable.
- **Data Persistence:** Automatically saves and loads tasks using **JSON** (`data.json`), ensuring data isn't lost when the program closes.
- **Task Management Logic:**
    * **Priority System:** Categorize tasks by High/Medium/Low priority.
    * **Deadline Tracking:** Calculates and displays remaining time (Countdown) or Overdue status in real-time.
    * **Filtering:** Filter tasks by tags, priority, or completion status.
- **Export Capability:** Convert your task list into a **CSV file** (`Events.csv`) for external use.
- **Unit Testing:** Core functions are fully tested using **pytest** to ensure reliability.

## Command Guide
Once the program is running, you can use the following commands:
- `add` - Create a new task (Name, Due Date, Tag, Priority).
- `list` - Show all tasks in a formatted table.
- `complete` - Mark a task as done.
- `filter` - Search tasks by specific criteria.
- `due` - Show tasks due today.
- `export` - Save tasks to a CSV file.
- `quit` - Exit the program.

## Tech Stack
 - Python, Rich Library, JSON/CSV

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/LittleCat1041/deadline-overlord.git
```
### 2. Install Dependencies
```bash
cd deadline-overlord
```
```bash
pip install -r requirements.txt
```
### 3. Run the Program
```bash
python project.py
```
### 4. Run Tests (Optional)
```bash
pytest test_project.py
```


