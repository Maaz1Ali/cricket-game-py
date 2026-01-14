import random
import time
from batting import user_bat, computer_bat
from utils import commentary, scoreboard

def bowl():
    balls = [1, 2, 3, 4, 2, 3, 4]  # bias
    return random.choice(balls)


def ball_engine(bowl_type , shot):
    if bowl_type in (1, 2) and shot in (1, 2):
        return 4
    elif bowl_type in (3, 4) and shot in (3, 4):
        return 6
    elif bowl_type == 1 and shot in (2, 3, 4):
        return "out"
    else:
        return 0


def play_innings(batting_side, target=None):
    runs = 0
    balls_left = 6
    ball_no = 1

    while balls_left > 0:
        current_bowl = bowl()

        if batting_side == 1:
            shot = user_bat()
        else:
            print("Computer is batting...")
            time.sleep(1)
            shot = computer_bat()

        result = ball_engine(current_bowl, shot)
        commentary(result)

        balls_left -= 1

        if result == "out":
            scoreboard(ball_no, runs, balls_left, target)
            break

        runs += result
        scoreboard(ball_no, runs, balls_left, target)
        ball_no += 1

        if target and runs >= target:
            break

    return runs
