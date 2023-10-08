a=input().split()
b= set()
for i in range(len(a)) :
    if a[i] in a[:i] :
        print("yes")
    else:
        print("no")
        b.add(i)