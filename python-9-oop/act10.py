class employee:
    def __init__(self, name, age, salary):
        self.name = name


        self.__age = age
        self.__salary = salary

    def getAge(self):
        return self.__age

    def getSalary(self):
        return self.__salary
    
    def setAge(self, age):
        self.__age = age

    def setSalary(self, salary):
        self.__salary = salary

e1 = employee("John", 25, 50000)
def display_employee():
    emp_name = e1.name
    emp_age = e1.getAge()
    emp_salary = e1.getSalary()
    print(f"{emp_name} is {emp_age} years old and earns ${emp_salary} per year.")

while True:
    print("\nEmployee Management System")
    print("*"*30)
    choice1 = input("DO you want to display employee details? (yes/no): ")
    if choice1 not in ["yes ","y"]:
        print("Exiting the program.")
        break
    else:
       display_employee()
       choice2 = input("Do you want to update employee details? (yes/no): ")
       if choice2 not in ["yes", "y"]:
        break
       else:
        new_age = int(input("Enter new age: "))
        new_salary = float(input("Enter new salary: "))
        e1.setAge(new_age)
        e1.setSalary(new_salary)
        display_employee()

        choice = input("Do you want to update employee details? (yes/no): ")
        if choice in ["yes", "y"]:
            continue
        else:
            print("Exiting the program.")
            break