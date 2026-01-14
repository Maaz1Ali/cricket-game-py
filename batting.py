import random

SHOT_NAMES = {
    1: "Straight Drive",
    2: "Cover Drive",
    3: "Lofted Drive",
    4: "Pull Shot"
}

def user_bat():
    try:
        try:
            print(SHOT_NAMES)
            shot = int(input("Select shot (1-4): "))
            if shot not in SHOT_NAMES:
                raise ValueError
            else:
                print(f"You played {SHOT_NAMES[shot]}")
                return shot
        except (ValueError, NameError):
            print("❌ Invalid shot. Try again.")
            return user_bat()
    except (EOFError , KeyboardInterrupt):
        print("\nBye Bye !!")
        print("Computer wins the game")
        return exit()

def computer_bat():
    return random.choice([1, 1, 2, 3, 3, 4, 4])
