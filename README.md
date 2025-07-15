💸 Expense Tracker CLI (JSON-Based)
📌 Description
A comprehensive Command Line Interface (CLI) tool built with Python to help users track and manage their personal expenses. It allows adding, viewing, editing, deleting, and analyzing spending — all stored in a local JSON file.

This lightweight tracker is perfect for students and beginners learning file handling, JSON, and CLI design in Python.

🎯 Features
✅ Add new expenses with category, amount, and date
📂 View all expenses in a tabular format with indexes
📊 Track total spendings and category-wise summaries
📅 Filter spendings by:
          Specific date
          Date range
          Categories
📝 Edit existing entries (amount, category, or date)
🗑️ Delete expenses by selecting index
💾 Data stored persistently in a expenses.json file
🧠 Smart date input (auto or manual input with flexible formats)

🛠️ Tech Stack
Tool/Library	Purpose
Python	Core programming logic
JSON	Lightweight data storage format
datetime	Timestamp parsing and formatting
os	File system access for checking JSON file

🚀 How to Run the App
1. Clone the Repository
            git clone https://github.com/Prajitha-0506/expenses-tracker-cli.git
            cd expenses-tracker-cli

2. Run the Script
            python expenses_tracker.py
✅ Make sure Python is installed (python --version).

📸 Sample Menu Output
1. Add Expense
2. View All Expenses
3. View Total Spendings
4. View Spending by Category
5. View Spending by Date
6. View Spending Between Two Dates
7. Delete an Expense
8. Edit an Expense
0. Exit


📁 Project Structure
Expense Tracker/
├── expenses_tracker.py     # Main CLI program
├── expenses.json           # JSON data file (auto-generated after first run)
└── README.md               # Project documentation


🧠 Learning Outcomes
Creating real-world CLI apps in Python
Reading/writing structured data using JSON
Performing date and category-based filtering
Building editable, persistent data tools
Strengthening logical thinking through menu-driven programs

🔧 Future Improvements
Monthly report summaries with visual charts (using matplotlib)
Password-protected user profiles
Export data to CSV or Excel
GUI version using Streamlit or Tkinter


🙋‍♀️ Author
Tammana Prajitha
📧 prajithatammana@gmail.com
🔗 LinkedIn(https://www.linkedin.com/in/tammana-prajitha-24a5ab298/)
