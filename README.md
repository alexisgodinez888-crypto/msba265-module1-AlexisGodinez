MSBA‑265‑01‑80805 — Special Analytics Topics (Fall 2026)

📌 1. Project Structure

This repository contains all required components for Module 1:
msba265-module1-AlexisGodinez/
│
├── notebooks/                     # Jupyter notebooks for EDA
│   └── module1_eda.ipynb
│
├── data/
│   ├── raw_business_data.csv      # Original dataset
│   └── cleaned_business_data.csv  # Output from cleaning pipeline
│
├── src/
│   └── clean_outliers.py          # Outlier cleaning script
│
├── reports/
│   ├── correlation_heatmap.png
│   ├── feature_distributions.png
│   ├── data_dictionary.csv
│   └── MSBA 265 module 1 .pdf     # Final homework report
│
└── README.md

📌 2. How to Replicate This Project (Step-by-Step)

Step 1 — Clone the Repository

git clone https://github.com/alexisgodinez888-crypto/msba265-module1-AlexisGodinez.git
cd msba265-module1-AlexisGodinez


Step 2 — Create and Activate a Virtual Environment
python -m venv venv

Activate it:

Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate


Step 3 — Install Required Python Packages
pip install pandas seaborn matplotlib
(If a requirements.txt is added later, use pip install -r requirements.txt.)

📌 3. Running the EDA Notebook
Launch Jupyter:

Then 
Open:
notebooks/module1_eda.ipynb

Run all cells top-to-bottom.

This notebook will automatically generate:
reports/correlation_heatmap.png
reports/feature_distributions.png
reports/data_dictionary.csv


📌 4. Running the Outlier Cleaning Pipeline
From the repo root:
python src/clean_outliers.py

This script:
Loads data/raw_business_data.csv
Removes invalid exposures
Removes impossible driver ages
Enforces BonusMalus regulatory caps (50–350)
Removes Density outliers using Tukey fences


Saves cleaned dataset to:
data/cleaned_business_data.csv

📌 5. Generated Artifacts
After running the notebook + script, you will have:
| File | Description |
| ``reports/correlation_heatmap.png`` | Pearson correlation heatmap |
| ``reports/feature_distributions.png`` | Density, DrivAge, BonusMalus, VehAge distributions |
| ``reports/data_dictionary.csv`` | Full data dictionary |
| ``data/cleaned_business_data.csv`` | Cleaned dataset ready for modeling |
| ``reports/MSBA ``265 ``module ``1 ``.pdf`` | Final homework report |
