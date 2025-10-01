# 🗂️ Python File Organizer

A simple **Python-based File Organizer** that helps manage files inside folders with options to **read, copy, move, delete, and rename**. It also allows creating new folders and subfolders, making it easier to keep your files structured and accessible.

---

## 📌 Features
- **Folder Navigation**
  - View and select folders inside a given directory.
  - Create new folders or subfolders.
- **File Management**
  - Read (open) files with their default applications.
  - Copy files (creates a duplicate in the same folder).
  - Move files to other folders within the directory.
  - Delete unwanted files.
  - Rename files safely.
- **Project-Specific Handling**
  - Handles Python project folders separately.
- **Interactive CLI**
  - Text-based menu for navigation and file operations.

---

## 🛠️ Technologies Used
- **Python 3**
- Built-in modules:
  - `os` → for directory and file handling
  - `shutil` → for copying and moving files

---

## 📂 Directory Structure
By default, the script organizes files inside the following paths:

OrganizeF/
│
├── Files/
│ ├── Docs/ # For document files
│ ├── Images/ # For images
│ ├── PDF/ # For PDF files
│ ├── PythonProjects/ # For Python project folders
│ └── ... (new folders created here)
