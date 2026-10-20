# Library Management System

A simple, menu-driven Library Management System built with Python. This project allows users to manage books and library members, check book availability, borrow books, and store library data using file handling.

## ✨ Features

### 📖 Book Management
- **Check Book Availability:** Check whether a book is available and view its available quantity and price.
- **Add Books:** Add new books or increase the quantity of existing books.
- **Borrow Books:** Borrow a specified quantity of books while checking stock availability.
- **Remove Books:** Remove a book from the library's records.

### 👥 Member Management
- **Check Members:** View a member's name, monthly salary, and working hours.
- **Add Members:** Register new library members.
- **Update Member Details:** Update the salary and working hours of existing members.
- **Remove Members:** Remove members from the library's records.

### 💾 File Handling
- Stores book and member information in `storage_file.txt`.
- Uses Python's `ast.literal_eval()` to load stored data.
- Generates an organized report in `output_file.txt`, displaying book details and member information.

## 🛠️ Technologies Used

- **Python**: Core programming language.
- **Object-Oriented Programming (OOP)**: Classes, constructors, attributes, and methods.
- **File Handling**: Reading and writing text files.
- **Data Structures**: Lists and dictionaries.
- **AST Module**: Safely evaluates Python literal data using `ast.literal_eval()`.

## 📁 Project Structure

```text
Library-Management-System/
│
├── main.py
├── storage_file.txt
├── output_file.txt
└── README.md
```

*Note: `main.py` represents your Python script. Rename it to match your actual filename if necessary.*

## ⚙️ Requirements

- Python 3.12 or newer is recommended because the code uses nested quotation marks inside f-strings.
- No external libraries are required. The project uses Python's built-in `ast` module.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd Library-Management-System
```

### 3. Prepare the Storage File

Create a file named `storage_file.txt` in the project directory.

For an empty library, initialize it with two lines:

```text
[]
[]
```

The first line stores book records, and the second line stores member records.

### 4. Run the Program

```bash
python main.py
```

Follow the interactive prompts in the terminal to manage books and members.

## 📋 Data Format

### Books

Each book is stored as a dictionary containing its name, available quantity, and unit price.

```python
{
    "name": "python basics",
    "amt": 5,
    "price": 250
}
```

### Members

Each member is stored as a dictionary containing their name, monthly salary, and working hours.

```python
{
    "name": "ram",
    "salary": 20000,
    "working_hour": 8
}
```

Both types of records are stored in lists and saved to `storage_file.txt`.

## 🎯 Learning Objectives

This project was developed to practice and strengthen my understanding of:

- Object-Oriented Programming in Python.
- Lists and dictionaries.
- Loops and conditional statements.
- Searching, adding, updating, and removing records.
- Reading and writing files.
- Working with persistent data.
- Generating formatted text reports.

## 🔮 Future Improvements

- Add input validation and exception handling.
- Introduce a graphical user interface.
- Track borrowed books and return transactions.
- Add member IDs and borrowing histories.
- Use a database such as SQLite for data storage.
- Improve the user interface and navigation.

## 👨‍💻 Author

**Arhat**

A student learning Python and building projects to improve programming skills.

---

*This project is part of my journey in learning Python, Object-Oriented Programming, and software development.*
