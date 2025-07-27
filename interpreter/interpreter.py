expression = input("Expression: ").strip().split(" ")
if expression[1] == "+":
    sum = round(float(expression[0])+float(expression[2]), 1)
    print(sum)
elif expression[1] == "-":
    diff = round(float(expression[0])-float(expression[2]), 1)
    print(diff)
elif expression[1] == "*":
    multiply = round(float(expression[0])*float(expression[2]), 1)
    print(multiply)
elif expression[1] == "/":
    if float(expression[2]) != 0.0:
        divide = round(float(expression[0])/float(expression[2]), 1)
        print(divide)
    else:
        print("Denominator cannot be zero, Try again")
