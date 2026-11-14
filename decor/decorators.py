import functools
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting the function...")
        result = func(*args, **kwargs)
        print("Ending the function...")
        return result
    return wrapper
@start_end_decorator    
def print_name(name):
    print(f"Hello, {name}!")

name = "Alice"
print_name(name)
print(help(print_name))
print(print_name.__name__)



def repeat_decorator(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat_decorator(3)
def greet(name):
    print(f"Hello, {name}!")

name = "Bob"
greet(name)