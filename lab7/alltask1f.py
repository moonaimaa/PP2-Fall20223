import re
#1
pattern = r'ab*'
# with open('row.txt', 'r') as file:
#      text = file.read()
text=input()
matches = re.findall(pattern, text)
for match in matches:
    print("Match:", match)
# a=re.findall(pattern, text)
# print(a)

#2
#text=intput()
tx = re.findall(r"ab{2,3}", text)
print("task 2",tx)

#3
tx = re.findall(r"[a-z][_][a-z]", text)
print(tx)

#4
with open('row.txt', 'r') as file:
    text = file.read()
#text = input()
tx = re.findall(r"[А-Я][а-я]+", text)
print(tx)

#5
# with open('row.txt', 'r') as file:
#      text = file.read()
text=input()
tx = re.findall(r"a.*b$", text)
print(tx)


#6
#text=input()
with open('row.txt', 'r') as file:
    text = file.read()
tx=re.sub("[ ,.]","|",text)
print(tx)

#7
text = input()
def snake_to_camel(txt):
    tx = re.findall("[a-z]+",text)
    help = ""
    for i in tx:
        help+=i[0].upper()+i[1:len(i)]
    return help
print(snake_to_camel(text))

#8
text = input()
# with open('row.txt', 'r') as file:
#      text = file.read()
tx = re.sub(r"(\w)([A-Z])", r"\1 \2",text)
print(tx)

#9
text = input()
# with open('row.txt', 'r') as file:
#      text = file.read()
tx = re.sub(r"(\w)(\s)+([A-Z])", r"\1 \3",text)
print(tx)

#10
# with open('row.txt', 'r') as file:
#      text = file.read()
text = input()
def camel_to_snake(text):
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
        
print(camel_to_snake(text))