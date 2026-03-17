from expenses import ExpenseTracker


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
