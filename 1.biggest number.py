while True:
    num1 = int(input("Enter the first number (enter 0 to exit): "))
    
    if num1 == 0:
        print("Exiting the program.")
        break
    
    num2 = int(input("Enter the second number: "))
    
    print(f"The higher value is: {max(num1, num2)}" if num1 != num2 else "The numbers are equal.")
