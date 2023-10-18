def rev(word):
    st = word.split()
    str_rev = ' '.join(reversed(st))
    
    return str_rev

st = input()

result = rev(st)
print( result)
