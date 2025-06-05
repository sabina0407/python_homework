# Task 2: A Decorator that Takes an Argument

# Defining the type_converter decorator
def type_converter(type_of_output): # This decorator takes a type as an argument
    def decorator(func): # This is the decorator that takes function being decorated
        def wrapper(*args, **kwargs): # This function runs the function and converts the result
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

# Creates and decorates return_int & return_string
@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string():
    return 'not a number'

# Testing the decorated functions
if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__)  # This should print 'str'

    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!")  # This is what should happen