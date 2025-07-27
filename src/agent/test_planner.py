import pytest
from agent.planner import plan

def test_plan_splits_on_and():
    tasks = plan("one and two and three")
    assert tasks == ["one", "two", "three"]

def test_plan_trims_whitespace():
    tasks = plan("  task1  and   task2 ")
    assert tasks == ["task1", "task2"]

def test_plan_single_task_if_no_and():
    tasks = plan("do something")
    assert tasks == ["do something"]

def test_plan_empty_and_whitespace():
    assert plan("") == []
    assert plan("   ") == []
