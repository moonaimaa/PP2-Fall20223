n,m = [int(s) for s in input().split()]
dw = set([day for day in range(1, n+ 1) if day % 7 not in (6, 0)])
nstr = set(dw)
for party in range(m):
    a, b = [int(s) for s in input().split()]
    mxs = (n - a) // b + 1
    nstr -= {a + b*i for i in range(mxs)}
print(len(dw) - len(nstr))
