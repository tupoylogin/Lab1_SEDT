import numpy.random as rand

number = rand.randint(0,100)

not_guessed = True

lower=0
upper=100

while not_guessed:
    print ("Guess a number from 0 to 100")
    not_inputed = True
    while not_inputed:
        try:
            guess = int(input())
        except: 
            ValueError 
            print("It is not an int")
        else: 
            if (guess<0) or (guess>100) or (guess==-0):
                print("It is not in range [0;100]")
            else: not_inputed=False
    if (guess > number):
        upper=guess-1
        print("Too high!\nTry in range [{0};{1}]".format(lower,upper))
    elif (guess < number):
        lower = guess+1
        print("Too low!\nTry in range [{0};{1}]".format(lower,upper))
    else:
        print("Congrats!")
        not_guessed=False