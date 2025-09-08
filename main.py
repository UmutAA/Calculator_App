import calc

def main():
    print("-------Simple Calculator-------")
    print("Available operations: +, -, *, /")
    temp = ""
    while True:
        temp = input("Type 'exit' to quit or press Enter to continue: ")
        if temp.lower() == "exit":
            break
        elif temp == "":
            num1 = float(input("Enter first number: "))
            op = input("Enter operator: ")
            num2 = float(input("Enter second number: "))

            match op:
                case "+":
                    result = calc.add(num1, num2)

                case "-":
                    result = calc.subtract(num1, num2)

                case "*":
                    result = calc.multiply(num1, num2)

                case "/":
                    try:
                        result = calc.divide(num1, num2)

                    except ValueError:
                        result = None
                        print("Error: Cannot divide by zero.")
                case _:
                    print("Error: Invalid operator.")
                    result = None

            if result is not None:
                print(f"Result: {result}")

        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()