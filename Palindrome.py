word = input ("Please enter a sentence: ")
wo = word.lower ()
w = wo.replace(' ', '')
if w == w [: :-1]:
    print ('Palindrome')
else:
    print ('Not Palindrome')
