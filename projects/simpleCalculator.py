#introduction
print("Simple Calculator 🧮")

#create calculation function
def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op== '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError
        return a / b
    elif op== '**':
        return a ** b
    else:
        raise ValueError("Invalid operator entered.")
        

while True:
    try:
        # prompt user for numbers and an operator
        num1 = float(input("Enter first number: "))
        op = input("Enter operator(+, -, *, /, **): ")
        num2 = float(input("Enter second number: "))

        #call the function and display the result
        print("Your answer is: ", round(calculate(num1, num2, op), 2))

    #handle errors
    except ValueError:
        print("Invalid Input.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")

    #ask user if they would like to continue
    proceed = input(" Do you wish to continue? (y/n) ")
    proceed.lower()
    if proceed == 'y':
        continue
    elif proceed == 'n':
        break
    else:
        print("Enter valid input y/n")
        continue