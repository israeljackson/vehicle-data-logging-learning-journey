import csv

#introduction
print("Multi-user Info Logger!")

#collect user info
def info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    location = input("Enter you location: ")
    

    #store each user data as a dictionary
    person = dict( Name = name, Age = age, Adress = location)
    print(person)
    return [name, age, location]

data = []

#open csv file
with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Location"])
    while True:
        
        proceed = input("Do you wish you proceed(y/n): ").lower()
        if proceed == 'y':
            data.append(info())
            continue
        elif proceed == 'n':
            break
        
    writer.writerows(data)

print("Info saved to users.csv successfully.")