#1
import math
n=int(input())
print("input degree:",n)
print("Output :",math.radians(n))

#2

def trap(a,b,h):
    return (a+b)*h/2

a=int(input())
b=int(input())
h=int(input())

print("base fist value:",a)
print("base second value:", b)
print("expected output:", (a+b)*h/2)

#3
#import math 
side=int(input())
le=int(input())
s=side*le**2/(4* math.tan(math.pi/side))
print(int(s))

#4

m=float(input())
k=float(input())
print(m*k)