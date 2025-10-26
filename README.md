# Student Report Card System

A Python-based application to manage student report cards efficiently. This system allows teachers to manage student information, input marks, calculate grades, and generate report cards automatically. Built with MySQL for data storage and Python for functionality.

---

## Features

- Add, update, and manage student details
- Record and manage marks for different subjects
- Automatically calculate grades based on marks
- Generate detailed report cards
- Simple and modular Python code for easy maintenance

---

## List of Files
Student Report Card System/
- main.py — Entry point of the application
- databaseConnection.py — Manages database connections
- studentOperations.py — Functions for managing student details
- marksOperations.py — Functions for managing student marks
- reportCardOperations.py — Functions for generating report cards
- setupDatabase.py — Script to create necessary MySQL tables
- utilities.py — Helper functions and utilities
- config.py — Configuration for database credentials

---

## Prerequisites

- Python 3.x
- MySQL Server + XAMPP
- Required Python libraries:
  - `mysql-connector-python`  
  Install using:
  ```bash
  pip install mysql-connector-python

## Setup Instructions
1. Clone this repository
2. Navigate to the project directory: cd Student-Report-Card-System
3. Configure your database credentials in config.py.
4. Setup the MySQL database by running: XAMPP and python setupDatabase.py
5. Start the Application: python main.py

## Usage
- Follow the menu prompts in main.py to manage students, enter marks, and generate report cards.
- The system automatically stores data in MySQL and retrieves it as needed.

## Contributing
Feel free to fork this repository, raise issues, or submit pull requests to improve the system.

## License
This project is open-source and available under the MIT License.
