import functools
def repeat(num):
    def decorator(func):
        functools.wraps(func)
        def dec(*args,**kwargs):
            for _ in range(num):
                result=func(*args,**kwargs)
            return result
        return dec
    return decorator

@repeat(num=3)
def say_hello():
    print("Hello from decortest.py!")
say_hello()