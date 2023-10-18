def histogram(li):
    for i in li:
        for k in range(i):
            print('*',end='')
        print()

myl= list(map(int, input().split()))
histogram(myl)
