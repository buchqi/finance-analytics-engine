"building double linked list to help me store transaction collections"

import core.algorithms as algorithms
from datetime import date


class Node:
    def __init__(self,transaction,next = None,prev = None):
        self.transaction = transaction
        self.next = next 
        self.prev = prev

class Dll_skeleton:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def add_node(self,node):
        #"adds already existing node at the end"
        if self.head is None:
            self.head = self.tail = node
            self.size += 1
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.size +=1
    def remove_node(self,node):
        #'removes exsisting node from list'
        if self.head is None:
            return 
        current = self.head
        while current:
            if current == node:
                #target node is head 
                if current == self.head:
                    self.head = current.next
                    self.head.prev = None
                    self.size -=1
                    return
                #target node is tail
                if current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                    self.size -= 1
                    return

                #normal situtatiin
                current.prev.next = current.next
                current.next.prev = current.prev
                self.size -=1
                return
            current = current.next
    
    def iterate(self):
        if self.head is None:
            return 
        current = self.head
        while current:
            print(current.transaction)
            current = current.next
    
class TransactionDataset:
    def __init__(self):
        #wrap transactionDataset with DLL for better user experiennce
        self.dll = Dll_skeleton()
        
    def add_transaction(self,transaction):
        #calling DLL method to add transaction
        node = Node(transaction)
        self.dll.add_node(node)
    def iterate_transactions(self):
        #calling dll method to iterate throut our transaction dataset
        self.dll.iterate()
    def total_income(self):
        #calculating total income of our transactions
        if self.dll.head is None:
            return
        total = 0
        current = self.dll.head
        while current:
            #iterate throuout dataset and suming up only transaction type == income 
            if current.transaction.transaction_type =='income':
                total += current.transaction.amount
            current = current.next
        return total
    def total_expense(self):
        if self.dll.head is None:
            return 0
        current = self.dll.head
        total = 0
        #iterate trought dataset and sum of only transaction which has type expense
        while current:
            if current.transaction.transaction_type == 'expense':
                total += current.transaction.amount
            current = current.next
        return total
    def balance(self):
        return self.total_income() + self.total_expense()
    
    def sort_by_amount(self):
        # sort all transactions by amount, using the algorithm in algorithms.py
        return algorithms.sort_by_amount(self.dll)
    
    def sort_by_date(self):
        # sort transactions by date, algorithm from algorithms.py
        algorithms.sort_by_date(self.dll)
    
    def search_by_id(self, t_id):
        # search for a transaction by its ID, returns the first one found
        return algorithms.search_by_id(self.dll,t_id)
    
    def search_by_date(self, date: date):
        # search for the first transaction on a specific date
        return algorithms.search_by_date(self.dll,date)
    
    def search_by_category(self, category: str):
        # search for the first transaction in the given category
        return algorithms.search_by_category(self.dll,category)
        
    def search_by_type(self,t_type):
        return algorithms.search_by_type(self.dll,t_type)
    
    def filter_by_amount(self, amount: float):
        # get all transactions with this exact amount
        return algorithms.filter_transactions(self.dll,lambda t: t.amount == amount)
    
    def filter_by_date(self, date: date):
        # get all transactions on this date
        return algorithms.filter_transactions(self.dll,lambda t: t.transaction_date == date)
    
    def filter_by_category(self, category):
        # get all transactions in this category
        return algorithms.filter_transactions(self.dll,lambda t: t.category == category)
    
    def filter_by_date_range(self,start_date:date,end_date:date):
       """filter out by range,call filter transaction functin and give him lambda function as argument,condition_fc should always
       return True or False,"""
       return algorithms.filter_transactions(self.dll,lambda t: start_date <=t.transaction_date <=end_date )
   
    def filter_by_amount_range(self,min_amount,max_amount):
        return algorithms.filter_transactions(self.dll,lambda t: min_amount<= t.amount <=max_amount)
    
    
            
        
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    