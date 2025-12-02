import random, time, json

#introduction
print("🏎️ Telemetry Logger 📖")

#establish list
car = {}

#open JSON format
with open ("Car_telemetry.json", "w") as f:
    #generate random values
    for i in range(1, 11):
        print(i)
        speed = random.randint(20,120)
        fuel = round(random.uniform(1, 60), 1)
        rpm = random.randint(1000, 5000)
        temperature = round(random.uniform(30, 150), 2)

        #append them to the dictionary
        car["Speed"] = speed
        car["Fuel"] = fuel
        car["RPM"] = rpm
        car["Temperature"] = temperature

        #format car dictionary to json list evry 2 seconds
        time.sleep(0.5)
        json_car = json.dump(car, f, indent=4)

#print end message
print(json_car)
print("File saved")