def get_operation():
    while True:
        operation = input("Choose an operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Invalid operation")
            continue


def get_number(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Please enter a valid number.")


def calculator():
    while True:
        num1 = get_number("Enter the first number: ")
        operation = get_operation()
        num2 = get_number("Enter the second number: ")

        try:
            if operation == '+':
                result = num1 + num2

            elif operation == '-':
                result = num1 - num2

            elif operation == '*':
                result = num1 * num2

            elif operation == '/':
                result = num1 / num2

            print("The result is:", result)
            break

        except ZeroDivisionError:
            print("Error: cannot divide by 0.")
            continue


calculator()


        
    
           
    

    
        


        
    
           
    

    
        
