import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

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

# Target encoding
df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})

# -----------------------
# 3. FEATURE ENGINEERING
# -----------------------
# Drop ID column
df = df.drop("customerID", axis=1)

# Convert categorical variables using one-hot encoding
df = pd.get_dummies(df)

X = df.drop("Churn", axis=1)
y = df["Churn"]

# -----------------------
# 4. TRAIN / TEST SPLIT
# -----------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------
# 5. SCALING
# -----------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -----------------------
# 6. TENSORFLOW MODEL
# -----------------------
model = keras.Sequential([
    keras.layers.Dense(64, activation="relu", input_shape=(X_train.shape[1],)),
    keras.layers.Dense(32, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# -----------------------
# 7. TRAINING
# -----------------------
history = model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# -----------------------
# 8. EVALUATION
# -----------------------
loss, acc = model.evaluate(X_test, y_test)

print("\n=== TEST RESULTS ===")
print("Accuracy:", acc)

model.save("models/churn_model.keras")
print("Model saved ✔")