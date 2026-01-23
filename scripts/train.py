import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import json
import os

os.makedirs("outputs/results", exist_ok=True)

df = pd.read_csv("winequality-red.csv")

X = df.drop("quality", axis=1)
y = df["quality"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

preds = model.predict(X_test)
mse = mean_squared_error(y_test, preds)

joblib.dump(model, "outputs/results/model.pkl")

with open("outputs/results/metrics.json", "w") as f:
    json.dump({"mse": mse}, f)

print("Training complete | MSE:", mse)
