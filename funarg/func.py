def print_name(name):
    print(f"Hello, {name}!")
print_name("Alice")
number=0
def foo(a,b,c,d=4):
    print(a,b,c,d)
foo(1,2,3)
foo(a=2,b=3,c=1)
foo(1,2,3,5)
my_list = [1, 0, 3]
foo(*my_list)
my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict)
"""
def goo(a,b,*args,**kwargs):
    print(a,b,args,kwargs)
    for i in args:
        print("arg:", i)
    for key, value in kwargs.items():
        print("kwarg:", key, value)
goo(1,2,3,4,5,x=10,y=20)
"""

def loo():
    x=number
    print("num in loo:",x)
loo()