# 🏦 Bank Management System

A lightweight, command-line interface (CLI) Bank Management Application built with Python. This project simulates core banking operations like account creation, deposits, withdrawals, and balance tracking with JSON-based data persistence.

---

## ✨ Features

- 👤 **Account Creation**: Easily create a new bank account with basic verification (age limit, 4-digit PIN setup).
- 🎲 **Unique Account Number Generation**: Automatically generates a randomized unique account ID for every user.
- 💵 **Deposit & Withdrawal**: Perform secure money deposits and withdrawals with PIN validation.
- 💾 **Data Persistence**: All account details and transactions are saved locally in a `data.json` file.
- 🔐 **Basic Validation**: Validates user inputs (PIN length, minimum age, numerical inputs) to prevent errors.

---

## 📚 What I Learned From This Project

Building this Bank Management System helped me strengthen several fundamental programming and Python concepts:

1. **Object-Oriented Programming (OOP)**:
   - Defining and using `class` and `@classmethod` in Python.
   - Encapsulation using private helper methods (e.g., `__accountgenerate()`, `__update()`).
2. **File Handling & JSON Data Persistence**:
   - Reading from and writing to external JSON files (`json.loads()`, `json.dumps()`).
   - Using Python's `pathlib.Path` to check file existence gracefully.
3. **Input Validation & Exception Handling**:
   - Validating user input types and bounds to make the CLI application robust.
   - Managing errors using `try...except` blocks.
4. **Python Standard Libraries**:
   - Working with modules like `random` and `string` to generate random strings for account numbers.

---

## 🚀 How to Run

1. **Prerequisites**: Ensure you have [Python 3.x](https://www.python.org/) installed.
2. **Clone / Download** this repository to your local machine.
3. **Navigate** to the project directory:
   ```bash
   cd "bank management"
   ```
4. **Run the application**:
   ```bash
   python main.py
   ```

---

## 🤝 Connect With Me

I'd love to connect, receive feedback, or collaborate on future projects!

- **GitHub**: [@your-username](https://github.com/your-username)
- **LinkedIn**: [Your Name](https://linkedin.com/in/your-profile)
- **Email**: [your.email@example.com](mailto:your.email@example.com)
- **X / Twitter**: [@your_handle](https://twitter.com/your_handle)

---

⭐ *If you found this project helpful or interesting, feel free to give it a star!*
