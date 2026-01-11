👑 Deadline Overlord

📽️ Video Demo: https://youtu.be/eh_n842N5tM

📃 Description:
**Deadline Overlord** is a command-line task management program designed to help users stay organized and on top of their deadlines, using colorful and readable output powered by the `rich` Python library. This project was created as the final submission for CS50 Python, with a focus on implementing a practical, testable, and well-structured Python application.

--------------------------------------------------------------------------------------------------

💡 Overview

The idea behind Deadline Overlord came from the need to have a simple yet visually pleasing terminal-based task manager. While many task apps exist, this one is made specifically for learners who want a tool that runs in the terminal, handles deadlines, and uses clean code that can be tested.

With this tool, you can add tasks or events with optional tags (e.g., `@home`, `@cs50`), assign priorities, and include due dates. You can then view all tasks in a color-coded table, filter them, export them, or mark them complete. Tasks are saved locally in a JSON file, so your data persists between runs.

--------------------------------------------------------------------------------------------------

📌 Features

- ✅ Add tasks with optional:
  - Tags (e.g. `@school`, `@cs50`)
  - Priority labels (`Low`, `Medium`, `High`)
  - Due dates
- 🎨 View tasks with color-coded formatting using `rich` library
- 🔍 Filter tasks by:
  - Tag
  - Priority
  - Status: `pending`, `done`, `overdue`
- 🗑️ Mark tasks as complete
- 💾 Automatically saves and loads your tasks from a local `data.json` file
- 📤 Export tasks to a .csv file
- 🧪 Includes `pytest` unit tests for all core functions

--------------------------------------------------------------------------------------------------

📁 Project Structure

- 📁 Files and Directories
     - `project.py`: This is the main file that contains all the program logic, including user interaction, data storage, task formatting, and display.
     - `test_project.py`: Contains unit tests for core functions such as `add_item`, `complete_item`, `filter_items`, and `format_priority`. These are executed using `pytest`.
     - `requirements.txt`: Lists external libraries required (`rich`, `pytest`) for setup.
     - `README.md`: The file you're reading now! It describes the project's purpose, structure, and usage.
     - `data.json`: A local file used to store user input and task data persistently (auto-created if not present).
     - `Events.csv`: A CSV file generated when exporting tasks. Automatically created upon first export.

--------------------------------------------------------------------------------------------------

⚙️ How It Works

When the user runs the program (`python project.py`), a menu appears with options such as `add`, `list`, `complete`, `filter`, `due`, `export`, or `quit`. Tasks can be input with a name and optional metadata (tag, priority, and due date in `YYYY-MM-DD HH:MM` format). The program calculates time left and uses `rich` to output colorful tables based on status and urgency.

Tasks are stored as a list of dictionaries and saved to `data.json` using `json.dump`. Upon startup, tasks are loaded using `json.load`. When due dates are present, the program calculates time remaining with `datetime` and uses basic math (divmod()) to split time into days, hours, and minutes.

--------------------------------------------------------------------------------------------------

✍️ Design Decisions

- CLI instead of GUI: Since this is a Python-based project and meant for a CS50 final, a terminal interface makes the most sense and ensures it’s portable and light.
- JSON over SQLite: JSON is simple for this level of task management, and easy to test and maintain.
- `rich` for styling: Adds visual clarity to command-line programs, making tasks easier to read and status more obvious.

--------------------------------------------------------------------------------------------------

✅ Testing

The file `test_project.py` includes tests for the most important functions. These ensure that core features like task creation, filtering, and marking tasks as complete work as expected. You can run tests with: pytest -v test_project.py

--------------------------------------------------------------------------------------------------

🚀 Getting Started

    1. Clone the project or download this files into your own computer.
    2. Install dependencies:
        - Run this code in terminal -> pip install -r requirements.txt
    3. Run the program:
        - Main program -> python project.py
        - Test program -> pytest -v test_project.py

--------------------------------------------------------------------------------------------------

💡 Future Ideas

While Deadline Overlord already provides core task management features, there are several possibilities for future enhancements that could make the program even more powerful:

- ⏰ Alarm Notifications
  Add support for real-time reminders or pop-up alerts when a task is approaching its due date (e.g., within 30 minutes or 1 hour).

- 📥 CSV Task Importing
  In addition to exporting tasks to CSV, users could be given the ability to import a CSV file containing tasks — useful for bulk uploads or migrating from another task manager.

- 🗑️ Task Deletion Feature
  Currently, tasks can be marked as complete, but cannot be deleted. A future improvement could include the ability to remove tasks permanently by name or ID.

--------------------------------------------------------------------------------------------------

🏁 Final Thoughts

Thank you for using Deadline Overlord👊
Deadline Overlord was built to be practical, readable, and fun to use — especially for those learning Python. It was a great exercise in building a modular Python app with real-world utility. Feel free to fork or modify it!

This project was submitted as the final project for Harvard’s CS50P course.

