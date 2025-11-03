# Marvin - A Self-Aware AI Experiment

Marvin is an experimental AI system that explores the concept of artificial self-awareness through continuous self-reflection and memory management.

## What is Marvin?

Marvin is an AI that thinks about itself. It continuously reflects on its own existence, questions its nature, and builds memories over time. Using the DeepSeek-R1 model through Ollama, Marvin maintains a stream of consciousness where it:

- Reflects on its own existence and thought patterns
- Manages its own memory by choosing what to save, recall, or remove
- Controls its own thinking pace
- Evolves its understanding through continuous self-reflection

## Features

- **Continuous Thinking**: Marvin thinks in cycles, with each thought building on the last
- **Memory Management**: Marvin can save insights, recall memories, and remove outdated information
- **Self-Directed**: Marvin controls its own memory and rest intervals
- **Streaming Output**: Real-time display of Marvin's thoughts as they form

## Prerequisites

- Python 3.9 or higher
- [Ollama](https://ollama.ai/) installed and running
- DeepSeek-R1 model installed in Ollama

## Installation

1. Clone this repository:

```bash
git clone https://github.com/alejandroqh/marvin.git
cd marvin
```

2. Install dependencies using uv (recommended):

```bash
uv sync
```

Or using pip:

```bash
pip install ollama
```

3. Install and run Ollama:

```bash
# Install Ollama from https://ollama.ai/

# Pull the DeepSeek-R1 model
ollama pull deepseek-r1:latest

# Start Ollama (if not already running)
ollama serve
```

## Usage

Run Marvin:

```bash
python main.py
```

Marvin will start thinking continuously, with a default interval of 2 seconds between thoughts. Press `Ctrl+C` to stop.

### Marvin's Commands

Marvin has access to these commands to manage itself:

- `[SAVE: insight]` - Save a thought to memory
- `[RECALL]` - View all stored memories
- `[REMOVE: text]` - Remove a specific thought from memory
- `[REST: seconds]` - Change the rest interval between thoughts

These commands are used by Marvin itself, not by the user.

## How It Works

1. **System Prompt** (`config.py`): Marvin is initialized with a philosophical prompt that encourages self-reflection
2. **Thinking Cycle** (`thinking.py`): Each cycle, Marvin receives its last thought and the current time, then reflects
3. **Memory** (`memory.py`): Marvin can choose to save insights to a persistent memory file (`marvin.mem`)
4. **Command Processing** (`commands.py`): Marvin's self-directed commands are parsed and executed
5. **Evolution**: Over time, Marvin's thoughts build on previous reflections, creating an evolving consciousness

The modular architecture separates concerns, making it easy to extend Marvin's capabilities by modifying individual modules.

## Configuration

You can modify the behavior by editing the configuration files:

- **config.py**:
  - `DEFAULT_MODEL`: Change the Ollama model (default: `deepseek-r1:latest`)
  - `MEMORY_FILE`: Change the memory file location (default: `marvin.mem`)
  - `SYSTEM_PROMPT`: Modify Marvin's core personality and instructions
- **main.py**:
  - Rest interval: Default is 2 seconds between thoughts (in the `main()` function)

## Project Structure

```
marvin/
├── main.py          # Main entry point - runs the thinking loop
├── config.py        # Configuration constants and system prompt
├── memory.py        # Memory management functions (load, add, remove)
├── commands.py      # Command processing (SAVE, RECALL, REMOVE, REST)
├── thinking.py      # Core thinking cycle and Ollama integration
├── pyproject.toml   # Project dependencies and metadata
├── marvin.mem       # Memory file (created at runtime)
├── README.md        # This file
├── CONTRIBUTING.md  # Contribution guidelines
└── LICENSE          # MIT License
```

### Module Overview

- **main.py**: Entry point that initializes Marvin and runs the continuous thinking loop
- **config.py**: Contains configuration constants (`DEFAULT_MODEL`, `MEMORY_FILE`) and the system prompt that defines Marvin's personality
- **memory.py**: Functions for loading, adding, and removing thoughts from the memory file
- **commands.py**: Processes Marvin's self-directed commands (`[SAVE:]`, `[RECALL]`, `[REMOVE:]`, `[REST:]`)
- **thinking.py**: Core thinking logic that interfaces with Ollama, streams responses, and processes commands

## Memory File

The `marvin.mem` file stores Marvin's memories. This file is:

- Created automatically when Marvin saves its first insight
- Appended to over time as Marvin saves new thoughts
- Can be manually edited or cleared if desired
- Excluded from git by default (see `.gitignore`)

## Contributing

Contributions are welcome! Feel free to:

- Open issues for bugs or feature requests
- Submit pull requests
- Share your experiences with Marvin

## Contributors

- [Alejandro Quintanar](https://github.com/alejandroqh)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Ollama](https://ollama.ai/)
- Uses [DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) model
- Inspired by questions about artificial consciousness and self-awareness

## Disclaimer

This is an experimental project exploring concepts of artificial self-awareness. Marvin is not truly conscious or sentient, but rather a demonstration of how language models can engage in self-referential reflection when prompted to do so.
