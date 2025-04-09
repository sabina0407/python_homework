import pandas as pd

# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
# 1. Create a DataFrame from a dictionary:

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(data)
print("DataFrame from dictionary:")
print(task1_data_frame)

# 2. Add a new column:
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print("\nDataFrame with added Salary column:")
print(task1_with_salary)

# 3. Modify an existing column:
task1_older = task1_with_salary.copy()
task1_older['Age'] += 1
print("\nDataFrame with incremented Age column:")
print(task1_older)

# 4. Save the DataFrame as a CSV file:
task1_older.to_csv('employees.csv', index=False)
print("\nCSV file 'employees.csv' created.")


# Task 2: Loading Data from CSV and JSON
# 1. Read data from a CSV file:
task2_employees = pd.read_csv('employees.csv')
print("\nDataFrame loaded from CSV:")
print(task2_employees)

# 2. Read data from a JSON file:
json_employees = pd.read_json('additional_employees.json')
print("\nDataFrame loaded from JSON:")
print(json_employees)

# 3. Combine DataFrames:
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\nCombined DataFrame from CSV and JSON:")
print(more_employees)


# Task 3: Data Inspection - Using Head, Tail, and Info Methods
# 1. Use the head() method:
first_three = more_employees.head(3)
print("\nFirst three rows of the DataFrame:")
print(first_three)

# 2. Use the tail() method:
last_two = more_employees.tail(2)
print("\nLast two rows of the DataFrame:")
print(last_two)

# 3. Get the shape of a DataFrame:
employee_shape = more_employees.shape
print("\nShape of the DataFrame:")
print(employee_shape)

# 4. Use the info() method:
employee_info = more_employees.info()
print("\nDataFrame info:")
print(employee_info)


# Task 4: Data Cleaning
# 1. Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data:
dirty_data = pd.read_csv('dirty_data.csv')
print("\nDataFrame loaded from dirty_data.csv:")
print(dirty_data)

clean_data = dirty_data.copy()

# 2. Remove any duplicate rows from the DataFrame:
clean_data.drop_duplicates(inplace=True)
print("\nDataFrame after removing duplicates:")
print(clean_data)

# 3. Convert Age to numeric and handle missing values:
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("\nDataFrame after converting Age to numeric:")
print(clean_data)

# 4. Convert Salary to numeric & replace known placeholders with NaN:
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
print("\nDataFrame after converting Salary to numeric and replacing placeholders with NaN:")
print(clean_data)

# 5. Fill Age with mean and Salary with median:
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print("\nDataFrame after filling missing values:")
print(clean_data)

# 6. Convert Hire Date to datetime:
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print("\nDataFrame after converting Hire Date to datetime:")
print(clean_data)

# 7. Strip extra whitespace and standardize Name & Department as uppercase:
clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print("\nDataFrame after stripping whitespace and standardizing Name & Department:")
print(clean_data)