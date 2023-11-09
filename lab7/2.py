import re
with open('row.txt', 'r') as file:
    text = file.read()

#text=intput()
tx = re.findall(r"ab{2,3}", text)
print(tx)

# import re
# with open('row.txt', 'r') as file:
#    my_string = file.read()
# #my_string = input('enter a string ')
# p = re.compile('ab{2,3}?')
# m = p.search(my_string)
# if m:
#     print('it\'s a match')
# else:
#     print('no match found')