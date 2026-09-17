import openml
import pandas as pd

dataset = openml.datasets.get_dataset(41214)  # freMTPL2freq
X, y, _, _ = dataset.get_data()

df = pd.concat([X, y], axis=1)
df.to_csv("data/raw_business_data.csv", index=False)

print("Downloaded:", df.shape)
