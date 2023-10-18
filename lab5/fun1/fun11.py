def pal(s):
    return s==s[::-1]

s=str(input())
st=pal(s)
if st:
    print("TRUE")
else:
    print("False")