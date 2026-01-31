import argparse
from datetime import datetime

from adapters.csv_importer import CSVImporter
from adapters.csv_exporter import CSVExporter
from core.datastructures import TransactionDataset


def parse_date(date_str):
    """Convert a string (YYYY-MM-DD) to a datetime.date object."""
    return datetime.strptime(date_str, "%Y-%m-%d").date()


def run_command(args):
    # Load the CSV file into a dataset
    dataset: TransactionDataset = CSVImporter.load(args.input)
    print("Dataset loaded successfully.")

    # Sort the dataset if requested
    if args.sort:
        if args.sort == "amount":
            dataset.sort_by_amount()
            print("Dataset sorted by amount.")
        elif args.sort == "date":
            dataset.sort_by_date()
            print("Dataset sorted by date.")

    # Apply filters one by one. Each filter rebuilds the dataset.
    if args.filter_category:
        transactions = dataset.filter_by_category(args.filter_category)
        dataset = TransactionDataset()
        for t in transactions:
            dataset.add_transaction(t)
        print(f"Filtered dataset by category: {args.filter_category}")

    if args.filter_type:
        transactions = dataset.search_by_type(args.filter_type)
        dataset = TransactionDataset()
        # search_by_type might return a single transaction or a list
        if isinstance(transactions, list):
            for t in transactions:
                dataset.add_transaction(t)
        else:
            dataset.add_transaction(transactions)
        print(f"Filtered dataset by type: {args.filter_type}")

    if args.filter_amount is not None:
        transactions = dataset.filter_by_amount(args.filter_amount)
        dataset = TransactionDataset()
        for t in transactions:
            dataset.add_transaction(t)
        print(f"Filtered dataset by exact amount: {args.filter_amount}")

    if args.filter_amount_range:
        min_a, max_a = args.filter_amount_range
        transactions = dataset.filter_by_amount_range(min_a, max_a)
        dataset = TransactionDataset()
        for t in transactions:
            dataset.add_transaction(t)
        print(f"Filtered dataset by amount range: {min_a} - {max_a}")

    if args.filter_date:
        date = parse_date(args.filter_date)
        transactions = dataset.filter_by_date(date)
        dataset = TransactionDataset()
        for t in transactions:
            dataset.add_transaction(t)
        print(f"Filtered dataset by date: {date}")

    if args.filter_date_range:
        start = parse_date(args.filter_date_range[0])
        end = parse_date(args.filter_date_range[1])
        transactions = dataset.filter_by_date_range(start, end)
        dataset = TransactionDataset()
        for t in transactions:
            dataset.add_transaction(t)
        print(f"Filtered dataset by date range: {start} - {end}")

    # Show analytics if requested
    if args.total_income:
        print("Total income:", dataset.total_income())
    if args.total_expense:
        print("Total expense:", dataset.total_expense())
    if args.balance:
        print("Balance:", dataset.balance())

    # Print all transactions if requested
    if args.print_dataset:
        print("Current transactions in dataset:")
        dataset.iterate_transactions()

    # Export dataset to CSV if an output path is given
    if args.export:
        CSVExporter.save(dataset, args.export)
        print(f"Dataset exported to {args.export}")


def main():
    parser = argparse.ArgumentParser(
        description="Finance Analytics Engine CLI"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Main command: run
    run_parser = subparsers.add_parser(
        "run", help="Import CSV, apply filters/sorts, print/export dataset"
    )

    # Required: CSV input file
    run_parser.add_argument("input", help="Path to input CSV file")

    # Sorting options
    run_parser.add_argument(
        "--sort",
        choices=["amount", "date"],
        help="Sort dataset by amount or date"
    )

    # Filtering options
    run_parser.add_argument("--filter-category", help="Keep only this category")
    run_parser.add_argument(
        "--filter-type", choices=["income", "expense"], help="Keep only income or expense transactions"
    )
    run_parser.add_argument("--filter-amount", type=float, help="Keep only transactions with this amount")
    run_parser.add_argument(
        "--filter-amount-range",
        nargs=2,
        type=float,
        metavar=("MIN", "MAX"),
        help="Keep only transactions within this amount range"
    )
    run_parser.add_argument("--filter-date", help="Keep only transactions on this date (YYYY-MM-DD)")
    run_parser.add_argument(
        "--filter-date-range",
        nargs=2,
        metavar=("START", "END"),
        help="Keep only transactions within this date range (YYYY-MM-DD)"
    )

    # Analytics flags
    run_parser.add_argument("--total-income", action="store_true", help="Show total income")
    run_parser.add_argument("--total-expense", action="store_true", help="Show total expense")
    run_parser.add_argument("--balance", action="store_true", help="Show balance")

    # Output options
    run_parser.add_argument("--print", dest="print_dataset", action="store_true", help="Print all transactions")
    run_parser.add_argument("--export", help="Export dataset to CSV file")

    args = parser.parse_args()

    if args.command == "run":
        run_command(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
