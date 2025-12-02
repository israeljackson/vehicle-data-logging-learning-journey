import pandas as pd
df = pd.read_csv("projects/car_telemetry.csv")

# Show first and last 5 rows
print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

average_speed = df['Speed'].mean()
min_fuel = df['Fuel'].min()
total_readings = len(df)

print("Average Speed:", round(average_speed,2))
print("Lowest Fuel Level:", min_fuel)
print("Total Number of Readings:", total_readings)

#filter only speeds above 60
high_speed_df = df[df['Speed'] > 60]

#save the unfiltered data
high_speed_df.to_csv('high_speed_readings.csv', index=False)

#print success message
print("\nHigh speed readings saved successfully!👍")