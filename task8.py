import pandas as pd

data = pd.read_csv("holiday_data.csv")

my_filter = data["feedback_score"] < 2
low_score = data[my_filter]
print(low_score)