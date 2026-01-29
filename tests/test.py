from datetime import date
from core.models import Transaction
from core.datastructures import TransactionDataset

# Create dataset
dataset = TransactionDataset()

# Add transactions
t1 = Transaction(date(2026,1,1), "Food", "Lunch", 15.0, "expense", "T001")
t2 = Transaction(date(2026,1,2), "Salary", "January Salary", 2000.0, "income", "T002")
t3 = Transaction(date(2026,1,2), "Food", "Dinner", 25.0, "expense", "T003")
t4 = Transaction(date(2026,1,3), "Investment", "Stocks", 500.0, "income", "T004")
t5 = Transaction(date(2026,1,2), "Foadsdod", "df", 25.0, "income", "df")

for t in [t1, t2, t3, t4,t5]:
    dataset.add_transaction(t)

# Test iteration
print("All transactions:")
dataset.iterate_transactions()

# Test totals
print("Total income:", dataset.total_income())
print("Total expense:", dataset.total_expense())
print("Balance:", dataset.balance())

# Test sorting
dataset.sort_by_amount()
print("\nAfter sort by amount:")
dataset.iterate_transactions()

dataset.sort_by_date()
print("\nAfter sort by date:")
dataset.iterate_transactions()

# Test searching
print("\nSearch by ID T003:", dataset.search_by_id("T003"))
print("Search by category 'Food':", dataset.search_by_category("Food"))
print("Search by type 'income':", dataset.search_by_type("income"))

# Test filtering
print("\nFilter by amount 25.0:", dataset.filter_by_amount(25.0))
print("Filter by category 'Food':", dataset.filter_by_category("Food"))
print("Filter by date range 2026-01-01 to 2026-01-02:", dataset.filter_by_date_range(date(2026,1,1), date(2026,1,2)))
print("Filter by amount range 10 to 1000:", dataset.filter_by_amount_range(10, 1000))
