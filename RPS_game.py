import random

def play(player, opponent, rounds=100):
    """Plays `rounds` games between your function and an opponent.
       Returns percentage of wins by your player."""
    wins = 0
    for _ in range(rounds):
        move = player()
        opp = opponent()
        if beats(move, opp):
            wins += 1
    return wins / rounds * 100

def beats(move, opp):
    return ((move == 'rock' and opp == 'scissors') or
            (move == 'scissors' and opp == 'paper') or
            (move == 'paper' and opp == 'rock'))

# Sample bot strategies others you must beat (imported in tests)
def quincy():
    return random.choice(['rock', 'paper', 'scissors'])

def abbey():
    return 'rock'

def kris():
    return 'scissors'

def mrugesh():
    return {'r': 'rock', 'p': 'paper', 's': 'scissors'}[random.choice('rps')]
