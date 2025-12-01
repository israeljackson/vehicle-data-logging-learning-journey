import csv

#introduction
print("Multi-user Info Logger!")

#collect user info
def info():
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        location = input("Enter you location: ")

        return{"Name": name, "Age": age,"Location": location}

    except ValueError:
        print("Age must be a number. Try again.")
        return info()
    

data = []

#open csv file
with open("users.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Age", "Location"])
    writer.writeheader()

    while True:
        entry = info()
        data.append(entry)

        writer.writerow(entry)

        proceed = input("Do you wish you proceed(y/n): ").lower()
        if proceed != 'y':
            break
        
print("Info saved to users.csv successfully.")