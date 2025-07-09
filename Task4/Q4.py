""" Write a decorator function that prints the execution time of the decorated function. """

import time
def calculate_time_decorator(function):
    def wrapper(*args, **kwargs):
        starting_time = time.time()
        result = function(*args, **kwargs)
        ending_time = time.time()
        duration = ending_time - starting_time
        print(f"Execution time of '{function.__name__}': {duration:.6f} seconds")
        return result
    return wrapper

@calculate_time_decorator
def say_hello():
    time.sleep(1)
    print("Hello!")
say_hello()