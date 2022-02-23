import os
import sqlite3
from decimal import *
from typing import List, Dict

def execute_query(query_sql: str) -> List:
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql)
    return result

def get_sum_order_in_invoice() -> Decimal:
    query_sql = f'''
            SELECT UnitPrice,Quantity
              FROM invoice_items
    '''
    records = execute_query(query_sql)
    result = 0
    for record in records:
        result += Decimal(str(record[0])) * Decimal(str(record[1]))
    return result

def get_firstname_clone() -> Dict:
    query_sql = f'''
                SELECT FirstName
                  FROM customers
        '''
    records = execute_query(query_sql)
    result = dict()
    full_list_firstname = []
    for record in records:
        full_list_firstname.append(record[0])
    for e in set(full_list_firstname.copy()):
        if full_list_firstname.count(e) > 1:
            result[e] = full_list_firstname.count(e)
    return result

print(get_sum_order_in_invoice())
print(get_firstname_clone())
