l = [int(i) for i in input().split()]
cnt = 0
for i in range(1, len(l) - 1):
    if l[i - 1] < l[i] > l[i + 1]:
        cnt += 1
print(cnt)