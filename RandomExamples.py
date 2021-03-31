import random 

#https://docs.python.org/3/library/index.html


def guess(x):
    newNumber = random.randint(1, x)

    print (newNumber)

    guess = 0

    while guess != newNumber:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        if guess < newNumber :
                print ("Sorry guess again - too low")
        if guess > newNumber :  
                print ("Sorry guess again - too high")
        
        
def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c': 
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} too high (h), too low(l) or correct (c)").lower()

        if feedback =='h':
            high = guess - 1
        elif feedback =='l':
            low = guess + 1

    print(f"Good job!")




computer_guess(10)
#guess(10)
#print ("well done- good bye")


