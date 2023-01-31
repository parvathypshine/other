# l= [1, 4, 2, 9,4 ,7,4, 8, 9, 3, 1]
# t=set(l)

# for i in t:
   
#     x=l.count(i)
    
#     print(i,"=",x,"times")
# l1=[1,2]
# l2=[3,4]
# print(l1+l2)

# import numpy as np
# x=int(input("enter"))
# rev=0
# y=x
# while x>0:
#     n=x%10
#     rev=rev+n*n*n
#     x=n//10
# if  y==rev:
#     print("y")
# else:
#     print("n")


x=int(input("enter"))
f=0
for i in range(1,x+1):
    if x%i==0:
        f=f+1
if f==2:
    print("P")
else:
    print("n")