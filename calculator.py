def get_number(number = 0):
    while True:
        operand = input("Number " + str(number)+": ")
        try:
            return float(operand)
        except:
            print("Not a valid Number")


operand1 = get_number(1)
operand2 = get_number(2)

sign = input("sign: ")
if sign == "+":
    result = operand1 + operand2
elif sign == "-":
    result = operand1 - operand2
elif sign == "/":
    if operand2 != 0:
        result = operand1 / operand2
    else:
        print("Division by zero.")
elif sign == "*":
    result = operand1 * operand2
else:
    print("Invalid sign.")

print("Result: ", round(result, 2))