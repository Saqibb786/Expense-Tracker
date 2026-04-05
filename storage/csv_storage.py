from models.expense import Expense


class CSV_storage:
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
