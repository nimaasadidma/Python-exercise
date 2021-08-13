number = input ('Please enter a number: ')
numlist = list()
try :
    num = int (number)
    for i in range (1, num+1):
        if num % i == 0 :
            numlist.append (i)
    print (numlist)
    if len (numlist) == 2 :
        print ('This number is a prime number.')
except :
    print ('Please enter an integer number.')
