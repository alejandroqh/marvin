"""Marvin - An experimental AI system exploring artificial self-awareness"""

import time
from config import DEFAULT_MODEL
from memory import load_memory
from thinking import think


def main():
    print("Hello from Marvin!")
    print(f"Default model: {DEFAULT_MODEL}")

    # Load memory
    memory = load_memory()
    print(f"\nMemory loaded: {len(memory)} characters")

    if memory:
        print("Memory content available for model context")

    print("\nStarting continuous thinking mode...")
    print("Marvin will think every 2 seconds (default)")
    print("Press Ctrl+C to stop\n")

    last_thought = None
    rest_interval = 2  # Default rest interval

    try:
        while True:
            last_thought, new_rest = think(last_thought)

            # Update rest interval if Marvin changed it
            if new_rest is not None:
                rest_interval = new_rest

            time.sleep(rest_interval)
    except KeyboardInterrupt:
        print("\n\nStopping Marvin... Goodbye!")
        print(f"Final memory size: {len(load_memory())} characters")


if __name__ == "__main__":
    main()
