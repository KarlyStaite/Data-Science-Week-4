import pandas as pd

data = pd.read_csv("/Users/karlystaite/Desktop/Data Science/Week 4/holiday_data.csv")

data.plot.bar(x='destination',y='feedback_score')