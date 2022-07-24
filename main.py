import random


def play():
    user = input("'r' rock, 'p' for paper or 's' scissors \n")
    computer = random.choice(['r', 'p', 's'])
    print(computer)

    if user == computer:
        return 'tie'

    if is_win(user, computer):
        return 'you won'

    return 'You lost'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 'r'):
        return True


print(play())
