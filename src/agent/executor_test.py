import os
import pytest
from agent.executor import execute

pytestmark = pytest.mark.skipif(
    not os.getenv("GENAI_API_KEY"),
    reason="GENAI_API_KEY not set"
)

def test_execute_returns_nonempty_string():
    result = execute("Say hello", {})
    assert isinstance(result, str)
    assert result.strip() != ""

def test_execute_empty_task_raises():
    with pytest.raises(ValueError):
        execute("", {})
