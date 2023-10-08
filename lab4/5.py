n, m = [int(i) for i in input().split()]
an_color = set()
bor_color = set()
for i in range(n):
    a = int(input())
    an_color.add(a)
for j in range(m):
    b = int(input())
    bor_color.add(b)
mnab = sorted(an_color & bor_color)
mna = sorted(an_color - bor_color)
mnb = sorted(bor_color - an_color)
print(len(mnab))
for num in mnab:
    print(num, end = ' ')
print()    
print(len(mna))
for num in mna:
    print(num, end = ' ')
print()    
print(len(mnb))
for num in mnb:
    print(num, end = ' ')
