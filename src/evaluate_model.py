import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    f1_score,
    roc_auc_score,
    precision_score,
    recall_score
)

import tensorflow as tf
from tensorflow import keras

# -----------------------
# 1. LOAD DATA
# -----------------------
df = pd.read_csv(
    "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

# -----------------------
# 2. CLEAN DATA
# -----------------------
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna()

df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})

df = df.drop("customerID", axis=1)

df = pd.get_dummies(df)

X = df.drop("Churn", axis=1)
y = df["Churn"]

# -----------------------
# 3. SPLIT
# -----------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------
# 4. SCALE
# -----------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -----------------------
# 5. MODEL (same as training)
# -----------------------
model = keras.Sequential([
    keras.layers.Dense(64, activation="relu", input_shape=(X_train.shape[1],)),
    keras.layers.Dense(32, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy"
)

# Train briefly (for evaluation demo)
model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0)

# -----------------------
# 6. PREDICTIONS
# -----------------------
probs = model.predict(X_test).flatten()
preds = (probs > 0.5).astype(int)

# -----------------------
# 7. METRICS
# -----------------------
print("\n=== CONFUSION MATRIX ===")
print(confusion_matrix(y_test, preds))

print("\n=== CLASSIFICATION REPORT ===")
print(classification_report(y_test, preds))

print("\n=== CUSTOM METRICS ===")
print("F1-score:", f1_score(y_test, preds))
print("Precision:", precision_score(y_test, preds))
print("Recall:", recall_score(y_test, preds))
print("ROC-AUC:", roc_auc_score(y_test, probs))