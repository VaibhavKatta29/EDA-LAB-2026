import pandas as pd

# Read the CSV file
df = pd.read_csv("MOSFET_ID_VDS.csv")

print("Columns:")
print(df.columns.tolist())

print("\nShape:")
print(df.shape)

print("\nDescription:")
print(df.describe())