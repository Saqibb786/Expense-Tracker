from models.expense import Expense
import csv


class CSV_storage:
    def __init__(self, filename="data.csv"):
        self.filename = filename
        self.fieldnames = ["name", "date_time", "amount", "category"]

    def load_expenses(self):
        expenses = []
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    expenses.append(Expense.from_csv_row(row))
        except FileNotFoundError:
            pass
        return expenses

    def save_expenses(self, expenses):
        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for expense in expenses:
                writer.writerow(expense.to_csv_row())
