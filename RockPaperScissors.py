#Rock paper scissors

import random

def play():
    user = input("What syour choice 'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r','p','s'])
    if user == computer:
        return "tie"

    if is_win(user,computer):
        return "You Won"

    return "You lost"


def is_win(player, opponent):
    #return true if plaer wins
    if  (player == 'r' and opponent == 's') or \
        (player == 's' and opponent == 'p') or \
        (player == 'p' and opponent == 'r'):
        return True   
    else:
        return False


print (f"{play()}")

if __name__