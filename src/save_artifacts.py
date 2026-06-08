import joblib
import tensorflow as tf
import pandas as pd

# load dataset again to rebuild scaler consistently
df = pd.read_csv(
    "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna()
df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})
df = df.drop("customerID", axis=1)
df = pd.get_dummies(df)

X = df.drop("Churn", axis=1)

# scaler
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)

joblib.dump(scaler, "models/scaler.pkl")

print("Scaler saved ✔")

# NOTE:
# We assume model was trained in train_tensorflow.py
# and saved manually there or will be saved here