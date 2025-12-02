import pandas as pd

#read car telemetry
df = pd.read_csv("projects/car_telemetry.csv")

#add acceleration, efficiency and status columns
df["Acceleration"] = df["Speed"].diff()
df["Efficiency"] = df["Speed"] / df["Fuel"]
df["Status"] = df["Fuel"].apply(lambda x: "Normal" if x >= 30 else "LowFuel")

average_speed =  round(df["Speed"].mean(), 2)
max_acceleration =  df["Acceleration"].max()
Min_fuel =  df["Fuel"].min()

#display average speed, max acceleration and minimum fuel
print("Average Speed = ", average_speed)
print("\nMaximum Acceleration = ", max_acceleration)
print("\nMinimum Fuel Level = ", Min_fuel)

#filter top speeds
top_speed_df = df[df["Speed"] > average_speed]

#save top speed
top_speed_df.to_csv("high_performance.csv", index=False)