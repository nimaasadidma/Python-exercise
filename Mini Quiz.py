
print ("Welcome to animal quiz. Let's play.")
n = input ('Please enter your name: ')
name = n.capitalize()

animals = ('lion' , 'elephant', 'swan', 'parrot', 'horse', 'cheetah', 'eagle', 'leopard', 'duck', 'tiger', 'fox', 'falcon', 'giraffe', 'bear', 'hyena', 'shark', 'whale', 'scorpian', 'rhino')
print(f'Welcome {name}. Please select your answers based on below animals. ')
print(animals)
print('\n')
def level () :
    print (f'NICE JOB {name}! Level passed !')
def gameover():
    print (f'{name}, your answer was wrong! Game Over!')

ans1 = input ('which animal is a farm animal? ')

if ans1 == 'horse' or ans1 == 'duck' :
    level()
    print('\n')
    ans2 = input ('which animal is a flesh-eating bird? ')
    if ans2 == 'eagle' or ans2 == 'falcon':
        level()
        print('\n')
        ans3 = input ('which animal is has horns? ')
        if ans3 == 'rhino':
            level()
            print('\n')
            ans4 = input ('which animal is the largest one? ')
            if ans4 == 'whale':
                level()
                print('\n')
                ans5 = input ('which animal is the fastest animal? ')
                if ans5 == 'cheetah':
                    print (f'Congrats! You got the gold medal {name}.')
                else:
                    print(f'Oops! Your answer was not correct but you got the silver medal {name}')
            else :
                gameover()
                
        else :
            gameover()      
    else :
        gameover()
else :
    gameover()
