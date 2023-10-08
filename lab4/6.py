n=int(input())
word = set()

for i in range(n):
    line =input().split() #строку разбиваем  на слова
    word.update(line) 
print(len(word))