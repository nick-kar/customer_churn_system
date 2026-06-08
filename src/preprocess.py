import pandas as pd

df = pd.read_csv(
    "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

print("Initial shape:", df.shape)

# TotalCharges should be numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Remove rows with missing TotalCharges
df = df.dropna()

print("\nFinal shape:", df.shape)

# Target encoding
df["Churn"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

print("\nTarget distribution:")
print(df["Churn"].value_counts())