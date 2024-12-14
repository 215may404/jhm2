import pandas as pd
import csv
print("""
Personal Expense Tracker
  1. Add Transaction
  2. Edit Transaction 
  3. Delete transaction
  4. View Summary
  5. Save and Exit
  """)

description = ""
amount = ""
date_input = ""
expense_df = pd.DataFrame(columns=["Date","Description","Amount"])
choice = ""
while choice != "5":
    choice = input("Enter your choice: ")
    if choice == "1":
       description = input("Enter description of expense: ")
       amount = input("Enter amount: ")
       date_input = input("Enter date of expense (YYYY-MM-DD): ") 
       expense_df = pd.read_csv("expense.csv")
    elif choice == "2":
        print("edit transaction")
    elif choice == "3":
        print("delete transaction")
    elif choice == "4":
        print("Expense: ")
        print(expense_df)
    else:
        print("save and exit")
