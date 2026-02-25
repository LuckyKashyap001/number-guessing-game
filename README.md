# 🎯 Number Guessing Game (Python)

A simple command-line number guessing game built using Python.

The program randomly selects a number between **1 and 100**, and the player must guess it. After each guess, feedback is provided until the correct number is guessed.

---

## 🚀 Features

- Random number generation using Python's `random` module  
- Feedback system:
  - "Too High" if the guess is greater than the target  
  - "Too Low" if the guess is smaller than the target  
  - "Correct!" when the guess matches  
- Counts and displays number of attempts  
- Option to play multiple rounds  

---

## 🧠 How the Game Works

1. The program generates a random number between 1 and 100.
2. The player enters a guess.
3. The program checks:
   - If guess > secret number → "Too High"
   - If guess < secret number → "Too Low"
   - If guess == secret number → "Correct!"
4. The total number of attempts is displayed.
5. Player can choose to play again.

---

## ▶️ How to Run

### 1️⃣ Make sure Python is installed
Check using:
```
python --version
```

### 2️⃣ Run the script
```
python your_file_name.py
```

---

## 📸 Sample Output

```
Guess the number between 1 and 100
Enter your guess: 50
Too Low
Enter your guess: 75
Too High
Enter your guess: 63
Correct!
You guessed the number in 3 attempts.

Do you want to play again? (yes/no):
```

---

## 📂 Project Structure

```
number-guessing-game/
│── game.py
│── README.md
```

---

## 🧩 Requirements

- Python 3.x  
(No external libraries required)

---

## 🎓 Concepts Used

- Functions
- Loops (while loop)
- Conditional statements
- Random number generation
- User input handling
- String formatting (f-strings)

---

## ⭐ Future Improvements (Optional Ideas)

- Add difficulty levels (Easy/Medium/Hard)
- Add score system
- Limit number of attempts
- Add graphical interface (Tkinter / Pygame)

---

## 📜 License

This project is open-source and free to use.

---

Happy Coding! 🚀
