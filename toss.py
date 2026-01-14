import random

def get_user_toss():
    import time
    try:
            choice = input("Choose Heads or Tails: ").lower().strip()
            if choice not in ("heads", "tails"):
                time.sleep(0.5)
                print("❌ Invalid toss choice.")
                return None
            return choice
    except (EOFError, KeyboardInterrupt):
        print("\nBye Bye !!")


def toss(user_choice):
    result = random.choice(("heads", "tails"))
    print(f"Toss landed on: {result}")
    return user_choice == result


def user_decision():
    try:
        choice = input("Bat or Bowl first? ").lower().strip()
        if choice == "bat":
            return 1
        elif choice == "bowl":
            return 0
        else:
            print("❌ Invalid choice.")
            return None
    except (EOFError, KeyboardInterrupt):
        print("\nBye Bye !!")


def computer_decision():
    return random.choice((0, 1))
