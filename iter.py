from itertools import product, permutations, combinations,accumulate,groupby
a= [1,2,3]
b= [4,5,6]
#product
prod=product(a,b,repeat=2)
print("Product of a and b with repeat=2:")
print(list(prod))
#permutations
print("Permutations of a:")
perm=permutations(a)
print(list(perm))
print("Permutations of a taken 2 at a time:")
prrem2=permutations(a,2)
print(list(prrem2))
#combinations
print("Combinations of a:")
comb=combinations(a,2)
print(list(comb))
#accumulate
print("Accumulate of a:")
acc=accumulate(a)
print(list(acc))
acc1=accumulate(a,func=max)
print(list(acc1))
#groupby
def key(x):
    return x%2==0   
print("Groupby of a:")
group=groupby(a,key=key)
for k,v in group:
    print(k,list(v))
group1=groupby(a,key=lambda x:x%2==0)
print("Groupby of a with lambda:")
for k,v in group1:
    print(k,list(v))    