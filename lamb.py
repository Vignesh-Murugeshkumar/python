from functools import reduce
add10 =lambda x: x+10
print(add10(5))
mul=lambda x,y: x*y
print( mul(5,6))

points2d=[(1,2),(5,4),(3,6)]

sorted_points2d=sorted(points2d,key=lambda x: x[1])
print(sorted_points2d)


a= [1,2,3,4,5]
b=map(lambda x:x*2,a)
print(list(b))

filter=filter(lambda x:x%2==0,a)
print(list(filter))

prod=reduce(lambda x,y:x*y,a)