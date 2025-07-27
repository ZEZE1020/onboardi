# src/agent/memory.py

import json
import os
from typing import Any, Dict

def _get_memory_path() -> str:
    """
    Determine current memory file path, allowing overrides via env var.
    """
    default = os.path.expanduser("~/.onboardi_memory.json")
    return os.getenv("AGENT_MEMORY_PATH", default)

def load_memory() -> Dict[str, Any]:
    """
    Load memory from disk. Returns empty dict if file doesn't exist.
    """
    path = _get_memory_path()
    if not os.path.isfile(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(data: Dict[str, Any]) -> None:
    """
    Save memory dict to disk (overwrites).
    """
    path = _get_memory_path()
    directory = os.path.dirname(path) or "."
    os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
