---

📌 Features

🎲 Toss system (Heads / Tails)

🏏 User vs Computer gameplay

⏱️ Realistic delays for computer actions

📊 Ball-by-ball scoreboard

📈 Live run rate calculation

🎙️ Commentary for 4s, 6s, outs, and dot balls

🧠 Probability-based bowling & batting

🧩 Clean modular code structure



---

🧠 Game Rules (Quick Overview)

Match consists of 2 innings

Each innings has 6 balls

Toss decides who bats first

If scores are equal → Match Draw


Batting Shots

Input	Shot Type

1	Straight Drive
2	Cover Drive
3	Lofted Drive
4	Pull Shot


Scoring Logic

Proper timing → 4 runs

Power shots → 6 runs

Yorker + wrong shot → OUT

Otherwise → Dot Ball



---

📁 Project Structure

cricket_game/
│
├── main.py        # Game entry point
├── engine.py      # Core innings & ball logic
├── utils.py       # Rules, commentary, scoreboard
├── batting.py     # User & computer batting logic
├── toss.py        # Toss & decision logic
└── README.md


---

▶️ How to Run

Requirements

Python 3.8+


Run the Game

python main.py


---

🛠️ Technologies Used

Python (Standard Library)

random module (probability)

time module (delays & realism)



---

🚀 Future Improvements (Planned)

Difficulty modes (Easy / Normal / Hard)

Advanced commentary system

Required run rate display

Match statistics (4s, 6s, strike rate)

Powerplay rules

Persistent match history



---

🧑‍💻 Author

Maaz Ali
B.E. Computer Engineering
Osmania University

> Built as a learning project with structured guidance and iterative improvement.




---

📜 License

This project is open for learning and personal use.
