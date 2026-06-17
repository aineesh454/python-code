def printFullName(firstName, lastName, greeting):
    print(greeting + " " + firstName + " " + lastName)
while True:
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    greeting = input("Enter your greeting: ")

    if greeting == "":
        printFullName(firstName, lastName)
    else:
        printFullName(firstName, lastName, greeting)

        
    answer = input("Do you want to continue? (yes/no): ")
    if answer not in ["yes", "y"]:
        exit()    