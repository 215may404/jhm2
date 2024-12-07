python3 -m venv env1
ls
source env1/bin/activate
pip3 install pandas

import pandas as pd 
'1' = ' Add Transaction'
'2' = 'Edit Transaction'
'3' = 'Delete Transaction'
'4' = 'View Summary'
'5' = 'Save and Exit'
  while
print("""
Personal Expense Tracker
  1. Add Transaction
  2. Edit Transaction 
  3. Delete transaction
  4. View Summary
  5. Save and Exit
  """)
input('Enter your choice:')
if input = '5'
  break
print('Save and Exit')
