def calculator(): 
    while True:
        try:
            num1 = float(input("Enter number 1: "))
            num2 = float(input("Enter number 2: "))
            operator = input("Enter a operator (+, -, *, /): ")

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2
            else:
                raise ValueError("Invalid Operaotr..!")
            
            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError as z:
            print(f"Error: {z}. Cannot divide by zero!")

calculator()
