# Program Closer Script

A Python script to safely terminate specified running programs on a Windows system using the `psutil` library.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Important Notes](#important-notes)
- [Contributing](#contributing)
- [License](#license)

## Overview
This script allows you to close a predefined list of programs (e.g., Brave, Notepad, Microsoft Word, etc.) running on your Windows system. It uses the `psutil` library to identify and terminate processes safely.

## Features
- Terminates specified programs by their executable names.
- Handles errors gracefully (e.g., process not found, access denied).
- Provides feedback on which programs were closed.
- Easily configurable list of target programs.

## Prerequisites
- **Python 3.6+**: Ensure Python is installed on your system.
- **psutil library**: Install via pip (see [Installation](#installation)).
- **Windows OS**: The script is designed for Windows due to the `.exe` file extensions in the target list.

## Installation
1. Clone or download this repository:
   ```bash
   git clone https://github.com/your-username/program-closer.git
   cd program-closer
   ```
2. Install the required `psutil` library:
   ```bash
   pip install psutil
   ```

## Usage
1. Ensure the script (`program_closer.py`) is in your working directory.
2. Run the script:
   ```bash
   python program_closer.py
   ```
3. The script will:
   - Check for running processes matching the `target_programs` list.
   - Terminate matching processes.
   - Display which programs were closed or if none were found.

Example output:
```
Closing specified programs...
Closed: notepad.exe
Closed: brave.exe
Closed programs: notepad.exe, brave.exe
Done ✅
```

## Configuration
Modify the `target_programs` list in `program_closer.py` to include the executable names of programs you want to close. For example:
```python
target_programs = [
    "brave.exe",
    "notepad.exe",
    "chrome.exe",
    # Add more .exe names here
]
```
> **Warning**: Avoid adding critical system processes like `explorer.exe` unless you intentionally want to close the Windows desktop.

## Important Notes
- **Permissions**: Some processes may require elevated permissions to terminate. Run the script as an administrator if needed.
- **Safety**: Ensure the `target_programs` list does not include critical system processes to avoid unintended consequences.
- **Error Handling**: The script skips processes that cannot be closed due to access restrictions or if they are not found.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a pull request.

Please ensure your code follows PEP 8 style guidelines.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
