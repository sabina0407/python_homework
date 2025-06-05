# Task 1: Writing and Testing a Decorator

import logging

logger = logging.getLogger(__name__ + '_parameter_log')
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler('./decorator.log', 'a'))

# Declare a decorator called logger_decorator. 
# function: <the function name> positional parameters: <a list of the positional parameters, or "none" if none are passed> keyword parameters: <a dict of the keyword parameters, or "none" if none are passed> return: <the return value>
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        positional_params = args if args else "none"
        keyword_params = kwargs if kwargs else "none"
        log_message = (
            f"function: {func.__name__} \n"
            f"positional parameters: {positional_params} \n"
            f"keyword parameters: {keyword_params} \n"
            f"return: {result}\n"
        )
        logger.log(logging.INFO, log_message)
        return result
    return wrapper

# 3 decorated test functions
@logger_decorator
def say_hello():
    print("Hello, World!")

@logger_decorator
def returns_true(*args):
    return True

@logger_decorator
def keyword_only(**kwargs):
    return logger_decorator

# Calling the decorated functions within the mainline code
if __name__ == "__main__":
    say_hello()
    returns_true(1, 2, 3)
    keyword_only(lesson="decorators", topic="Python")