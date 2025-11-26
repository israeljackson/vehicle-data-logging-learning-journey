import random, csv, time

#introduction
print("-----Temperature logger-----")

#open csv file
with open("temperatures.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Time", "Temperature"])
    for i in range(1,11):
        time.sleep(2)
        temp = round(random.uniform(20,40), 2)
        writer.writerow([i, temp])

#display success message
print("Temperature has been logged into CSV file.")