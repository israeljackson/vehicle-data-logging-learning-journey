# Vehicle Telemetry Logger (BUGGY VERSION)
# Your task: Find and fix at least 5 bugs!

import json, random, datetime, time

print("Starting telemetry loggerr...")

def generate_packet():
    speed = random.randint(0, 120)
    fuel = random.uniform(0, 40)
    gps = {"lat": random.uniform(-90, 90), "lon": random.uniform(-180, 180)}
    time_stamp = datetime.datetime.now().isoformat()
    packet = {
        "Speed": speed,
        "Fuel": fuel,
        "GPS": gps,
        "Timestamp": time_stamp
    }
    print(packet)
    return packet


def save_packet(packet):
    with open("telemetry_data.json", "w") as f:
        json.dump(packet, f, indent=4)
        print("Saved packet: ", packet)

for i in range(5):
    data = generate_packet()
    save_packet(data)
    print("Packet", i+1, "logged!")
    time.sleep(1)

print("Telemetry logging completed successfully!")
