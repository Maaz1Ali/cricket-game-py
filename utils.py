import time

def show_rules():
    print("=" * 45)
    print("🏏 MINI CRICKET — 1 OVER MATCH")
    print("=" * 45)
    print("""
RULES:
• 2 innings, 6 balls each
• Toss decides who bats first

SHOT TYPES:
1 → Straight Drive
2 → Cover Drive
3 → Lofted Drive
4 → Pull Shot

SCORING:
• (1,2) vs (1,2) → FOUR
• (3,4) vs (3,4) → SIX
• Yorker vs wrong shot → OUT
• Else → DOT BALL
""")
    print("=" * 45)


def commentary(result):
    time.sleep(0.5)
    if result == 6:
        print("💥 HUGE SIX!")
    elif result == 4:
        print("✨ CLASSY FOUR!")
    elif result == "out":
        time.sleep(0.5)
        print("🔥 CLEAN BOWLED! OUT!")
    else:
        print("• Dot ball")
    time.sleep(0.6)


def scoreboard(ball_no, runs, balls_left, target=None):
    balls_bowled = 6 - balls_left

    if balls_bowled == 0:
        run_rate = 0.0
    else:
        run_rate = (runs / balls_bowled) * 6

    line = (
        f"Ball {ball_no} | "
        f"Score: {runs} | "
        f"Balls left: {balls_left} | "
        f"RR: {run_rate:.2f}"
    )

    if target:
        line += f" | Target: {target}"

    print(line)
    print("-" * 45)
