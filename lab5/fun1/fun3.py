def solve(numheads, numlegs):
    rab = (numlegs - numheads*2 )/2
    kur = numheads - rab
    return rab , kur

print(solve(35,94))
'''heads= int(input())
legs=int(input())
print(solve(heads,legs))'''