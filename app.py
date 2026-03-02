from flask import Flask, render_template, request
import joblib
import numpy as np
import sqlite3

app = Flask(__name__)

model = joblib.load("model/fatigue_model.pkl")

def get_level(score):
    if score <= 30:
        return "Low"
    elif score <= 60:
        return "Moderate"
    elif score <= 80:
        return "High"
    else:
        return "Critical"

# Create database table
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            score REAL,
            level TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/analyze")
def analyze():
    return render_template("analyze.html")

@app.route("/predict", methods=["POST"])
def predict():
    values = [
        float(request.form["sleep"]),
        float(request.form["sleep_quality"]),
        float(request.form["screen_time"]),
        float(request.form["stress"]),
        float(request.form["activity"]),
        float(request.form["water"]),
        float(request.form["work"]),
        float(request.form["caffeine"]),
        float(request.form["mood"]),
    ]

    input_data = np.array([values])
    score = model.predict(input_data)[0]
    level = get_level(score)

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO records (score, level) VALUES (?, ?)", (score, level))
    conn.commit()
    conn.close()

    return render_template("result.html", score=round(score, 2), level=level)

@app.route("/dashboard")
def dashboard():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT score FROM records")
    data = c.fetchall()
    conn.close()

    scores = [row[0] for row in data]

    return render_template("dashboard.html", scores=scores)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)