import pandas as pd

data = pd.read_csv("holiday_data.csv")

my_filter = data["feedback_score"] == data["feedback_score"].min()
lowest_score = data[my_filter]
print(lowest_score.head())