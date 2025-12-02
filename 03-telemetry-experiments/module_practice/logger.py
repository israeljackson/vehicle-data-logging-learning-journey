import csv
from generator import generate_data

def log_data():
    with open("data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Speed", "Fuel", "RPM"])
        for i in range(20):
            data = generate_data()
            writer.writerow([data["speed"], data["fuel"], data["rpm"]])

if __name__ == "__main__":
    print("loggging data to csv...")
    log_data()