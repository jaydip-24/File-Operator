# File Operator

## Project Name

File Operator - Personal Journal Manager

## Project Type

Python File Handling and Object-Oriented Programming (OOP) Console Program

## Project Folder

This project is created inside:

`D:\RND Assignments\Assignment-6\`

Main Python file:

`Assign.py`

## About the Project

File Operator is a simple Python console program that lets you keep a
personal journal in a text file. Every entry is saved with the date and
time, and all entries are stored in a file named `journal.txt`.

The program uses a menu-driven system so the user can add, view, search
and delete journal entries. All the work is done by one class,
`JournalManager`, and every file operation is protected with exception
handling so the program does not crash.

## Features

The project provides the following options:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

## Class Design

| Class | Method | What it does |
|-------|--------|--------------|
| `JournalManager` | `__init__()` | Sets the journal file name (`journal.txt`) |
| `JournalManager` | `create_file_if_missing()` | Creates the file only if it does not exist (mode `x`) |
| `JournalManager` | `add_entry()` | Adds a new entry with a timestamp (mode `a`) |
| `JournalManager` | `view_entries()` | Shows all entries (mode `r`) |
| `JournalManager` | `search_entries()` | Finds entries by keyword or date |
| `JournalManager` | `delete_entries()` | Deletes the journal file after confirmation |

## Python Concepts Used

- Classes and objects
- Constructor using `__init__`
- Instance methods using `self`
- File handling using `open()` and the `with` statement
- File modes `r`, `a` and `x`
- Reading and writing text files
- Exception handling using `try` and `except`
- Date and time using the `datetime` module
- File deletion using the `os` module
- `while` loop for the main menu
- `if`, `elif`, and `else`
- List comprehension
- Functions using `def`

## How to Run the Project

### Step 1: Open the Project

Open the `Assignment-6` folder in Visual Studio Code.

### Step 2: Open the Terminal

Open the integrated terminal in Visual Studio Code.

### Step 3: Go to the Project Folder

```powershell
cd "D:\RND Assignments\Assignment-6"
```

### Step 4: Run the Python File

```powershell
py Assign.py
```

### Step 5: Use the Menu

The welcome menu appears. Type a number from 1 to 5 and press Enter.

## How the Program Works (Step by Step)

### 1. Add a New Entry

1. Type `1` and press Enter.
2. Type your journal entry when the program asks for it.
3. Press Enter.
4. The program saves the entry with the current date and time at the end of
   `journal.txt`.
5. The message `Entry added successfully!` is displayed.

If `journal.txt` does not exist, the program creates it automatically.
Empty entries are not accepted.

![Add Entry](Screenshots/Add_Entry.png)

### 2. View All Entries

1. Type `2` and press Enter.
2. The program reads `journal.txt`.
3. All entries are shown with their date and time under
   `Your Journal Entries:`.

If the file does not exist or is empty, the message
`No journal entries found. Start by adding a new entry!` is displayed.

![View All Entries](Screenshots/View_All_Entries.png)

### 3. Search for an Entry

1. Type `3` and press Enter.
2. Type a keyword or a date (for example a word from an entry, or a date
   like `2026-10-28`) and press Enter.
3. The program checks every entry and shows the ones that match under
   `Matching Entries:`.

The search is not case sensitive. If nothing matches, the message
`No entries were found for the keyword: ...` is displayed. If the journal
file does not exist, an error message asks the user to add an entry first.

![Search Entry](Screenshots/Search.png)

### 4. Delete All Entries

1. Type `4` and press Enter.
2. The program asks `Are you sure you want to delete all entries? (yes/no)`.
3. Type `yes` and press Enter to delete the journal file.
4. The message `All journal entries have been deleted.` is displayed.

Any answer other than `yes` cancels the delete and keeps the entries safe.
If there is no journal file, the message `No journal entries to delete.` is
displayed.

![Delete Entries](Screenshots/Delete_Entries.png)

### 5. Exit

1. Type `5` and press Enter.
2. The message `Thank you for using Personal Journal Manager. Goodbye!` is
   displayed and the program closes.

If any other number or text is typed, the message
`Invalid option. Please select a valid option from the menu.` is displayed
and the menu appears again.

## File Modes Used

| Mode | Where it is used | Effect |
|------|------------------|--------|
| `r` | View and search | Only reads the file. The file must exist |
| `a` | Add entry | Adds to the end of the file and keeps old entries |
| `x` | Create file | Creates a new file and fails if it already exists |

The `w` mode is not used because it erases all old entries, so `a` is the
safe choice for a journal.

## Exception Handling

| Error | When it happens | What the program does |
|-------|-----------------|-----------------------|
| `FileNotFoundError` | Journal file is missing | Shows a clear message |
| `FileExistsError` | File already exists in mode `x` | Ignores it and continues |
| `PermissionError` | No permission to read, write or delete | Shows a permission message |
| `OSError` | Any other file problem | Shows the error message |
| `KeyboardInterrupt`, `EOFError` | User presses Ctrl+C or Ctrl+D | Exits politely |

## Project Structure

```text
Assignment-6
│
├── Screenshots
│   ├── Add_Entry.png
│   ├── View_All_Entries.png
│   ├── Search.png
│   └── Delete_Entries.png
├── Assign.py
├── journal.txt
└── README.md
```

`journal.txt` is created automatically when the first entry is added.

## Assumptions

- Entries are stored in `journal.txt` in the same folder as `Assign.py`.
- Each entry is saved in this format, followed by a blank line:

  ```text
  [YYYY-MM-DD HH:MM:SS]
  Your entry text
  ```

- Search works for both keywords and dates because the timestamp is part of
  every entry.
- Empty entries and empty search words are rejected with a message.
- Only the answer `yes` confirms deleting all entries.
- The program works only with text files (`.txt`).

## Requirements

- Python 3
- Visual Studio Code (optional)
- Python extension for Visual Studio Code (optional)

No external Python libraries are required for this project.

## Learning Outcomes

After completing this project, the user can understand:

- How to read, write and append text files in Python
- How the file modes `r`, `a` and `x` are different
- How to handle errors such as `FileNotFoundError` and `PermissionError`
- How to create a class and use instance methods
- How to build a menu-driven Python program
- How to handle invalid user input

## Conclusion

File Operator is a basic Python Personal Journal Manager. It combines file
handling, exception handling and OOP in one practical project, and is
suitable for beginners who are learning Python.