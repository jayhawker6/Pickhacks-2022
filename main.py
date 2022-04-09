import pandas as pd

df = pd.read_csv("file.csv", header=0)

print(df.to_string())
