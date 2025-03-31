import traceback
import csv
import os
import custom_module
from datetime import datetime

# Task 2: Read a CSV File
def read_employees():
    data = {}
    rows = []
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            first = True
            for row in reader:
                if first:
                    data["fields"] = row
                    first = False
                else:
                    rows.append(row)
                data["rows"] = rows
            return data
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

employees = read_employees()
print(employees)


# Task 3: Find the Column Index
def column_index(string):
    return employees["fields"].index(string)

employee_id_column = column_index("employee_id")
print(employee_id_column)


# Task 4: Find the Employee First Name
def first_name(row_number):
    first_name_index = column_index("first_name")
    row = employees["rows"][row_number]
    return row[first_name_index]

print(first_name(0))


# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches
print(employee_find(17))


# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches
print(employee_find_2(17))


# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_index])
    return employees["rows"]
sort_by_last_name()
print("Sorted by last name", employees)


# Task 8: Create a dict for an Employee
def employee_dict(row):
    employee_data = {}
    for field, value in zip(employees["fields"][1:], row[1:]):
        employee_data[field] = value
    return employee_data
test_row = employees["rows"][0]
print("employee dict", employee_dict(test_row))


# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        employee_id = row[0]
        result[employee_id] = employee_dict(row)
    return result
all_employees = all_employees_dict()
print("all employees: ", all_employees)


# Task 10: Use the os Module
def get_this_value():
    return os.getenv("THISVALUE")
print(get_this_value())


# Task 11: Creating Own Module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
set_that_secret("noSecret")
print("Secret is: ", custom_module.secret)


# Task 12: Read minutes1.csv & minutes2.csv
def read_minutes():
    def read_files(file_path):
        with open(file_path, 'r', newline="") as file:
            reader = csv.reader(file)
            data = {"fields":next(reader), "rows": [tuple(row) for row in reader]}
        return data
    
    minutes1 = read_files('../csv/minutes1.csv')
    minutes2 = read_files('../csv/minutes2.csv')
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(f"Minutes1: {minutes1}, Minutes2: {minutes2}")


# Task 13: Create minutes_set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)

minutes_set = create_minutes_set()
print("Minutes set ", minutes_set)

# Task 14: Convert to datetime
def create_minutes_list():
    minutes_list = list(minutes_set)
    converted_list = map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list)
    return list(converted_list)
    
minutes_list = create_minutes_list()
print("Converted to datetime: ", minutes_list)


# Task 15: Write Out Sorted List
def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    converted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list))
    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)
    return converted_list
written_minutes_list = write_sorted_list()
print("Written Minutes List: ", written_minutes_list)
