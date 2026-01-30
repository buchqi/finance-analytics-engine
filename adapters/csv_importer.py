import csv
from core.models import Transaction
from core.datastructures import TransactionDataset

class CSVImporter:
    @staticmethod
    def load(filepath:str):
        #create dataset
        dataset = TransactionDataset()
        #open file
        with open(filepath,newline='',encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transaction = Transaction(row["date"],row["category"],row["description"],float(row["amount"]),row["transaction_type"],'temp')
                dataset.add_transaction(transaction)
        
        return dataset
    
