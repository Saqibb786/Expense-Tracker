from datetime import datetime
import csv
import os


class ExpenseTracker:
    def __init__(self, name, filename="data.csv"):
        self.filename = filename
        self.name = name.capitalize()
        self.expenses = self.load_expenses()
        self.balance = self.load_balance()

    def __str__(self):
        return f"Hello 👋🏻 {self.name} your total spending is ${self.get_total_spending():.2f} and you balance is ${self.balance:.2f}"

    def print_menu(self):
        print('='*30)
        print(f"{self.name}'s EXPENSE TRACKER")
        print('='*30)
        print('1. Add expense')
        print('2. Add Balance')
        print('3. View Balance')
        print('4. View all expenses')
        print('5. View total by category')
        print('6. View monthly summary')
        print('7. Delete Expense')
        print('0. Exit')

    def print_header(self, title):
        print(f"\n--- {title} ---")

    def print_all_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.\n")
            return
        for expense in self.expenses:
            print(f"{expense['description']:<15}: ${expense['amount']:.2f}")
        print(f"{'TOTAL SPENDING':<15}= ${self.get_total_spending():.2f}")

    def print_current_balance(self):
        if self.balance == 0:
            print(
                f"Your account is empty ☹️  ${abs(self.balance):.2f} so far you spended ${self.get_total_spending():.2f}")
        elif self.balance < 0:
            print(
                f"You are under debt 🤯  of ${abs(self.balance):.2f} so far you spended ${self.get_total_spending():.2f}")
        else:
            print(
                f"Hello 👋🏻 {self.name} your balance is ${self.balance:.2f} so far you spended ${self.get_total_spending():.2f}")

    def print_spending_by_category(self):
        if not self.expenses:
            print("No expenses recorded yet.\n")
            return
        summary = self.get_spending_by_category()
        for key, value in summary.items():
            flag = "⚠️" if value > 100 else ""
            print(f"{key:<15}: ${value:.2f} {flag}")

    def print_monthly_summary(self):
        if not self.expenses:
            print("No expenses recorded yet.\n")
            return
        monthly_expenses = self.get_monthly_expenses()
        summary = {}
        for month, expenses in monthly_expenses.items():
            summary[month] = sum([expense["amount"] for expense in expenses])
            print(f"{month:<15}: ${summary[month]:.2f}")

    def get_valid_description(self):
        while True:
            description = input(
                f"{'Enter Description':<15}: ").strip().capitalize()
            if len(description) < 2:
                print("Description must be greater than two characters! Try Again..")
                continue
            return description

    def get_valid_amount(self):
        while True:
            try:
                amount = float(input(f"{'Enter amount':<15}: ").strip())
                if amount <= 0:
                    print("Amount must be greater than zero! Try Again..")
                    continue
                return amount
            except ValueError:
                print("Invalid Value! Try Again..")

    def get_valid_category(self):
        valid = ['Food', 'Transport', 'Entertainment', 'Other']
        while True:
            category = input(f"{'Enter category':<15}: ").strip().capitalize()
            if len(category) < 2:
                print("Category must be at least 2 characters. Try again.")
                continue
            if category not in valid:
                print("Category set to 'Other'.\n")
                category = "Other"
            return category

    def add_expense(self):
        current_datetime = str(datetime.now().strftime("%Y-%m-%d %H-%M"))
        description = self.get_valid_description()
        amount = self.get_valid_amount()
        category = self.get_valid_category()

        new_expense = {
            "name": self.name,
            "date": current_datetime,
            'description': description,
            'amount': amount,
            'category': category
        }

        self.expenses.append(new_expense)
        self.save_expenses([new_expense])
        self.balance -= amount
        self.save_balance()
        print(f"✅ Expense added successfully.")

    def delete_expense(self):
        if not self.expenses:
            print("No expenses to delete.\n")
            return
        description = self.get_valid_description()
        # Find first matching expense in memory
        match_index = None
        for i, expense in enumerate(self.expenses):
            if expense["description"] == description:
                match_index = i
                break
        if match_index is None:
            print(f"No expense found for '{description}'.")
            return
        removed = self.expenses.pop(match_index)
        self.balance += float(removed["amount"])
        other_rows = []
        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)
                other_rows = [row for row in reader if row.get(
                    "name") != self.name]
        except FileNotFoundError:
            pass
        my_rows = [{"name": self.name, **expense}
                   for expense in self.expenses]
        self.save_expenses(other_rows + my_rows,
                           mode='w', header=True)
        self.save_balance()
        print(
            f"🗑️ Deleted expense: {removed['description']} (${removed['amount']:.2f})")

    def add_balance(self):
        self.balance += self.get_valid_amount()
        self.save_balance()

    def load_expenses(self):
        expenses = []
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["name"] == self.name:
                        expenses.append({
                            "date": row['date'],
                            'description': row['description'],
                            'amount': float(row['amount']),
                            'category': row['category']
                        })

        except FileNotFoundError:
            print("No expenses file found — starting fresh.")
        except PermissionError:
            print("Can't read that file — permission denied.")

        return expenses

    def save_expenses(self, expense, mode='a', header=False):
        file_exists = os.path.isfile(self.filename)

        with open(self.filename, mode, newline="") as file:
            fieldnames = ["name", "date", "description", "amount", "category"]
            writer = csv.DictWriter(file, fieldnames)
            if not file_exists or header:
                writer.writeheader()
            writer.writerows(expense)

    def load_balance(self, default_balance=0.0):
        try:
            with open("balance.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["name"] == self.name:
                        return float(row["balance"])
        except (FileNotFoundError, ValueError, KeyError):
            pass
        return float(default_balance)

    def save_balance(self):
        rows = []
        try:
            with open("balance.csv", "r", newline="") as file:
                reader = csv.DictReader(file)
                rows = list(reader)
        except FileNotFoundError:
            rows = []

        updated = False
        for row in rows:
            if row["name"] == self.name:
                row["balance"] = f"{self.balance:.2f}"
                updated = True
                break

        if not updated:
            rows.append({"name": self.name, "balance": f"{self.balance:.2f}"})

        with open("balance.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "balance"])
            writer.writeheader()
            writer.writerows(rows)

    def get_total_spending(self):
        return sum(expense['amount'] for expense in self.expenses)

    def get_spending_by_category(self):
        summary = {}
        for expense in self.expenses:
            cat = expense["category"]
            summary[cat] = summary.get(cat, 0) + expense["amount"]
        return summary

    def get_monthly_expenses(self):
        monthly = {}
        for expense in self.expenses:
            month = datetime.strptime(
                expense["date"], "%Y-%m-%d %H-%M").strftime("%B %Y")
            if month not in monthly:
                monthly[month] = []
            monthly[month].append(expense)
        return monthly

    def run(self):
        while True:
            self.print_menu()
            choice = input('Enter choice (0-7): ').strip()
            if choice == '1':
                # get input, call add_expense
                self.print_header("Add Expense")
                self.add_expense()

            elif choice == '2':
                self.print_header("Add Balance")
                self.add_balance()
                print("")
            elif choice == '3':
                self.print_header("View Balance")
                self.print_current_balance()
                print("")
            elif choice == '4':
                # call display_all
                self.print_header("View All Expenses")
                self.print_all_expenses()
                print('')
            elif choice == '5':
                # get category, call get_category_total
                self.print_header("Spending By Category")
                self.print_spending_by_category()
                print('')
            elif choice == '6':
                # call get_monthly_summary
                self.print_header("Spending By Month")
                self.print_monthly_summary()
                print('')
            elif choice == '7':
                self.print_header("Delete Expense")
                self.delete_expense()
                print('')
            elif choice == '0':
                print('GoodBye 😊')
                break
            else:
                print("Invalid Choice! Try Again..\n")
