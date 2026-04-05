from models.expense import ExpenseTracker


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
        summary[month] = sum(expense["amount"] for expense in expenses)
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


# def get_valid_category(self):
    # valid = ['Food', 'Transport', 'Entertainment', 'Other']
    # while True:
    #     category = input(f"{'Enter category':<15}: ").strip().capitalize()
    #     if len(category) < 2:
    #         print("Category must be at least 2 characters. Try again.")
    #         continue
    #     if category not in valid:
    #         print("Category set to 'Other'.\n")
    #         category = "Other"
    #     return category

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


def main():
    print("-"*50)
    print(f"{"PERSONAL EXPENSE TRANCKER":^50}")
    print("-"*50)

    username = input(f"{"Enter Username":<15}: ")

    tracker = ExpenseTracker(name=username, filename=f"data.csv")
    tracker.run()
    # print(tracker)


if __name__ == "__main__":
    main()
