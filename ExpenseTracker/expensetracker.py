import pandas as pd
columns = ['Date','Type','Description','Amount']
filename = 'expenses.csv' 
try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    df = pd.DataFrame(columns = columns)
    print('No file, please build a new file!')

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
        date = input("Enter date of expense (YYYY-MM-DD): ")
        trans_type = input("Enter type (expenses/income): ")
        description = input("Enter description of expense: ") 
        amount = float(input("Enter amount: "))
        df.loc[len(df)] = {'Date':date,'Type':trans_type,'Description':description,'Amount':amount} 
        df.to_csv(filename, index=False)
        
    elif choice == "2":
        print("edit transaction")
        print(df)
        index = int(input("enter the edited tag:"))
        print(df.loc[index])
        new_date = input('New Date(Enter 保留原值):') or df.loc[index,'Date']
        new_type = input('New type(Enter 保留原值): ') or df.loc[index,'Type']
        new_descripition = input('New Descripitopn(Enter 保留原值):') or df.loc[index,'Description']
        new_amount = input('New Amount(Enter 保留原值):') or df.loc[index,'Amount']
        df.loc[index] = {'Date':new_date,'Type':new_type,'Description':new_descripition,'Amount':float(new_amount)}
        df.to_csv(filename, index=False)   
    elif choice == "3":
        print("delete transaction")
        index = int(input("enter the deleted tag:"))
        df = df.drop(index).reset_index(drop =True)
        df.to_csv(filename, index=False)
    elif choice == "4":
        print(df)

        total_expenses = df[df['Type'] == 'expenses']['Amount'].sum()
        total_income = df[df['Type'] == 'income']['Amount'].sum()
        savings = total_income - total_expenses
        if total_expenses == 0 and total_income == 0:print('no related record')
        else:
            print("records")
            print(f'toal expenses:{total_expenses}')
            print(f'total income:{total_income}')
            print(f'balance:{savings}')

    elif choice == "5":
        df.to_csv(filename, index=False)
        print("save and exit")
        break
    else:    
        print("Invalid choice, please try agian.")
