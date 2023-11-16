import os
path = "/Users/gu.yemail.ru/Desktop/pp2tut/lab8/row.txt"
if os.path.exists(path):
    fileName = os.path.basename(path)
    path_to_file = os.path.dirname(path)
    print(fileName)
    print(path_to_file)
else:
    print("The path does not exist")