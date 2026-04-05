from datetime import datetime
from models.category import Category


class Expense:
    def __init__(self, name, amount, category, date_time=datetime.now()):
        self.name = str(name).strip().capitalize()
        self.amount = float(amount)
        self.category = self._parse_category(category)
        self.date_time = date_time

    def __str__(self):
        return f"{self.name} : ${self.amount:.2f} | Date: {self.date_time.strftime('%d %B %Y')}"

    @staticmethod
    def _parse_category(category):
        if isinstance(category, Category):
            return category
        try:
            return Category(str(category).strip().capitalize())
        except ValueError:
            return Category.OTHER

    @classmethod
    def from_csv_row(cls, row: dict):
        return cls(
            name=row["name"],
            amount=float(row["amount"]),
            category=row["category"],
            date_time=datetime.fromisoformat(row["date_time"]),
        )

    @classmethod
    def to_csv_row(self):
        return {
            "name": self.name,
            "date_time": self.date_time.isoformat(),
            "amount": f"{self.amount:.2f}",
            "category": self.category.value,
        }
