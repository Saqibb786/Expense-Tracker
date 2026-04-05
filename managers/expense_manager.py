from models.expense import Expense
from storage.csv_storage import CSV_storage


class Expense_manager:
    def __init__(self, storage=CSV_storage):
        self.storage = storage()
        self.__expenses = self.storage.load_expenses()

    @property
    def expenses(self):
        return self.__expenses

    def add_expense(self, name, amount, category):
        new_expense = Expense(name, amount, category)
        self.__expenses.append(new_expense)
        self.storage.save_expenses(self.__expenses)

    def delete_expense(self, name, date):
        matched_expenses = []
        for expense in self.__expenses:
            if expense.name == name and expense.date_time.date() == date:
                matched_expenses.append(expense)
        if not matched_expenses:
            return 0

        self.__expenses = [
            expense for expense in self.__expenses if expense not in matched_expenses]
        self.storage.save_expenses(self.__expenses)
        return len(matched_expenses)

    def get_total_spending(self):
        return sum(expense.amount for expense in self.__expenses)

    def get_spending_by_category(self):
        summary = {}
        for expense in self.__expenses:
            cat = expense.category.value
            summary[cat] = summary.get(cat, 0) + expense.amount
        return summary

    def get_monthly_expenses(self):
        monthly = {}
        for expense in self.__expenses:
            month = expense.date_time.strftime("%B %Y")
            if month not in monthly:
                monthly[month] = []
            monthly[month].append(expense)
        return monthly
