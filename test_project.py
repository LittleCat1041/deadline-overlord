import pytest
from project import add_item, complete_item, filter_items, format_priority
from datetime import datetime, timedelta

def test_add_item():
    items = []
    add_item(items, "Test Task", "2025-07-01 12:00", "@work", "High")
    assert len(items) == 1
    assert items[0]["name"] == "Test Task"
    assert items[0]["done"] is False

def test_complete_item():
    items = [{"name": "Test_Task1", "done": False, "due": None, "tag": None, "priority": None}]
    result1 = complete_item(items, "test_task1")
    assert result1 is True
    assert items[0]["done"] is True

    result2 = complete_item(items, "nonexistent")
    assert result2 is False

def test_filter_items():
    items = [
        {"name": "Task1", "done": False, "due": None, "tag": "@home", "priority": "Low"},
        {"name": "Task2", "done": True, "due": None, "tag": "@work", "priority": "High"},
        {"name": "Task3", "done": False, "due": None, "tag": "@work", "priority": "Medium"}]

    filtered1 = filter_items(items, tag="@work")
    assert len(filtered1) == 2

    filtered2 = filter_items(items, status="done")
    assert len(filtered2) == 1

    filtered3 = filter_items(items, priority="low")
    assert len(filtered3) == 1

def test_format_priority():
    assert format_priority("High") == "🔴 High"
    assert format_priority("Medium") == "🟡 Medium"
    assert format_priority("Low") == "🟢 Low"
    assert format_priority(None) == "-"
    assert format_priority("Unknown") == "-"
    assert format_priority("") == "-"

def test_filter_case_insensitivity():
    items = [{"name": "Task", "done": False, "due": None, "tag": "@Work", "priority": "HIGH"}]
    result = filter_items(items, tag="@work", priority="high")
    assert len(result) == 1

def test_filter_overdue():
    overdue_time = (datetime.now() - timedelta(hours=1)).strftime("%Y-%m-%d %H:%M")
    items = [{"name": "Late Task", "done": False, "due": overdue_time, "tag": None, "priority": None}]
    result = filter_items(items, status="overdue")
    assert len(result) == 1
    assert result[0]["name"] == "Late Task"

