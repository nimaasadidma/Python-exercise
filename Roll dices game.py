from random import random, randint
player1 = input ('Player1, please enter your name: ')
player2 = input ('Player2, please enter your name: ')
p1 = player1.capitalize()
p2 = player2.capitalize()
L1 = list()
L2 = list()
i = 0
while i <= 3 :
     start1 = input (f'{p1}, please press Enter to roll dices. ')
     d1 = randint (1, 6)
     d2 = randint (1, 6)
     print (d1, d2)
     L1.append (max(d1, d2))

     start2 = input (f'{p2}, please press Enter to roll dices. ')
     d1 = randint (1, 6)
     d2 = randint (1, 6)
     print (d1, d2)
     L2.append (max(d1, d2))

     i += 1

avr1 = sum (L1) / len (L1)
avr2 = sum (L2) / len (L2)
print (f"{p1}'s score is {avr1: .2f} and {p2}'s score is {avr2: .2f}")
if avr1 == avr2 :
    print ('Tie')
elif avr1 > avr2 :
    print (f'{p1} won.')
else:
    print (f'{p2} won.')
