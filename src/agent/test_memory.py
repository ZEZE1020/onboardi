import os
import json
import tempfile
import pytest
from agent.memory import load_memory, save_memory, MEMORY_PATH

@pytest.fixture(autouse=True)
def temp_memory_path(monkeypatch, tmp_path):
    fake = tmp_path / "mem.json"
    monkeypatch.setenv("AGENT_MEMORY_PATH", str(fake))
    return fake

def test_memory_roundtrip(temp_memory_path):
    data = {"foo": "bar", "num": 123}
    save_memory(data)
    assert temp_memory_path.exists()
    loaded = load_memory()
    assert loaded == data

def test_load_nonexistent_returns_empty(temp_memory_path):
    # File does not exist yet
    if temp_memory_path.exists(): 
        temp_memory_path.unlink()
    assert load_memory() == {}
