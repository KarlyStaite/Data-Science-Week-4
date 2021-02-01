import pandas as pd

data = pd.read_csv("holiday_data.csv")

print(data.iloc[2:8,0:5])