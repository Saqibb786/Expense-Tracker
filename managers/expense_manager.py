

class Expense_manager:

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
        with open(self.filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            other_rows = [row for row in reader if row.get(
                "name") != self.name]

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
