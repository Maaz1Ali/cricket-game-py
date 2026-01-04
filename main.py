from toss import get_user_toss, toss, user_decision, computer_decision
from game_engine import play_innings
from utils import show_rules

def main():
    show_rules()

    user_toss = get_user_toss()
    if not user_toss:
        return

    user_won = toss(user_toss)

    if user_won:
        print("🎉 You won the toss!")
        decision = user_decision()
        if decision is None:
            return
    else:
        print("Computer won the toss.")
        decision = computer_decision()

    if decision == 1:
        print("You bat first.")
        user_score = play_innings(1)
        print(f"Your Score: {user_score}")
        comp_score = play_innings(0, user_score + 1)
    else:
        print("Computer bats first.")
        comp_score = play_innings(0)
        print(f"Computer Score: {comp_score}")
        user_score = play_innings(1, comp_score + 1)

    print("=" * 40)
    if user_score > comp_score:
        print("🏆 YOU WIN!")
    elif user_score < comp_score:
        print("😞 COMPUTER WINS")
    else:
        print("🤝 MATCH DRAW")

if __name__ == "__main__":
    main()