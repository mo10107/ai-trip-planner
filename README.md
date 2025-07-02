# AI Trip Planner

This project is an AI-powered trip planner. Below are the instructions to set up the development environment and install dependencies.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) (a fast Python package manager)
- Python 3.11.13 (CPython, Windows x86_64)
   ```sh
   pip install uv
   ```

## Setup Instructions

1. **List available Python versions with uv:**
   ```sh
   uv python list
   ```

2. **Install the required Python version:**
   ```sh
   uv python install cpython-3.11.13-windows-x86_64-none
   ```

3. **Create a virtual environment:**
   ```sh
   uv venv env --python cpython-3.11.13-windows-x86_64-none
   ```

4. **Activate the virtual environment:**
   ```sh
   .\env\Scripts\activate.bat
   ```
   Or, if you are using a different shell, adjust the activation command accordingly.

5. **Install project dependencies:**
   ```sh
   uv add langchain langgraph
   ```

6. **List installed packages (optional):**
   ```sh
   uv pip list
   ```

## Notes

- Make sure to activate the virtual environment before running or developing the project.
- For command history in Windows Command Prompt, you can use:
  ```sh
  doskey /history
  ```

## Project Structure

- `env/` - Virtual environment directory
- `README.md` - Project documentation

