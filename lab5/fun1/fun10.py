def uniq(li):
    li1 = []
    for i in li:
        if i not in li1:
            li1.append(i)
    return li1
l=list(map(int, input().split()))

print(uniq(l))
