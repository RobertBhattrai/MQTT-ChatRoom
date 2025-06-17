import numpy as np
from collections import deque, Counter
from sklearn.ensemble import RandomForestClassifier

# Moves
moves = ['rock', 'paper', 'scissors']
move_to_int = {'rock': 0, 'paper': 1, 'scissors': 2}
int_to_move = {0: 'rock', 1: 'paper', 2: 'scissors'}

# ML data
X, y = [], []

# Use longer history
HISTORY_LENGTH = 5
history = deque(maxlen=HISTORY_LENGTH)

# Stronger model
model = RandomForestClassifier(n_estimators=100)

# Scores
score = {'user': 0, 'ai': 0, 'draw': 0}

def predict_next_move():
    if len(history) < HISTORY_LENGTH:
        return fallback_prediction()

    input_seq = [move_to_int[m] for m in history]
    
    if len(X) >= 20:
        model.fit(X, y)
        prediction = model.predict([input_seq])[0]
        return int_to_move[prediction]
    
    return fallback_prediction()

def fallback_prediction():
    if len(history) == 0:
        return np.random.choice(moves)
    # Frequency-based guess
    freq = Counter(history)
    most_common_move = freq.most_common(1)[0][0]
    return most_common_move

def get_counter_move(predicted):
    # Best move to beat the predicted move
    return {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock'
    }[predicted]

def get_result(user, ai):
    if user == ai:
        score['draw'] += 1
        return "Draw"
    elif (user == 'rock' and ai == 'scissors') or \
         (user == 'paper' and ai == 'rock') or \
         (user == 'scissors' and ai == 'paper'):
        score['user'] += 1
        return "You Win!"
    else:
        score['ai'] += 1
        return "AI Wins!"

def display_score():
    print(f"\n📊 Scoreboard:")
    print(f"   You     : {score['user']}")
    print(f"   AI      : {score['ai']}")
    print(f"   Draws   : {score['draw']}")
    print("---\n")

def play_game():
    print("🎮 Let's play Rock-Paper-Scissors! Type 'exit' to quit.\n")

    while True:
        user_move = input("Your move (rock/paper/scissors): ").lower()

        if user_move == 'exit':
            break
        if user_move not in moves:
            print("Invalid input. Try again.\n")
            continue

        predicted = predict_next_move()
        ai_move = get_counter_move(predicted)

        print(f"\n🤖 AI predicted: {predicted}")
        print(f"🤖 AI plays   : {ai_move}")
        print(f"🧑 You played : {user_move}")

        result = get_result(user_move, ai_move)
        print(f"🏁 Result     : {result}")

        display_score()

        # Update training data
        if len(history) == HISTORY_LENGTH:
            X.append([move_to_int[m] for m in history])
            y.append(move_to_int[user_move])

        history.append(user_move)

    print("👋 Thanks for playing!")

if __name__ == "__main__":
    play_game()
