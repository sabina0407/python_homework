# Task 3: List Comprehensions Practice
import pandas as pd

# Read csv into a DataFrame
df = pd.read_csv('../csv/employees.csv')

# Creates full names using list comprehension
full_names = [row['first_name'] + ' ' + row['last_name'] for _, row in df.iterrows()] # df.iterrows -> returns (index, row) for each row

print("Full names: \n", full_names)

# Filters names that contain only letter 'e'
e_names = [name for name in full_names if 'e' in name.lower()]
print("Names containing 'e': \n", e_names)
