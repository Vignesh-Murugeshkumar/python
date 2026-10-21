try:
    a=5/0
except ZeroDivisionError as e:  
    print("Error: Division by zero")
    print(e)
try:
    b=a+4
except TypeError as e:
    print("Error: Type error")
    print(e)
else:
    print("No error occurred")
finally:
    print("Execution completed")