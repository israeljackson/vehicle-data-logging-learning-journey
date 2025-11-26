import random
#introduction
print("-----Dice Simulator-----")

#create a list
results = []

#create function
def roll_dice():
    while True:
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        prompt = input("Enter 'y' to roll the dice and enter 'n' to quit ")
        prompt.lower()
        rolls = roll1, roll2
        try:
            if prompt == 'y':
                print(rolls)
                results.append(rolls)
            elif prompt == 'n':
                break
        except ValueError:
            print("Enter an alphabet. Either 'y', or 'n'.")

#declare the function
roll_dice()

#display the results
print("Your results:", results)