from managers.expense_manager import Expense_manager
from datetime import datetime

# --------------------- Utilities ---------------------


def print_header(title):
    print(f"\n--- {title} ---")


def print_all_expenses(tracker: Expense_manager):
    if not tracker.expenses:
        print("No expenses recorded yet.\n")
        return
    for expense in tracker.expenses:
        print(expense)
    print("_"*25)
    print(f"{'TOTAL SPENDING':<15}= ${tracker.get_total_spending():.2f}")


def print_spending_by_category(tracker: Expense_manager):
    if not tracker.expenses:
        print("No expenses recorded yet.\n")
        return
    summary = tracker.get_spending_by_category()
    for key, value in summary.items():
        flag = "⚠️" if value > 100 else ""
        print(f"{key:<15}: ${value:.2f} {flag}")


def print_monthly_summary(tracker: Expense_manager):
    if not tracker.expenses:
        print("No expenses recorded yet.\n")
        return
    monthly_expenses = tracker.get_monthly_expenses()
    summary = {}
    for month, expenses in monthly_expenses.items():
        summary[month] = sum(expense.amount for expense in expenses)
        print(f"{month:<15}: ${summary[month]:.2f}")

# --------------------- INPUTS ---------------------


def get_valid_name():
    while True:
        name = input(
            f"{'Enter Name':<15}: ").strip().capitalize()
        if len(name) < 2:
            print("Name must be greater than two characters! Try Again..")
            continue
        return name


def get_valid_amount():
    while True:
        try:
            amount = float(input(f"{'Enter amount':<15}: ").strip())
            if amount <= 0:
                print("Amount must be greater than zero! Try Again..")
                continue
            return amount
        except ValueError:
            print("Invalid Value! Try Again..")


def get_valid_category():
    while True:
        category = input(f"{'Enter category':<15}: ").strip().capitalize()
        if len(category) < 2:
            print("Category must be at least 2 characters. Try again.")
            continue
        return category


def get_valid_date():
    while True:
        date_text = input(f"{'Enter date (YYYY-MM-DD)':<15}: ").strip()
        try:
            return datetime.strptime(date_text, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")


# --------------------- UI ---------------------
def print_menu():
    print_header("Menu")
    print('1. Add expense')
    print('2. View all expenses')
    print('3. View total by category')
    print('4. View monthly summary')
    print('5. Delete Expense')
    print('6. Exit')


def run(tracker: Expense_manager):
    print("-"*50)
    print(f"{'EXPENSE TRACKER':^50}")
    print("-"*50)
    while True:
        print_menu()
        choice = input('Enter choice (1-6): ').strip()
        if choice == '1':
            # get input, call add_expense
            print_header("Add Expense")
            name = get_valid_name()
            amount = get_valid_amount()
            category = get_valid_category()
            tracker.add_expense(name, amount, category)
            print("✅ Expense added successfully.")

        elif choice == '2':
            # call display_all
            print_header("View All Expenses")
            print_all_expenses(tracker)
            print('')
        elif choice == '3':
            # get category, call get_category_total
            print_header("Spending By Category")
            print_spending_by_category(tracker)
            print('')
        elif choice == '4':
            # call get_monthly_summary
            print_header("Spending By Month")
            print_monthly_summary(tracker)
            print('')
        elif choice == '5':
            print_header("Delete Expense")
            if tracker.expenses:
                name = get_valid_name()
                date = get_valid_date()
                deleted_count = tracker.delete_expense(name, date)
                if deleted_count:
                    print(f"✅ Deleted {deleted_count} expense(s).")
                else:
                    print("No expense found for that name and date!")
            else:
                print("No expenses recorded yet.\n")
            print('')
        elif choice == '6':
            print('GoodBye 😊')
            break
        else:
            print("Invalid Choice! Try Again..\n")


def main():
    tracker = Expense_manager()
    run(tracker)


if __name__ == "__main__":
    main()
