import pandas as pd

data = pd.read_csv("/Users/karlystaite/Desktop/Data Science/Week 4/holiday_data.csv")

data.plot.scatter(x='feedback_score',y='all_inclusive_count')