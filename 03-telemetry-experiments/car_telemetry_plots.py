import pandas as pd
import matplotlib.pyplot as plt

#load csv
df = pd.read_csv("projects/car_telemetry2.csv")

#first plot
plt.figure(figsize=(10, 6))
plt.plot(df["Time"], df["Speed"])
plt.title("Speed vs Time")
plt.xlabel("Time(s)")
plt.ylabel("Speed(km/h)")
plt.grid(True)
plt.savefig("speed_time_plot.png")
plt.show()

#second plot
plt.figure(figsize=(10, 6))
plt.scatter(df["Fuel"], df["Speed"])
plt.title("Fuel vs Speed")
plt.xlabel("Fuel(L)")
plt.ylabel("Speed(km/h)")
plt.grid(True)
plt.savefig("fuel_speed_scatter.png")
plt.show()

#third plot
plt.figure(figsize=(10, 6))
plt.plot(df["Time"], df["RPM"], label="RPM")
plt.plot(df["Time"], df["Temperature"], label="Temperature")
plt.title("RPM and Temperature vs Time")
plt.xlabel("Time(s)")
plt.ylabel("values")
plt.legend()
plt.grid(True)
plt.savefig("rpm_temp_plot.png")
plt.show()

print("All plots saved as PNG files:")
print("1. speed_time_plot.png")
print("2. rpm_temp_plot.png")
print("3. fuel_speed_scatter.png")