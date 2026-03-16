from datetime import datetime
import csv
import os


def print_menu():
    print(f'{'='*30}')
    print(f"{'PERSONAL EXPENSE TRACKER':^30}")
    print(f'{'='*30}')
    print('1. Add expense')
    print('2. View all expenses')
    print('3. View total by category')
    print('4. View monthly summary')
    print('5. Exit')


def print_header(title):
    print(f"\n--- {title} ---")


def print_all_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    for expense in expenses:
        print(f"{expense["description"]:<15}: ${expense['amount']:.2f}")
    print(f"{'TOTAL SPENDING':<15}= ${get_total_spending(expenses):.2f}")


def print_spending_by_category(expenses):
    expenses = get_spending_by_category(expenses)
    for key, value in expenses.items():
        flag = "⚠️" if value > 100 else ""
        print(f"{key:<15}: ${value:.2f} {flag}")


def print_monthly_summary(expenses):
    monthly_expenses = get_monthly_expenses(expenses)
    summary = {}
    for month, expenses in monthly_expenses.items():
        summary[month] = sum(expense["amount"] for expense in expenses)
        print(f"{month:<15}: ${summary[month]:.2f}")


def get_valid_description():
    while True:
        try:
            description = input(f"{"Enter Description":<15}: ").capitalize()
            if (len(description) < 2):
                raise ValueError(
                    "Description must be greater than two characters! Try Again..")
            return description
        except ValueError as e:
            print(e)


def get_valid_amount():
    while True:
        try:
            amount = float(input(f"{'Enter amount':<15}: "))
            if (amount <= 0):
                print("Amount must be greater than zero! Try Again..\n")
                continue
            return amount
        except ValueError:
            print("Invalide Value! Try Again..\n")


def get_valid_category():
    valid = ['Food', 'Transport', 'Entertainment', 'Other']
    while True:
        category = input(f"{'Enter category':<15}: ").capitalize()
        if len(category) < 2:
            print("Category must be at least 2 characters. Try again.")
            continue
        if category not in valid:
            print("Category set to 'Other'.\n")
            category = "Other"
        return category


def add_expense(expenses, description, amount, category="Other"):
    current_datetime = str(datetime.now().strftime("%Y-%m-%d %H-%M"))
    new_expense = {
        "date": current_datetime,
        'description': description,
        'amount': amount,
        'category': category
    }
    expenses.append(new_expense)
    save_expenses([new_expense], filename='data.csv')


def load_expenses(filename):
    expenses = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            expenses = [{
                "date": row['date'],
                'description': row['description'],
                'amount': float(row['amount']),
                'category': row['category']
            } for row in reader]

    except FileNotFoundError:
        print("No expenses file found — starting fresh.")
    except PermissionError:
        print("Can't read that file — permission denied.")

    finally:
        return expenses


def save_expenses(expenses, filename):
    file_exists = os.path.isfile(filename)

    with open(filename, "a", newline="") as file:
        fieldnames = ["date", "description", "amount", "category"]
        writer = csv.DictWriter(file, fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerows(expenses)
    print(f"✅ Expense added successfully.")


def get_total_spending(expenses):
    return sum(expense['amount'] for expense in expenses)


def get_spending_by_category(expenses):
    summary = {}
    for expense in expenses:
        cat = expense["category"]
        if cat not in summary:
            summary[cat] = 0
        summary[cat] += expense["amount"]
    return summary


def get_monthly_expenses(expenses):
    monthly_expenses = {}
    for expense in expenses:
        month = datetime.strptime(
            expense["date"], "%Y-%m-%d %H-%M").strftime("%B")
        if month not in monthly_expenses:
            monthly_expenses[month] = []
        monthly_expenses[month].append(expense)
    return monthly_expenses
