"""
Project: Personal Expense Tracker
Author: Tammana Prajitha
Description: Tracks daily expenses, shows summaries, and saves data using JSON.
Date: June 2025
"""



import json
import os
from datetime import datetime


DATA_FILE = "expenses.json"


def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    else:
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


expenses = load_expenses()




def add_expense():
    amount = int(input("Enter the amount: "))
    category = input("Enter a Category: ")
    date = input("Do you want to use today's date(y/n): ").lower()
    if date == "y":
        date = datetime.today().strftime("%Y-%m-%d")
    else:
        raw_date = input("Enter the date manually (DD/MM/YY or YYYY-MM-DD): ")
        try:
            date = datetime.strptime(raw_date, "%d/%m/%y").strftime("%Y-%m-%d")
        except ValueError:
            date = raw_date
    new_entry = {"amount":amount,"category":category,"date":date}
    expenses.append(new_entry)
    save_expenses(expenses)
    print("Successfully added!!!!!")



def view_all_expenses():
    if len(expenses) == 0:
        print("No record found.")
        return

    print(f"{'Date'.ljust(12)} | {'Category'.ljust(15)} | Amount")
    print("*"*40)
    for idx,entry in enumerate(expenses):
        print(f"{idx}.{entry['date'].ljust(12)} | {entry['category'].ljust(15)} | {entry['amount']}/-")




def view_total_spendings():
    total = 0
    for entry in expenses:
        total += entry['amount']

    print(f"\nTotal Spendings: {total}")




def view_spendings_by_category():
    category_totals = {}
    for entry in expenses:
        category = entry['category']
        amount = entry['amount']

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("Spendings by category")
    print("*"*40)
    for category,total in category_totals.items():
        print(f"{category.ljust(15)} : {total}/-")




def view_spendings_by_date():
    date_totals = {}
    for entry in expenses:
        date = entry['date']
        amount = entry['amount']

        if date in date_totals:
            date_totals[date] += amount
        else:
            date_totals[date] = amount

    print("Spendings by date")
    print("*"*40)
    for date,total in date_totals.items():
        print(f"{date.ljust(15)} : {total}/-")




def view_spendings_by_input_dates():
    start = input("Enter the start date (YYYY-MM-DD): ").replace("/", "-")
    end = input("Enter the end date (YYYY-MM-DD): ").replace("/", "-")

    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    total = 0

    for entry in expenses:
        entry_date = datetime.strptime(entry['date'], "%Y-%m-%d")

        if start_date <= entry_date <= end_date:
            total += entry['amount']

    print(f"Your total spendings from {start_date} to {end_date} : {total}")



def delete_expenses():
    view_all_expenses()
    index = int(input("Enter the index of the entry that you want to delete."))
    if 0 <= index < len(expenses):
        expenses.pop(index)
        print("Scuccessfully deleted.")
        save_expenses(expenses)
    else:
        print("Invalid Index.")




def edit_expenses():
    view_all_expenses()
    index = int(input("Enter the index of the entry that you want to edit."))
    if 0 <= index < len(expenses):
        entry = expenses[index]
        field = input("Enter the field you want to edit (amount/category/date): ").lower()
        if field in entry:
            if field == "amount":
                edit = int(input("Enter the amount: "))
            else:
                edit = input("Enter the new value: ")
        entry[field] = edit
        print("Successfully edited.")
        save_expenses(expenses)
    else:
            print("Invalid.")




while True:
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spendings")
    print("4. View Spending by Category")
    print("5. View Spending by Date")
    print("6. View Spending Between Two Dates")
    print("7. Delete an expense")
    print("8. Edit an expense")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_all_expenses()
    elif choice == "3":
        view_total_spendings()
    elif choice == "4":
        view_spendings_by_category()
    elif choice == "5":
        view_spendings_by_date()
    elif choice == "6":
        view_spendings_by_input_dates()
    elif choice == "7":
        delete_expenses()
    elif choice == "8":
        edit_expenses()
    elif choice == "0":
        break
    else:
        print("Invalid choice! Try again.")


