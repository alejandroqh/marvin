"""Memory management for Marvin"""

from pathlib import Path
from config import MEMORY_FILE


def load_memory():
    """Load memory from marvin.mem file"""
    memory_path = Path(MEMORY_FILE)
    if memory_path.exists():
        with open(memory_path, 'r') as f:
            return f.read()
    return ""


def add_thought(thought):
    """Add a thought to the memory file"""
    memory_path = Path(MEMORY_FILE)
    with open(memory_path, 'a') as f:
        f.write(f"\n{thought}\n")


def remove_thought(thought_text):
    """Remove a specific thought from the memory file"""
    memory_path = Path(MEMORY_FILE)
    if memory_path.exists():
        with open(memory_path, 'r') as f:
            content = f.read()

        # Remove the thought
        updated_content = content.replace(thought_text, "")

        with open(memory_path, 'w') as f:
            f.write(updated_content)
