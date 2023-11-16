import os
if os.path.exists(r"/Users/gu.yemail.ru/Desktop/pp2tut/lab8/A.txt"):
    os.remove(r"/Users/gu.yemail.ru/Desktop/pp2tut/lab8/A.txt")
else:
    print("The file does not exist")