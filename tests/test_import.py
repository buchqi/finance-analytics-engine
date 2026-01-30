from adapters.csv_importer import CSVImporter

# 1️⃣ Import CSV into dataset
dataset = CSVImporter.load("transactions_test.csv")

# 2️⃣ Debug print all transactions
print("=== Imported Transactions ===")
dataset.iterate_transactions()  # prints each transaction


