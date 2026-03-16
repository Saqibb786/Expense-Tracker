import expenses as e
from datetime import datetime


def main():
    expenses = e.load_expenses(filename='data.csv')
    while True:
        e.print_menu()
        choice = input('Enter choice (1-5): ')
        if choice == '1':
            # get input, call add_expense
            e.print_header("Add Expense")
            description = e.get_valid_description()
            amount = e.get_valid_amount()
            category = e.get_valid_category()
            e.add_expense(expenses, description, amount, category)
            print('')
        elif choice == '2':
            # call display_all
            e.print_header("View All Expenses")
            e.print_all_expenses(expenses)
            print('')
        elif choice == '3':
            # get category, call get_category_total
            e.print_header("Spending By Category")
            e.print_spending_by_category(expenses)
            print('')
        elif choice == '4':
            # call get_monthly_summary
            e.print_header("Spending By Month")
            e.print_monthly_summary(expenses)
            print('')
        elif choice == '5':
            print('GoodBye 😊')
            break
        else:
            print("Invalid Choice! Try Again..\n")


if __name__ == "__main__":
    main()
