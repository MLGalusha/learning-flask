# rock_paper_scissors.py
import random

def play_rps(user_choice):
    options = ["r", "p", "s"]

    computer_choice = random.choice(options)
    mapping = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

    def convert_choice(choice):
        return mapping.get(choice)

    if user_choice == computer_choice:
        return f"It's a tie!"

    results = {
        'r': {'p': "You lost!", 's': "You win!"},
        'p': {'s': "You lost!", 'r': "You win!"},
        's': {'r': "You lost!", 'p': "You win!"}
    }

    result = results[user_choice][computer_choice]
    ratio = {
        "win": 0,
        "loss": 0
    }
    if result == "You win!":
        ratio["win"] += 1
    elif result == "You lost!":
        ratio["loss"] += 1

    return f"{result}  Win:{ratio["win"]}   Loss:{ratio["loss"]}"
