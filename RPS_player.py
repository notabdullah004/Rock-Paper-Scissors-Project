# RPS_player.py

history = {'rock':0, 'paper':0, 'scissors':0}

def player():
    # Predict opponent’s next move by frequency
    if sum(history.values()) == 0:
        return 'rock'  # start with rock

    # Find most frequent opponent move
    pred = max(history, key=history.get)

    # Play the move that beats the predicted one
    counter = {'rock':'paper', 'paper':'scissors', 'scissors':'rock'}
    return counter[pred]

def update(opponent_move):
    history[opponent_move] += 1
