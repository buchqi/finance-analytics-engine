from adapters.csv_importer import CSVImporter
from adapters.csv_exporter import CSVExporter

dataset = CSVImporter.load("transactions_test.csv")
dataset.iterate_transactions()  # debug print
CSVExporter.save(dataset, "transactions_exported.csv")