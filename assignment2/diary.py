# Task 1: Diary

import traceback

try:
    with open('diary.txt', 'a') as diary_file:
        first_input = True  
        while True:
            if first_input:
                user_input = input("What happened today? ")
                first_input = False 
            else:
                user_input = input("What else? ")
            
            diary_file.write(user_input + "\n")  
            
            if user_input == "done for now":  
                break  

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
