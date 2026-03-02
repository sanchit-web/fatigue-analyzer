import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

np.random.seed(42)

data_size = 1000

data = pd.DataFrame({
    "sleep": np.random.uniform(3, 9, data_size),
    "sleep_quality": np.random.uniform(1, 10, data_size),
    "screen_time": np.random.uniform(2, 12, data_size),
    "stress": np.random.uniform(1, 10, data_size),
    "activity": np.random.uniform(0, 2, data_size),
    "water": np.random.uniform(1, 4, data_size),
    "work": np.random.uniform(4, 12, data_size),
    "caffeine": np.random.uniform(0, 5, data_size),
    "mood": np.random.uniform(1, 10, data_size)
})

data["fatigue_score"] = (
    (10 - data["sleep"]) * 5 +
    (10 - data["sleep_quality"]) * 3 +
    data["screen_time"] * 2 +
    data["stress"] * 4 +
    data["work"] * 2 +
    data["caffeine"] * 1.5 -
    data["activity"] * 5 -
    data["water"] * 2 -
    data["mood"] * 3
)

data["fatigue_score"] = data["fatigue_score"].clip(0, 100)

X = data.drop("fatigue_score", axis=1)
y = data["fatigue_score"]

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "fatigue_model.pkl")

print("Model Saved Successfully")