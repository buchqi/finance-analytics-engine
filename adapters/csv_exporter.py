import csv
from core.datastructures import TransactionDataset

class CSVExporter:
    @staticmethod
    def save(dataset: TransactionDataset,filepath:str):
        with open(filepath,mode = 'w',newline ='',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['date','category','description','amount','transaction_type'])
            
            current = dataset.dll.head
            while current:
                t = current.transaction
                writer.writerow([t.transaction_date, t.category, t.description, t.amount, t.transaction_type])
                current = current.next