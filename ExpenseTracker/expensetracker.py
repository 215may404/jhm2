import pandas as pd
columns = ["date","type","description","amount",]
try:
    df = pd.read_csv('expenses.csv')
except FileNotFoundError:
    df = pd.DataFrame(columns = columns)
    print('No file, please build a new file!')
filename = 'expenses.csv'
while True:
    print("""
Personal Expense Tracker
  1. Add Transaction
  2. Edit Transaction 
  3. Delete transaction
  4. View Summary
  5. Save and Exit
  """)
    choice = input("Please enter your choice (1-5): ")   
    if choice == "1":
        "date" == input("Enter date of expense (YYYY-MM-DD): ")
        "type" == input("Enter type (expenses/income): ")
        "description" == input("Enter description of expense: ") 
        "amount" == float(input("Enter amount: "))
        df.loc[len(df)] = {'Date':"date",'Description':"description",'Amount':"amount",'Type':"type"} 
    
    elif choice == "2":
        print("edit transaction")
        index = int(input("enter the edited tag:"))
        print(df.loc[index])
        new_date = input('New Date(enter original date):')
        new_descripition = input('New Descripitopn(enter original descripition):')
        new_amount = input('New Amount(enter original amount):')
        new_type = input('New type(enter original type): ')
        df.loc[index] = {'date':new_date,'description':new_descripition,'amount':new_amount,'type':new_type}
        
    elif choice == "3":
        print("delete transaction")
        index = int(input("enter the deleted tag:"))
        df = df.drop(index).reset_index(drop =True)
    elif choice == "4":
        total_expenses = df[df['type'] == 'expenses']['amount'].sum()
        total_income = df[df['type'] == 'income']['amount'].sum()
        if total_expenses == 0 and total_income == 0:print('no related record')
        else:
            print("records")
            savings = total_income - total_expenses
            print(f'toal expenses:{total_expenses}')
            print(f'total income:{total_income}')
            print(f'balance:{savings}')
        
    elif choice == "5":
        df.to_csv(filename, index=False)
        print("save and exit")
        break
    else:    
        print("Invalid choice, please try agian.")
