def recursivefn(n):
    if n == 0 or n == 1: 
        return 1
    return n * recursivefn(n - 1)
while True:
    try:
        user_input = input("Enter a number to calculate its factorial: ")
        if user_input.lower() in ["no", "n", "exit"]:
            print("Exiting the program.")
            break
        number = int(user_input)
        if number < 0:
            print("Factorial is not defined for negative numbers. Please enter a non-negative integer.")
            continue
        print(recursivefn(number))
    except ValueError:
        print("Invalid input. Please enter a non-negative integer or 'exit' to quit.")
        continue
    answer = input("Do you want to continue? (yes/no): ")
    if answer not in ["yes", "y"]:
        print("Exiting the program.")
        break
    print("program has ended")