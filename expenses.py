def print_menu():
    print('1. Add expense')
    print('2. View all expenses')
    print('3. View total by category')
    print('4. View monthly summary')
    print('5. Exit')


def print_header(title):
    print(f"\n--- {title} ---")


def get_valid_description():
    while True:
        try:
            description = input(f"{"Enter Description":<15}: ").capitalize()
            if (len(description) < 2):
                raise ValueError(
                    "Description must be greater than two characters! Try Again..\m")
            return description
        except ValueError as e:
            print(e)


def get_valid_amount():
    while True:
        try:
            amount = float(input(f"{'Enter amount':<15}: "))
            if (amount < 0):
                print("Amount must be greater than zero! Try Again..\n")
                continue
            return amount
        except ValueError:
            print("Invalide Value! Try Again..\n")


def get_valid_category():
    valid = ['Food', 'Transport', 'Entertainment', 'Other']
    try:
        category = input(f"{'Enter category':<15}: ").capitalize()
        if category not in valid:
            print(
                "Category set to Other as its not in ('Food', 'Transport', 'Entertainment')\n")
            category = "Other"
        if (len(category) < 2):
            raise ValueError(
                "Category must be greater than two characters! Try Again..\n")
        return category
    except ValueError as e:
        print(e)


def add_expense(expenses, name, amount, category="Other"):
    expenses.append({
        'name': name,
        'amount': amount,
        'category': category
    })


# load_expenses(filename)   ← you already wrote this
# save_expenses(expenses, filename)  ← you already wrote this
# add_expense(expenses, name, amount, category)
# get_category_total(expenses, category)
# get_monthly_summary(expenses)
# display_all(expenses)
