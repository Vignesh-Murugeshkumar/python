import sys
def mygenerator():
    yield 1
    yield 2
    yield 3
my_gen=mygenerator()
sorted_list=sorted(my_gen)
print(sorted_list)

def countdow(n):
    print("starting to count down from",n)
    while n>0:
        yield n
        n-=1
    print("Countdown finished.")
print(countdow(5))
value=countdow(5)

print(next(value))
print(next(value))
print(next(value))

def firstn(n):
    nums=[]
    num=0
    while num<n:
        nums.append(num)
        num+=1
    return nums

my_list=firstn(5)
print(my_list)

def firstn_generator(n):
    no=0
    while no<n:
        yield no
        no+=1
print(list(firstn_generator(5)))
print(sum(firstn_generator(10)))
print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))


def fib(n):
    a,b=0,1
    while a<n:
        yield a
        a,b=b,a+b
    return a
print(list(fib(10)))

