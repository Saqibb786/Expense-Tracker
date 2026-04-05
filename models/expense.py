from datetime import datetime
from models.category import Category

import csv
import os


class Expense:
    def __init__(self, name, amount, category):
        self.name = name.capitalize()
        self.current_datetime = datetime.now()
        self.amount = amount
        if Category(category):
            self.category = Category(category)
        else:
            self.category = Category.OTHER

    def __str__(self):
        return f"{self.name} : ${self.amount:.2f} | Date: {self.current_datetime.strftime("%d %B %Y")}"
