import random as rand
while True:
    num = rand.randint(1,100)
    print(num)
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
                    print("\n\tCongratulation, you guessed  the number in first attempt")
                else:
                    print(f'\nit took you {attempts} attempts to guess the right number\n')
                break 
        except Exception as e:
            print('\n\t\ttry again\n')
    



