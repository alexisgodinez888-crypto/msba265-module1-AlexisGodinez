import pandas as pd

def clean_outliers(df):
    # 1. Remove negative exposures
    df = df[df["Exposure"] > 0]

    # 2. Remove impossible driver ages
    df = df[(df["DrivAge"] >= 18) & (df["DrivAge"] <= 100)]

    # 3. Cap BonusMalus at regulatory limits
    df = df[(df["BonusMalus"] >= 50) & (df["BonusMalus"] <= 350)]

    # 4. Remove Density outliers beyond Tukey fence
    q1 = df["Density"].quantile(0.25)
    q3 = df["Density"].quantile(0.75)
    iqr = q3 - q1
    upper_fence = q3 + 1.5 * iqr
    df = df[df["Density"] <= upper_fence]

    return df

if __name__ == "__main__":
    df = pd.read_csv("data/raw_business_data.csv")
    cleaned = clean_outliers(df)
    cleaned.to_csv("data/cleaned_business_data.csv", index=False)
    print("Cleaned dataset saved:", cleaned.shape)
