# 🧠 Rock-Paper-Scissors Predictor AI (Advanced Version)

A smarter AI that plays Rock-Paper-Scissors against you — and learns to **beat you** over time! It uses a **Random Forest Classifier** and analyzes your recent move patterns to predict and counter your next move.

---

## 🎯 Project Goal

- Predict user’s next move based on **last 5 moves**.
- Use **machine learning + fallback strategy** to beat random play.
- Keep track of **scores** (wins, losses, draws).

---

## 🛠️ Technologies Used

- **Python**
- **scikit-learn** – `RandomForestClassifier` for smarter prediction
- **NumPy** – data transformation
- **collections** – for history tracking and move frequency analysis

---

## 🚀 Features

✅ Predicts user’s next move using a machine learning model  
✅ Counters with AI’s best move  
✅ Keeps a live scoreboard  
✅ Analyzes your last **5 moves** instead of 3  
✅ Uses **frequency-based fallback strategy** when not enough data  
✅ Trains and improves **as you play**

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/rps-predictor-ai.git
cd rps-predictor-ai
pip install scikit-learn numpy
