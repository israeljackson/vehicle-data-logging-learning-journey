#introduction
print("✏️ Grade calculator 🧮")

#establish result list
results = []

 #prompt user for name
name = input(f"Enter your name: ")

#prompt user for grade
for i in range(1, 4):
    score = int(input(f"Enter your score {i}: "))
    results.append(score)

#create function to calculate average score
def avg_score(scores):
    return round((sum (scores) / len(scores)),2)

#create function to assign grade
def assign_grade():
    if avg_score(results) >= 70 :
        print("Grade = A")
    elif avg_score(results) >= 60:
        print("Grade = B")
    elif avg_score(results) >= 50:
        print("Grade = C")
    else:
        print("Grade = F")

#display information
print("Name:", name)
print("Scores: ", results)
print("Average Score: ", avg_score(results))
assign_grade()