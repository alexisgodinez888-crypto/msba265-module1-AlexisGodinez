import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual styling
plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams["font.sans-serif"] = "DejaVu Sans"
plt.rcParams["font.size"] = 10
pd.set_option("display.max_columns", 20)

# Load dataset
data_path = os.path.join("..", "data", "raw_business_data.csv")

if not os.path.exists(data_path):
    data_path = os.path.join("data", "raw_business_data.csv")

df = pd.read_csv(data_path)

print(f"[+] Loaded Dataset Shape: {df.shape[0]} rows x {df.shape[1]} columns")

# Show first 10 rows
print(df.head(10))
