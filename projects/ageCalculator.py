import datetime

#ask user for name
name = input("Enter your name: ")

#create a function to ask user for age
while True:
    try:   
        age = int(input("Enter your age: "))
        if age < 0:
            print("Enter a valid age.")
            continue
        break
    except ValueError:
        print("Enter an Integer.")    

#establish present year
current_year = datetime.datetime.now().year

#calculate year of birth
birth_year = current_year - age

#display info
print(f"Your name is {name} and you are {age} years old. You were born in the year {birth_year}.")

#check if age is even or odd
if age % 2 == 0:
    print("Age is even.")
else:
    print("Age is odd.")