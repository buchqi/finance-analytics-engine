"creating a domain model whichs represents one financal transaction and enforces basic rules"
from datetime import date


class Transaction:
    def __init__(self,transaction_date: date,category:str,description:str,amount:float,transaction_type:str):
        if amount <0:
            raise ValueError("Amount must be positive")
        if transaction_type not in ('income','expense'):
            raise ValueError("transaction type must be  'income' or 'expense")
        self.transaction_date = transaction_date
        self.category = category
        self.description = description
        self.amount = amount
        self.transaction_type = transaction_type
    
    def signed_amount(self):
        'return positive value for income and negative for expenses '
        return self.amount if self.transaction_type =='income' else -self.amount
    
    def __repr__(self):
        return (f'date:{self.transaction_date},category:{self.category},amount:{self.amount},type:{self.transaction_type}')
    
