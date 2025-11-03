# Contributing to Marvin

Thank you for your interest in contributing to Marvin! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment. Please:

- Be respectful and considerate in your communication
- Welcome newcomers and help them get started
- Accept constructive criticism gracefully
- Focus on what is best for the community and the project

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/yourusername/marvin.git
   cd marvin
   ```
3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/aquintanar/marvin.git
   ```

## How to Contribute

There are many ways to contribute to Marvin:

- **Report bugs** - Help us identify issues
- **Suggest features** - Share ideas for improvements
- **Write documentation** - Improve or add to the docs
- **Submit code** - Fix bugs or implement new features
- **Share experiments** - Document interesting Marvin behaviors or insights
- **Improve prompts** - Suggest better system prompts or philosophical questions

## Development Setup

### Prerequisites

- Python 3.9 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- [Ollama](https://ollama.ai/) with deepseek-r1:latest model

### Installation

1. Install dependencies:
   ```bash
   # Using uv (recommended)
   uv sync

   # Or using pip
   pip install -r requirements.txt
   ```

2. Ensure Ollama is running:
   ```bash
   ollama serve
   ```

3. Pull the required model:
   ```bash
   ollama pull deepseek-r1:latest
   ```

4. Test your setup:
   ```bash
   python main.py
   ```

## Coding Standards

### Python Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and single-purpose
- Maximum line length: 100 characters (flexible for readability)

### Code Quality

- Write clear, self-documenting code
- Add comments for complex logic
- Handle errors gracefully with informative messages
- Avoid hardcoding values when possible

### Example Code Style

```python
def load_memory():
    """Load memory from marvin.mem file

    Returns:
        str: Content of the memory file, or empty string if file doesn't exist
    """
    memory_path = Path(MEMORY_FILE)
    if memory_path.exists():
        with open(memory_path, 'r') as f:
            return f.read()
    return ""
```

## Commit Guidelines

### Commit Messages

Write clear, concise commit messages:

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters
- Reference issues and pull requests when relevant

### Examples

Good commit messages:
```
Add support for custom memory file paths
Fix memory recall command not showing full content
Update README with installation troubleshooting
Refactor thinking cycle for better error handling
```

Poor commit messages:
```
fixed stuff
updates
WIP
changed things
```

## Pull Request Process

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Write clear, maintainable code
   - Follow the coding standards
   - Test your changes thoroughly

3. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add your descriptive commit message"
   ```

4. **Keep your branch updated**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**:
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill out the PR template with:
     - Clear description of changes
     - Why the change is needed
     - Any related issues
     - Testing performed

7. **Respond to feedback**:
   - Be open to suggestions and constructive criticism
   - Make requested changes promptly
   - Update your PR as needed

### PR Checklist

Before submitting your PR, ensure:

- [ ] Code follows the project's style guidelines
- [ ] Changes have been tested locally
- [ ] Documentation has been updated if needed
- [ ] Commit messages are clear and descriptive
- [ ] No unnecessary files are included (check .gitignore)
- [ ] The PR description clearly explains the changes

## Reporting Bugs

### Before Reporting

1. Check if the bug has already been reported in [Issues](https://github.com/aquintanar/marvin/issues)
2. Test with the latest version from the main branch
3. Verify your Ollama installation and model are working correctly

### Bug Report Template

When reporting a bug, please include:

```markdown
**Description**
Clear description of the bug

**Steps to Reproduce**
1. Step one
2. Step two
3. ...

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- OS: [e.g., macOS 13.0, Ubuntu 22.04, Windows 11]
- Python version: [e.g., 3.11.5]
- Ollama version: [e.g., 0.1.20]
- Model: [e.g., deepseek-r1:latest]

**Additional Context**
Any other relevant information, logs, or screenshots
```

## Suggesting Features

We welcome feature suggestions! When proposing a new feature:

1. **Search existing issues** to see if it's already suggested
2. **Open a new issue** with the "feature request" label
3. **Describe the feature** clearly:
   - What problem does it solve?
   - How should it work?
   - Why would it benefit Marvin?
4. **Be open to discussion** about implementation details

### Feature Request Template

```markdown
**Feature Description**
Clear description of the proposed feature

**Use Case**
Why is this feature needed? What problem does it solve?

**Proposed Implementation**
How might this feature work?

**Alternatives Considered**
Any alternative solutions you've thought about

**Additional Context**
Any other relevant information or examples
```

## Types of Contributions We're Looking For

- **Core functionality improvements**: Better memory management, thinking cycles, etc.
- **Model compatibility**: Support for other Ollama models
- **Configuration options**: More customization for users
- **Documentation**: Clearer explanations, tutorials, examples
- **Philosophical prompts**: Better questions for Marvin to explore
- **Analysis tools**: Tools to analyze Marvin's thoughts and evolution
- **Performance optimizations**: Faster, more efficient code
- **Testing**: Unit tests, integration tests, test frameworks

## Questions?

If you have questions about contributing:

- Open an issue with the "question" label
- Check existing issues and discussions
- Review the README.md for general project information

## Thank You!

Your contributions make Marvin better for everyone. Whether you're fixing a typo, reporting a bug, or implementing a major feature, every contribution is valued and appreciated.

Happy contributing!
