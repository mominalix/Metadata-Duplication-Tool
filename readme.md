# Metadata Editor

This repository contains a Metadata Editor tool that allows you to read the metadata of PDF files in one folder and update the metadata of corresponding PDF files in another folder. Additionally, it provides instructions on how to use the tool and edit the source code.

## Folder Structure

The repository is structured as follows:

```
Metadata-Editor/
│
├── build/
│   ├── Metadata Editor.exe
│   ├── Original/
│   ├── Edited/
│   └── How to use.pdf
│
└── src/
    ├── run.py
    ├── Original/
    └── Edited/
    └── requirements.txt
```

- **build/**: Contains the packaged product along with sample PDFs in the "Original" and "Edited" folders, and a guide on how to use the tool ("How to use.pdf").
- **src/**: Contains the source code (`run.py`) along with sample PDFs in the "Original" and "Edited" folders.

## How to Use

1. **Using the Packaged Product**:
   - Navigate to the "build/" folder.
   - Run the "Metadata Editor.exe" file.
   - Follow the instructions in the "How to use.pdf" guide for using the Metadata Editor tool.

2. **Editing the Source Code**:
   - Navigate to the "src/" folder.
   - Open the `run.py` file in a text editor or IDE of your choice.
   - Modify the script according to your requirements.
   - Run the script using Python.

## How the Code Works

The `run.py` script in the "src/" folder performs the following tasks:

1. It reads the metadata of PDF files in the "Original" folder.
2. It updates the metadata of corresponding PDF files in the "Edited" folder with the same metadata.
3. It provides a command-line interface for interacting with the tool.

To understand how to edit the source code, refer to the comments within the `run.py` file and the Python docstrings for each function.


