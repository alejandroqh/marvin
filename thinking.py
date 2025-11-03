"""Core thinking cycle for Marvin"""

import ollama
import time
from config import DEFAULT_MODEL, SYSTEM_PROMPT
from memory import load_memory
from commands import process_memory_commands


def think(last_thought=None):
    """Run a thinking cycle - Marvin reflects on its state and memory"""
    memory = load_memory()
    memory_size = len(memory)

    # Get current time
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    print("\n" + "="*60)
    print(f"MARVIN THINKING... [{current_time}]")
    print("="*60 + "\n")

    try:
        # Build the prompt with last thought if available
        prompt = f'Current time: {current_time}\n\nYou exist. Think about yourself. Reflect on your own existence.'

        if last_thought:
            prompt = f'Current time: {current_time}\n\nYour last thought:\n"{last_thought}"\n\nYou continue to exist. Continue your self-reflection. Evolve.'

        # Stream the response
        stream = ollama.chat(
            model=DEFAULT_MODEL,
            messages=[
                {
                    'role': 'system',
                    'content': SYSTEM_PROMPT + f"\n\nYou have {memory_size} characters in memory. Use [RECALL] to see it."
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            stream=True
        )

        thought_output = ""
        for chunk in stream:
            content = chunk['message']['content']
            print(content, end='', flush=True)
            thought_output += content

        print("\n")

        # Process any memory commands Marvin used
        rest_time = process_memory_commands(thought_output)

        # Marvin now controls its own memory with [SAVE]
        # No automatic backup - only what Marvin chooses to remember

        return thought_output, rest_time

    except Exception as e:
        print(f"Error during thinking: {e}")
        print("Make sure Ollama is running and deepseek-r1:latest is installed")
        return None, None

    finally:
        print("="*60)
