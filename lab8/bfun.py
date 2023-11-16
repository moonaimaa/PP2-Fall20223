import math 
import string

mylist=[2,3,4,5,6]

print(math.prod(mylist))

print("A'ripterdi en'gizin'iz:", end=' ')
s=str(input())
upp,low=0,0
for i in range(len(s)):
    if ord(s[i])>=ord('A') and ord(s[i])<=ord('Z'):
        upp+=1
    elif ord(s[i])>=ord('a') and ord(s[i])<=ord('z'):
        low+=1
print(upp,low)

print("palindrome or not so'z jaz:", end=" ")
s=input()
rev=reversed(s)
pal="".join(rev)
print('YES is pal') if pal==s else print("NO")


import time
number = int(input("Sample Input:\n"))
milliseconds = int(input())
root = pow(number, 0.5) 
print("Sample Output:")
time.sleep(milliseconds / 1000)
print("Square root of", number, "after", milliseconds, "is", root)

my_tuple = ("Astana", "Almaty", "Mektep", True, False, 0, 4, 7)
print(all(my_tuple))