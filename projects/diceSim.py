import random

#create a list
results = []

#create the function
def roll_dice(n):
    for i in range(n):
        roll = random.randint(1, 6)
        print(roll)
        results.append(roll)

#call function
roll_dice(8)

#display results
print(results)
