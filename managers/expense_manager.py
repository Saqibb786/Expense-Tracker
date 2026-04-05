from models.expense import Expense
from models.category import Category
from storage.csv_storage import CSV_storage


class Expense_manager:
    def __init__(self, storage=CSV_storage):
        self.storage = storage()
        self.expenses = self.storage.load_expenses()

    def add_expense(self, name, amount, category):
        new_expense = Expense(name, amount, category)
        self.expenses.append(new_expense)
        self.storage.save_expenses(self.expenses)

    def delete_expense(self, name):
        for i, expense in enumerate(self.expenses):
            if expense.name == name.capitalize():
                self.expenses.pop(i)
                self.storage.save_expenses(self.expenses)
                return True
        return False

    def get_total_spending(self):
        return sum(expense.amount for expense in self.expenses)

    def get_spending_by_category(self):
        summary = {}
        for expense in self.expenses:
            cat = expense.category.value
            summary[cat] = summary.get(cat, 0) + expense.amount
        return summary

    def get_monthly_expenses(self):
        monthly = {}
        for expense in self.expenses:
            month = expense.date_time.strftime("%B %Y")
            if month not in monthly:
                monthly[month] = []
            monthly[month].append(expense)
        return monthly
