# Storage Checker

This project is a simple Python application that checks and displays the available storage on your system. It provides a graphical user interface (GUI) to show the amount of storage left in gigabytes (GB) and as a percentage using a visual bar.

## Project Structure

```
storage-checker
├── .venv
├── dist
│   ├── main.build
│   ├── main.dist
│   ├── main.onefile-build
│   └── main.exe       # Executable for application
├── src
│   ├── __pycache__
│   ├── main.py        # Entry point of the application
│   └── gui.py         # Contains GUI components
└── README.md           # Project documentation
```

## Running the Executable

1. Navigate to dist folder
2. run main.exe

## Running / Modifing the Source

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Activate the virtual environment:
   - On Windows:
     ```
     .\.venv\Scripts\Activate.ps1
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
4. Run the application using the following command:
   ```
   python src/main.py
   ```

## Compiling script using Nuitka

1. Activate Virtual environment
2. Run Nuitka with following command:
```
nuitka --standalone --onefile --enable-plugin=tk-inter --windows-console-mode=disable --output-dir=dist src/main.py
```

## Features

- Displays the available storage in GB.
- Shows the storage percentage with a visual bar.
- User-friendly interface for easy access to storage information.
