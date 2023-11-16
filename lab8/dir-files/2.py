import os
path = r"/Users/gu.yemail.ru/Desktop/pp2tut/lab8/row.txt"
f = open(path)
if os.path.exists(path):
    print("YES, the path is exist!")
else:
    print("does not exist :(")
print(f.readable())
print(f.writable()) # доступен просмотр
if os.access(path, os.X_OK):
    print("YES, it's executable!")
else:
    print("NO")