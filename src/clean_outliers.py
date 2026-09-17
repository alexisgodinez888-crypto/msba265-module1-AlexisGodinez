import pandas as pd

df = pd.read_csv("data/raw_business_data.csv")

cleaned = df.copy()

for col in ["Density", "DrivAge", "BonusMalus", "VehAge"]:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    cleaned = cleaned[(cleaned[col] >= lower) & (cleaned[col] <= upper)]

cleaned.to_csv("data/cleaned_business_data.csv", index=False)
print("Cleaned:", cleaned.shape)
