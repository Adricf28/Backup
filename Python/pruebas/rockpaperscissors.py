import random

def play():
    user = "r"
    computer = random.choice(["r", "p", "s"])
    # r>s  s>p  p>r
    if user == computer:
        return 'It\'s a  Tie'
    
    if iswin(user, computer):
        return 'You won!'
    
    return 'You lost!'
    
def iswin(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True
    
print(play())