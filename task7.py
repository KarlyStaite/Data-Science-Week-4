import pandas as pd

data = pd.read_csv("holiday_data.csv")

my_filter = data["feedback_score"] > 8
high_score = data[my_filter]
print(high_score)