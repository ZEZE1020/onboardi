from typing import List

def plan(goal: str) -> List[str]:
    """
    Break a goal string into a list of subtasks.
    If the goal is empty or whitespace, returns an empty list.
    """
    if not goal or not goal.strip():
        return []

    # Simple split on " and " for now; can replace with LLM logic later
    tasks = [task.strip() for task in goal.split(" and ") if task.strip()]
    return tasks or [goal.strip()]
