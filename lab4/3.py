a=set(input().split())
b=set(input().split())
c=a&b
print(*sorted(c, key=int))