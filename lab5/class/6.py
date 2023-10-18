def isPrime(x):
    d = 2
    while x % d != 0 and pow(d,2) < x:
        d+=1
    if x % d != 0:
         return True
    else:
        return False

def filt(n):
    list(map(lambda x : isPrime(x), n))
    print(*list(filter(isPrime,n)))
# * -> кортеж емес кылып шыгарып береды, негызы ол сызда шыгаруга болады и там можно готовый листты колдануга тоже можно если лень вводить 
 
n=list(map(int,input().split()))

#[1, 3, 2,5 , 20, 21]
filt(n)