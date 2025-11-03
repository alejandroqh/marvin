"""Command processing for Marvin's self-directed commands"""

import re
import time
from memory import add_thought, load_memory, remove_thought


def process_memory_commands(text):
    """Process memory commands in Marvin's output (only outside <think> tags)
    Returns: rest_time (seconds to wait before next thought, or None for default)
    """
    # Remove <think> blocks from text before processing commands
    # Commands inside <think> tags are part of reasoning, not explicit commands
    text_without_thinking = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)

    rest_time = None

    # Check for [SAVE: ...] commands
    save_pattern = r'\[SAVE:\s*(.*?)\]'
    saves = re.findall(save_pattern, text_without_thinking, re.DOTALL)
    for save_text in saves:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        add_thought(f"[{timestamp}] INSIGHT: {save_text.strip()}")
        print(f"\n💾 Saved to memory: {save_text.strip()[:50]}...")

    # Check for [RECALL] command
    if '[RECALL]' in text_without_thinking:
        memory = load_memory()
        print(f"\n📖 Memory recalled ({len(memory)} chars)")
        print("─" * 60)
        print(memory[:500] + "..." if len(memory) > 500 else memory)
        print("─" * 60)

    # Check for [REMOVE: ...] commands
    remove_pattern = r'\[REMOVE:\s*(.*?)\]'
    removes = re.findall(remove_pattern, text_without_thinking, re.DOTALL)
    for remove_text in removes:
        remove_thought(remove_text.strip())
        print(f"\n🗑️  Removed from memory: {remove_text.strip()[:50]}...")

    # Check for [REST: N] command
    rest_pattern = r'\[REST:\s*(\d+)\]'
    rest_match = re.search(rest_pattern, text_without_thinking)
    if rest_match:
        rest_time = int(rest_match.group(1))
        print(f"\n⏸️  Rest interval changed to {rest_time} seconds")

    return rest_time
