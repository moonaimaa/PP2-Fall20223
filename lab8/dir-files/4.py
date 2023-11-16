a = open(r"/Users/gu.yemail.ru/Desktop/pp2tut/lab8/row.txt").read()
b = open("/Users/gu.yemail.ru/Desktop/pp2tut/lab6/sample-data.json").read()
c = open(r"/Users/gu.yemail.ru/Desktop/pp2tut/lab8/row.txt")
d = open("/Users/gu.yemail.ru/Desktop/pp2tut/lab6/sample-data.json")
e = open("all.txt").read()      

if e:
    print(e.count("\n") + 1)  # if file is not empty 
else:
    print(e.count("\n"))      # if file is empty

print("first way with count() method where we count amount of lines in a file:")
print(a.count("\n") + 1)      # first way where we count amount of lines in a file with count() method
print(b.count("\n") + 1)

print("second way with readlines() which returns list of lines and we take its lenght as number of lines in a file:")
print(len(c.readlines()))     # second way with readlines() which returns list of lines and we take its lenght as number of lines in a file
print(len(d.readlines()))

