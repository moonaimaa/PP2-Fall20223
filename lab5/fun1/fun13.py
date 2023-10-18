import random

print('Hello! What is your name?')
name = input()

print(f'Well, {name}, I am thinking of a number between 1 and 20.')
print('Take a guess.')

myNum = random.randint(1, 20)

def low():
    print('Your guess is too low')
    print('Take a guess.')

def up():
    print('Your guess is too high.')
    print('Take a guess.')

cnt = 1
while True:
    num = int(input())
    if num == myNum:
        print(f'Good job,{name}! You guessed my number in {cnt} guesses!')
        break
    if num < myNum:
        low()
    if num > myNum:
        up()
    cnt +=1



