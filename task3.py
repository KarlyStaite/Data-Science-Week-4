import pandas as pd

data = pd.read_csv("holiday_data.csv")

print(data["all_inclusive_count"].mean())