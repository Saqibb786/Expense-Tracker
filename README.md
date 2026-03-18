# Personal Expense Tracker

A lightweight command-line expense manager built with Python.

Track spending, maintain your running balance, and review summaries by category and month. Data is stored locally in CSV files so you can keep things simple and transparent.

## Features

- Add expenses with description, amount, category, and timestamp.
- Add money to your balance whenever needed.
- View your current balance and total spending.
- List all recorded expenses for the active username.
- View category-wise spending summary.
- View monthly spending summary.
- Delete a previously added expense by description.
- Persist data between runs using local CSV files.

## Menu Options

When the program starts, you can choose:

- `1` Add expense
- `2` Add balance
- `3` View balance
- `4` View all expenses
- `5` View total by category
- `6` View monthly summary
- `7` Delete expense
- `0` Exit

## Project Structure

```text
.
|-- main.py        # Entry point and username prompt
|-- expenses.py    # ExpenseTracker class and business logic
|-- README.md
|-- LICENSE
```

## Requirements

- Python 3.10+
- No external dependencies (uses only Python standard library)

## Run Locally

1. Open the project folder in terminal.
2. Run:

```bash
python main.py
```

3. Enter a username and use the menu.

## Data Files

The app creates these files automatically in the project root:

- `data.csv`: stores all expense rows (`name,date,description,amount,category`)
- `balance.csv`: stores per-user balance (`name,balance`)

These files are meant to be generated runtime data and are usually ignored by Git via `.gitignore`.

## Example Workflow

```text
Enter Username : Saqib
Enter choice (0-7): 2
Enter amount   : 100
Enter choice (0-7): 1
Enter Description: Tea
Enter amount   : 20
Enter category : Food
Enter choice (0-7): 3
Enter choice (0-7): 0
```

## Notes

- Username matching is case-insensitive on input because the app normalizes names with capitalization.
- Invalid category values are automatically set to `Other`.
- If no CSV exists yet, the app starts with empty data.

## Troubleshooting

- If `python` is not recognized, use your full Python path or reinstall Python with "Add to PATH" enabled.
- If CSV files appear in Git, ensure they were not previously tracked. If they were, untrack once with:

```bash
git rm --cached data.csv balance.csv
```

## License

This project is licensed under the MIT License. See `LICENSE` for details.
