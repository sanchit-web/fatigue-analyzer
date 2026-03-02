# 🧠 Smart Fatigue Intelligence System

A full-stack Machine Learning web application that analyzes daily lifestyle factors and predicts a fatigue score (0–100) with intelligent risk classification and interactive dashboard analytics.

This project combines Backend Engineering + Machine Learning + Database Integration in a production-style Flask application.

---

## 🚀 Features

- 🔍 Lifestyle-based fatigue prediction
- 📊 Fatigue score generation (0–100 scale)
- 🚦 Risk classification (Low / Moderate / High / Critical)
- 📈 Dashboard with historical trend visualization (Chart.js)
- 💾 SQLite database integration
- 🧠 Machine Learning model using Random Forest Regressor
- 🌐 Multi-page Flask web application
- 🎨 Clean dark-themed modern UI

---

## 🏗️ Tech Stack

### Backend
- Python
- Flask
- SQLite
- Scikit-learn
- NumPy
- Pandas

### Frontend
- HTML
- CSS
- Chart.js (CDN-based visualization)

---

## 🧠 How It Works

The system collects user lifestyle inputs including:

- Sleep hours
- Sleep quality
- Screen time
- Stress level
- Physical activity
- Water intake
- Work hours
- Caffeine consumption
- Mood score

These features are processed through a trained **Random Forest Regression model** to generate a fatigue score between 0 and 100.

The fatigue score is then classified into levels:

| Score Range | Fatigue Level |
|-------------|--------------|
| 0–30        | Low          |
| 31–60       | Moderate     |
| 61–80       | High         |
| 81–100      | Critical     |

Each prediction is stored in a SQLite database and visualized in the dashboard for historical tracking.

---

## 📁 Project Structure
fatigue-analyzer/
│
├── app.py
├── model/
│ ├── train_model.py
│ └── fatigue_model.pkl
│
├── templates/
│ ├── base.html
│ ├── home.html
│ ├── analyze.html
│ ├── result.html
│ ├── dashboard.html
│ └── about.html
│
├── static/
│ └── css/
│ └── style.css
│
├── database.db
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/YOUR-USERNAME/fatigue-analyzer.git
cd fatigue-analyzer
2️⃣ Create Virtual Environment
Windows (PowerShell)
python -m venv venv
venv\Scripts\activate
Mac / Linux
python3 -m venv venv
source venv/bin/activate
3️⃣ Upgrade pip (Recommended)
python -m pip install --upgrade pip
4️⃣ Install Dependencies

If you have requirements.txt:

pip install -r requirements.txt

If not, install manually:

pip install flask pandas scikit-learn joblib numpy
5️⃣ Train the Machine Learning Model (First-Time Setup Only)
cd model
python train_model.py
cd ..

This will generate:

model/fatigue_model.pkl
6️⃣ Run the Application
python app.py
7️⃣ Open in Browser
http://127.0.0.1:5000


