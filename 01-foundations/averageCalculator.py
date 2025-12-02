from turtle import speed
from numpy import mean
import pandas as pd

df = pd.read_csv("data.csv")
print(df.head(5))
print(df.tail(5))

print(df.mean())
print(df.min())
print(df.shape())

