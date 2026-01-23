"all of the searching and sorting algorithms"
from datetime import date

def sort_by_amount(dll):
    q = dll.head
    while q:
        r = q.next
        while r:
            if r.transaction.amount<q.transaction.amount:
                r.transaction,q.transaction = q.transaction,r.transaction
            r = r.next
        q = q.next

def sort_by_date(dll):
    q = dll.head
    while q:
        r = q.next
        while r:
            if r.transaction.transaction_date < q.transaction.transaction_date:
                q.transaction,r.transaction = r.transaction,q.transaction
            r = r.next
        q = q.next
        
def search_by_id(dll,transaction_id:str):
    #returns node if found in DLL else returns None
    current = dll.head
    while current:
        if current.transaction.transaction_id == transaction_id:
            return current
        current = current.next
    return None

def search_by_date(dll,transaction_date:date):
    """Search nodes in TransactionDataset by date. Returns list of nodes if found, else None."""
    current = dll.head
    while current:
        if current.transaction.transaction_date == transaction_date:
            return current
        current = current.next
    return None

def search_by_category(dll,category:str):
    """Search nodes in TransactionDataset by category. Returns list of nodes if found, else None."""
    current = dll.head
    while current:
        if current.transaction.category == category:
            return current
        current = current.next
    return None

def search_by_type(dll,transaction_type):
    """Search nodes by type and return list of them if found, else return None """
    if transaction_type not in("income",'expense'):
        raise ValueError("transaction type must be  'income' or 'expense'")
    
    current = dll.head
    while current:
        if current.transaction.transaction_type == transaction_type:
            return current
        current = current.next
    return None

def filter_transactions(dll,condition_fn):
    """
Generic filter for transactions.
Returns a list of nodes where condition_fn(node.transaction) is True.
Example:
    TransactionDataset.filter_transactions(lambda t: t.amount > 100)
    TransactionDataset.filter_transactions(lambda t: t.category == "Food")
    TransactionDataset.filter_transactions(lambda t: t.transaction_type == "income")
"""
    results = []
    current = dll.head
    
    while current:
        if condition_fn(current.transaction):
            results.append(current)
        current = current.next
    return results

def filter_by_date_range(self,start_date:date,end_date:date):
    """filter out by range,call filter transaction functin and give him lambda function as argument,condition_fc should always
    return True or False,"""
    return self.filter_transactions(lambda t: start_date <=t.transaction_date <=end_date )

def filter_by_amount_range(self,min_amount,max_amount):
    return self.filter_transactions(lambda t: min_amount<= t.amount <=max_amount)

        







