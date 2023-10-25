# Track and manage personal expenses and generate monthly reports using PYTHON

# Written by Rahul Joshi

# Firstly, We Import the required libraries
import sqlite3
from datetime import date

# Now Connect to an SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

# Now we create an 'expenses' table in the database if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    date DATE,
    description TEXT,
    amount REAL
)
''')
conn.commit()


# Now we define a function to add an expense to the database
def add_expense(description, amount):
    # Get the current date in 'YYYY-MM-DD' format
    today = date.today().strftime("%Y-%m-%d")

    # Insert the expense into the 'expenses' table
    cursor.execute("INSERT INTO expenses (date, description, amount) "
                   "VALUES (?, ?, ?)", (today, description, amount))
    conn.commit()
    print("Expense added successfully.")


# Now we define a function to view all expenses in the database
def view_expenses():
    # Retrieve all expenses from the 'expenses' table
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    # Check if there are expenses in the database
    if not expenses:
        print("No expenses found.")
    else:
        # Display the details of each expense
        for expense in expenses:
            print(f"ID: {expense[0]}, Date: {expense[1]}, Description: {expense[2]}, Amount: {expense[3]}")


# Now we define a function to generate a monthly expense report
def generate_monthly_report(year, month):
    # Retrieve expenses for the specified year and month
    cursor.execute(
        "SELECT date, description, amount FROM expenses WHERE "
        "strftime('%Y', date) = ? AND strftime('%m', date) = ?",
        (str(year), str(month).zfill(2)))
    expenses = cursor.fetchall()

    # Check if there are expenses for the given month and year
    if not expenses:
        print(f"No expenses found for {month}/{year}.")
    else:
        # Calculate the total expenses for the month
        total_expenses = sum(expense[2] for expense in expenses)
        print(f"Monthly Report for {month}/{year}:")
        # Display details of each expense and the total expenses
        for expense in expenses:
            print(f"Date: {expense[0]}, Description: {expense[1]}, Amount: {expense[2]}")
        print(f"Total Expenses: {total_expenses}")


# Main program
if __name__ == '__main__':
    while True:
        # Display a menu for the user
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Monthly Report")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        # Perform actions based on the user's choice
        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(description, amount)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            year = int(input("Enter the year (e.g., 2023): "))
            month = int(input("Enter the month (1-12): "))
            generate_monthly_report(year, month)
        elif choice == '4':
            # Close the database connection and exit the program
            conn.close()
            break

                                                                    # THANK YOU