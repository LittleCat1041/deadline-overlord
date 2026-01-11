from datetime import datetime, timedelta
import json
import csv
from rich.console import Console
from rich.table import Table
import os

DATA = "data.json"
console = Console()

def main():
    console.print("[bold green]Welcome to Deadline Overlord![/bold green]")
    items = load_items(DATA)

    while True:
        console.print("\n[bold yellow]Menu[/bold yellow]: add / list / complete / filter / due / export / quit")
        choice = input("What would you like to do?: ").strip().lower()

        if choice == "add":
            name = input("Event/Task name: ").strip()
            due_date = input("Due date (YYYY-MM-DD HH:MM) [optional]: ").strip()
            tag = input("Tag (e.g., @home, @work) [optional]: ").strip()
            priority = input("Priority (Low/Medium/High) [optional]: ").strip().capitalize()
            add_item(items, name, due_date or None, tag or None, priority or None)
            save_items(DATA, items)

        elif choice == "list":
            display_items(items)

        elif choice == "complete":
            name = input("Task/Event to complete: ").strip()

            if complete_item(items, name):
                console.print(f"✅ [green]Task/Event completed:[/green] {name}")
                save_items(DATA, items)
            else:
                console.print("❌ [red]Task/Event not found.[/red]")

        elif choice == "filter":
            tag = input("Filter by tag [press enter to skip]: ").strip()
            priority = input("Filter by priority [press enter to skip]: ").strip().capitalize()
            status = input("Filter by status (done, pending, overdue) [press enter to skip]: ").strip().lower()
            filtered = filter_items(items, tag or None, priority or None, status or None)
            display_items(filtered)

        elif choice == "due":
            display_due_today(items)

        elif choice == "export":
            export_to_csv(items, "Events.csv")

        elif choice == "quit":
            console.print("👋 [italic]Goodbye![/italic]")
            break
        else:
            console.print("[red]Invalid command.[/red]")

def get_timedelta(due_date_str):
    # คำนวณผลต่างเวลา (Delta) ระหว่างเวลาปัจจุบันและ Due Date เพื่อใช้ในการแสดงสถานะ Countdown หรือ Overdue
    due_date = parse_due_date(due_date_str)
    return due_date - datetime.now()

def parse_due_date(date_str):
    if date_str.endswith("24:00"):
        base = datetime.strptime(date_str[:10], "%Y-%m-%d")
        return base + timedelta(days=1)
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M")

def format_timedelta(delta):
    days = delta.days
    hours, remain = divmod(delta.seconds, 3600)
    minutes = remain // 60
    return f"{days}D:{hours}H:{minutes}M"

def format_priority(priority):
    if priority == "High":
        return "🔴 High"
    elif priority == "Medium":
        return "🟡 Medium"
    elif priority == "Low":
        return "🟢 Low"
    return "-"

def display_items(items):
    if not items:
        console.print("[dim]No tasks to show.[/dim]")
        return
    # ใช้ rich.table เพื่อสร้างตารางที่จัด Format อัตโนมัติ ช่วยให้อ่านข้อมูล Task/Priority ได้ง่ายกว่า Text ปกติ
    table = Table(title="Tasks and Events")
    table.add_column("Name", style="bold")
    table.add_column("Due In")
    table.add_column("Priority")
    table.add_column("Tag")
    table.add_column("Status")

    for item in items:
        due = item["due"]

        if item["done"]:
            status = "✅ Done"
            due_in = "-"

        elif due:
            delta = get_timedelta(due)
            due_in = "Overdue!" if delta.total_seconds() < 0 else format_timedelta(delta)
            status = "❗ Overdue" if delta.total_seconds() < 0 else "⏳ Pending"
        else:
            due_in = "-"
            status = "⏳ Pending"

        prio = format_priority(item.get("priority"))
        table.add_row(item["name"], due_in, prio, item.get("tag") or "-", status)

    console.print(table)

def display_due_today(items):
    today = datetime.now().date()
    today_items = [item for item in items if item["due"] and not item["done"] and datetime.strptime(item["due"], "%Y-%m-%d %H:%M").date() == today]
    if today_items:
        console.print("\n📆 [bold]Tasks due today:[/bold]")
        display_items(today_items)
    else:
        console.print("[dim]No tasks due today.[/dim]")

def filter_items(items, tag=None, priority=None, status=None):
    filtered = []
    for item in items:
        if tag and (item["tag"] or "").lower() != tag.lower():
            continue
        if priority and (item["priority"] or "").lower() != priority.lower():
            continue
        if status == "done" and not item["done"]:
            continue
        if status == "pending" and item["done"]:
            continue
        if status == "overdue" and (not item["due"] or get_timedelta(item["due"]).total_seconds() >= 0 or item["done"]):
            continue
        filtered.append(item)
    return filtered

def complete_item(items, name):
    for item in items:
        if item["name"].lower() == name.lower():
            item["done"] = True
            return True
    return False

def load_items(file_path):
    # เลือกใช้ JSON เพราะเป็น format มาตรฐาน น้ำหนักเบา และ map เข้ากับ Python Dictionary/List ได้ทันที
    try:
        with open(file_path) as f:
            return json.load(f)
    except FileNotFoundError:
        # สร้างไฟล์ใหม่ให้อัตโนมัติหากไม่พบไฟล์เดิม ป้องกันการ Crash
        save_items(file_path, [])
        return []

def add_item(items, name, due_date=None, tag=None, priority=None):
    if any(item["name"].lower() == name.lower() for item in items):
        console.print(f"[red]Task '{name}' already exists.[/red]")
        return
    item = {"name": name, "done": False, "due": due_date, "tag": tag, "priority": priority}
    items.append(item)
    return item

def save_items(file_path, items):
    # บันทึกข้อมูลสถานะล่าสุดลงไฟล์ทันทีที่มีการเปลี่ยนแปลง
    with open(file_path, 'w') as f:
        json.dump(items, f, indent=2)

def export_to_csv(items, filename):
    try:
        os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)

        with open(filename, 'w', newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "done", "due", "tag", "priority"])
            writer.writeheader()
            writer.writerows(items)

        console.print(f"📤 [blue]Exported to {filename}[/blue]")
    except Exception as e:
        console.print(f"[red]Failed to export CSV: {e}[/red]")

if __name__=="__main__":
    main()
