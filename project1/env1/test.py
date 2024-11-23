import pandas as pd

# step 1: Create a Dataframe
data = {
    'Name' : ['alice','Bob','Charlie'],
    'Age' : [25,30,35],
    'City' : ['new York','Los Angles','Chiago']
}

df = pd.DataFrame(data)

# Step 2: Display the dataFrame
print('Original dataFrame:') 
print(df)

# dsep 3: Access specific columns
print("\nAccess the 'Name' column:'")
print(df['Name'])

# Step 4: Access specific rows using iloc
print("\nAccess the second row using iloc:")
print(df.iloc[1])

# Step 5: Add a new column
df['Salary'] = [70000,80000,75000]
print("\nDataFrame after adding a new column 'Salary':")
print(df)

# step 6: Filter rows based on a condition
filtered_df = df[df['Age']>28]
print("\nFiltered dataFrame where Age > 28:")
print(filtered_df)

# Step 7:Calculate theaverage salary
average_salary = df['Salary'].mean()
print(f"\nAverage Salary: {average_salary}")