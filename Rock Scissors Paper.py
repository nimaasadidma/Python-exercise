
from random import random, randint

ch = ('r', 's', 'p')

score = 0
mark = 0
while True:
    
    if score == 3 or mark == 3:
        break
    ran = randint(0,2)
    com = ch[ran]
    user = input ('Enter your choice: ')
    if user not in ch:
        print ('Select a valid tool!')
        continue
    print (com)

    if com == user:
        print('tie!')
    elif com == 'r' and user == 's':
        print ('You lost!')
        mark = mark + 1
        print (f'Your score is {score} and your opponent score is {mark}.')
    elif com == 'r' and user == 'p':
        print ('You win!')
        score = score + 1
        print (f'Your score is {score} and your opponent score is {mark}.')
    elif com == 's' and user == 'p':
        print ('You lost!')
        mark = mark +1
        print (f'Your score is {score} and your opponent score is {mark}.')
    elif com == 's' and user == 'r':
        print ('You win!')
        score = score + 1
        print (f'Your score is {score} and your opponent score is {mark}.')
    elif com == 'p' and user == 'r':
        print ('You lost!')
        mark = mark +1
        print (f'Your score is {score} and your opponent score is {mark}.')
    elif com == 'p' and user == 's':
        print ('You win!')
        score = score + 1
        print (f'Your score is {score} and your opponent score is {mark}.')

