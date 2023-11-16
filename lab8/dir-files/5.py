a = open(r"/Users/gu.yemail.ru/Desktop/pp2tut/lab8/row.txt").readlines()
f = open("files.txt", "a")
for i in a:
    f.write(i)
f.write("\n")
f.close()
f = open("files.txt").read()
print(f)