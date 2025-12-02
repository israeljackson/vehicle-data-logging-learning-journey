import random

def generate_data():
    return {
        "speed" : random.randint(20,120),
        "fuel":  round(random.uniform(5,70), 2),
        "rpm": random.randint(1000, 5000)
    }

if __name__ == "__main__":
    print("Generating data..")