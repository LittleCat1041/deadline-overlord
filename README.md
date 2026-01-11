# Deadline Overlord

A powerful Command-Line Interface (CLI) Task Manager built with **Python**, featuring a beautiful terminal UI powered by the **Rich** library. This project focuses on efficient task tracking, data persistence, and clean code architecture.

## Video Demo

*(Click the link below to watch the project demonstration)*

[**▶️ Watch the Demo Video Here**](https://youtu.be/eh_n842N5tM)

---

## ✨ Key Features

* **🎨 Rich Terminal UI:** utilized the `rich` library to render color-coded tables and formatted text, making the CLI experience modern and readable.
* **💾 Data Persistence:** Automatically saves and loads tasks using **JSON** (`data.json`), ensuring data isn't lost when the program closes.
* **📊 Task Management Logic:**
    * **Priority System:** Categorize tasks by High/Medium/Low priority.
    * **Deadline Tracking:** Calculates and displays remaining time (Countdown) or Overdue status in real-time.
    * **Filtering:** Filter tasks by tags, priority, or completion status.
* **📤 Export Capability:** Convert your task list into a **CSV file** (`Events.csv`) for external use.
* **🧪 Unit Testing:** Core functions are fully tested using **pytest** to ensure reliability.

## 🛠️ Tech Stack

* **Language:** Python 3
* **Libraries:** `rich`, `pytest`
* **Data Storage:** JSON (Internal), CSV (Export)

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone [https://github.com/LittleCat1041/deadline-overlord.git](https://github.com/LittleCat1041/deadline-overlord.git)
cd deadline-overlord
