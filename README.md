# 📚 Library Management System (LMS)

The **Library Management System (LMS)** is a Python-based desktop application built using **PyQt5** for the graphical
user interface (UI) and **PostgreSQL** as the backend database. This application helps users manage a library by keeping
track of books, members, and borrowing transactions.

The application follows a **three-layer architecture** for better modularity and maintainability.

---

## 🏛 Application Architecture

The project is structured based on the **three-layer architecture**, consisting of:

1. **UI Layer**:
    - Contains the graphical user interface built using **PyQt5**.
    - Responsible for handling user interaction and displaying data.

2. **Controller Layer**:
    - Acts as the bridge between the UI and the repository layer.
    - Contains the application’s business logic, processes user inputs, and interacts with the repository.

3. **Repository Layer**:
    - Handles data storage and retrieval using **PostgreSQL**.
    - Provides a clean interface for data operations (CRUD) on the database.

---

## 📋 Features

- Add, update, and delete books and members.
- Track borrowing and return history.
- Simple and intuitive PyQt5-based user interface.
- PostgreSQL database for persistent data storage.
- Modular architecture for scalability and easy maintenance.

---

## 🛠 Installation

### 1. Prerequisites

- Python 3.8 or higher
- PostgreSQL installed and configured

### 2. Create and activate a virtual environment

Run the following commands to create a virtual environment and activate it:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On Linux/macOS
source venv/bin/activate
```

### 3. Install dependencies

After activating the virtual environment, install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Configure the PostgreSQL Database

Ensure that your PostgreSQL server is running and that you have created a database for the application. Update the
database connection settings in the repository layer to match your PostgreSQL configuration.

If the necessary tables are not created, you may need to run SQL scripts or ensure that the repository layer initializes
them on the first run.

---

### 5. Running the Application

```bash
python app.py
```

---



