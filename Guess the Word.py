
from random import random, randint

planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus')
print (planets)
s = 0

while True:

    ran = randint(0, len(planets)-1)
    com = planets[ran]
    user = input ('Enter your choice: ')
    guess = user.capitalize()
    print(com)
    if s == -2:
        print ('GAME OVER')
        break
    if com == guess :
        s = s + 2
        print (f'TRUE. You have {3+s} more chances.', '\n')
    else :
        s = s - 1
        print (f'Wrong. You have {3+s} more chance(s).', '\n')
