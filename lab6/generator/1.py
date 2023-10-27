#1
def squares(n):
    for i in range(n):
        yield i**2
        
a = squares(5)
for i in a:
    print(i)

#2
def even(n):
    for i in range(n):
        if i%2==0:
            yield i

n=int(input())
n=even(n)
for i in n:
    print(i)

#3
def divisible(n):
    for i in range(n):
        if i%4==0 and i%3==0:
            yield i
    

n=divisible(90)
for i in n:
    print(i)

#4

def sq(a,b):
    for i in range(a,b):
        yield i**2

n=sq(4,15)
for i in n:
    print(i)

#5
def rev(n):
    for i in range(n,-1,-1) : 
        yield i

n=rev(5)
for i in n:
    print(i)