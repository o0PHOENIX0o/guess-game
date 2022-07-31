import random as rand

def game():
    guess=None
    attempts = 0
    while(guess!=num):
        try:
            guess=int(input("\nguess the number: "))
            if guess>num:
                attempts=attempts+1
                print("\n\t\twrong guess!\n\t try smaller number\n")
            elif guess<num:
                attempts=attempts+1
                print("\n\t\t**wrong guess!**\n\t try greater number\n")
            elif guess==num:
                print("\n\t\tyour guess is right")
                if attempts==0:
                    print('_'*100,end=' ')
                    print("\n\t\tCongratulation, you guessed  the number in first attempt")
                    print('-'*100,end='')
                else:
                    print('_'*100,end='')
                    print(f'\n\tit took you {attempts} attempts to guess the right number')
                    print('_'*100,end='')
                break 
        except Exception as e:
            print('\n\t\ttry again\n')

while True:
    print('\n\nlevles: 1.Easy\n\t2.Medium\n\t3.Hard\n\t4.Impossible')
    lvl = input('\nenter the level: ')
    if lvl.lower() in ['exit','done','quit']:
        print('\t\t\tgame ended')
        break
    elif lvl.lower() in ['1','easy']:
        num = rand.randint(1,50)
        game()
    elif lvl.lower() in ['2','medium']:
        num = rand.randint(1,150)
        game()
    elif lvl.lower() in ['3','hard']:
        num = rand.randint(1,350)
        game()
    elif lvl.lower() in ['4','impossible']:
        num = rand.randint(200,600)
        game()
    else:
        print('\t\tthere is no such level\n\t\tplease enter a valid level')

        

    



