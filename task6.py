import pandas as pd

data = pd.read_csv("holiday_data.csv")

my_filter = data["all_inclusive_count"] > 300
high_all_inc = data[my_filter]
print(high_all_inc)