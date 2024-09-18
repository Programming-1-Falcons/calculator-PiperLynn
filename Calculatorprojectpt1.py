while True:
    one = float(input("Enter First Number: "))

    operation = input("Enter Operation: ")

    two = float(input("Enter Second Number: "))

    if operation == "+":
        answer = one + two

    if operation == "-":
        answer = one - two

    if operation == "/":
        answer = one / two

    if operation == "*":
        answer = one * two

    if operation == "^":
        answer = one ** two

    print("Answer: " + str(answer))