from expenses import ExpenseTracker


def main():
    tracker = ExpenseTracker(name="Saqib", filename="data.csv")
    tracker.run()
    # print(tracker)


if __name__ == "__main__":
    main()
