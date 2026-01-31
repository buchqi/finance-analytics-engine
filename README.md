# \# Finance Analytics Engine

# 

## Description

###### Finance Analytics Engine is a \*\*Python-based data processing project\*\* designed to manage and analyze financial transactions.  

###### 

###### Under the hood, it uses:  

###### 

###### \- \*\*Doubly Linked Lists (DLL)\*\* to store transactions efficiently in memory, enabling fast insertions, deletions, and iteration.  

###### \- \*\*Custom sorting algorithms\*\* to sort transactions by amount or date.  

###### \- \*\*Filtering functions\*\* that can filter transactions by category, type, amount, date, or ranges, leveraging higher-order functions (passing lambda conditions).  

###### \- \*\*Analytics calculations\*\* such as total income, total expense, and balance, performed directly on the in-memory dataset.  

###### \- \*\*CSV import/export adapters\*\* for flexible reading and writing of transaction data, converting strings from CSV into Python `datetime.date` and floats.  

###### \- \*\*Modular design\*\* separating core data structures (`TransactionDataset`, `Transaction`, DLL nodes) from CLI logic, making the backend reusable in other Python projects.  

###### 

###### This project is a \*\*hands-on example of implementing data structures, algorithms, and file I/O in Python\*\*, while providing a fully functional data pipeline for financial analytics.  

###### 

##### ---

### Ensure your CSV files follow this format:

###### date,category,description,amount,transaction\_type

###### 2026-01-01,Food,Lunch,15.0,expense

###### 2026-01-02,Salary,Monthly Salary,2000.0,income



##### 

##### +------------------------+-----------------+------------------------------------------+

##### | Flag                   | Type            | Description                              |

##### +------------------------+-----------------+------------------------------------------+

##### | input                  | positional      | Path to CSV file                          |

##### | --sort amount|date     | choice          | Sort dataset by amount or date           |

##### | --filter-category CAT  | string          | Filter by category (e.g., Food)          |

##### | --filter-type TYPE     | choice          | Filter by transaction type (income/expense) |

##### | --filter-amount AMT    | float           | Filter by exact amount                    |

##### | --filter-amount-range MIN MAX | float    | Filter by amount range                     |

##### | --filter-date YYYY-MM-DD       | string   | Filter by exact date                       |

##### | --filter-date-range START END  | string   | Filter by date range                       |

##### | --total-income         | flag            | Print total income                         |

##### | --total-expense        | flag            | Print total expense                        |

##### | --balance              | flag            | Print balance                              |

##### | --print                | flag            | Print current dataset                      |

##### | --export FILENAME      | string          | Export dataset to CSV file                 |

##### +------------------------+-----------------+------------------------------------------+

##### 

### Usage Examples

**Basic import + print**

python -m cli.main run transactions\_test.csv --print



**Sorting**

python -m cli.main run transactions\_test.csv --sort amount

python -m cli.main run transactions\_test.csv --sort date



**Filtering**

python -m cli.main run transactions\_test.csv --filter-category Food

python -m cli.main run transactions\_test.csv --filter-type income

python -m cli.main run transactions\_test.csv --filter-amount 25

python -m cli.main run transactions\_test.csv --filter-amount-range 10 100

python -m cli.main run transactions\_test.csv --filter-date 2026-01-02

python -m cli.main run transactions\_test.csv --filter-date-range 2026-01-01 2026-01-03



**Analytics**

python -m cli.main run transactions\_test.csv --total-income --total-expense --balance



**Export dataset**

python -m cli.main run transactions\_test.csv --export output.csv

# 

