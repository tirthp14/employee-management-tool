#Tirth Tusharkumar Patel, Noel, Joel
#This program helps a company manage their employee details

print("Welcome to TeamTracker")

Emp_Data = {}

def INPUTDETAILS():
    N = int(input("\nEnter the number of employee's: "))
    for i in range(N):
        print("\n---------------------------------------- \n")
        print("Enter employee details here", "\n")
        while True:
            Empid = int(input("Enter employee's ID: "))
            if Empid <= 0:
                print("Invalid input. Enter a positive number!")
                print("---------------------------------------- \n")
            else:
                break
        Empname = input("Enter employee's Full Name: ")
        Emp_Designation = input("Enter employee's designated position: ")
        Emp_Department = input("Enter employee's Department: ")
        while True:
            Emp_Salary = float(input("Enter employees's Salary: "))
            if Emp_Salary < 0:
                print("Invalid input. Enter a positive number!")
            else:
                break
        Emp_Data[i] = {"Employee ID" : Empid, "Employee Name" : Empname, "Employee Designation" : Emp_Designation, "Employee Department" : Emp_Department, "Employee Salary" : Emp_Salary}

def EMPDETAILS():
    size = len(Emp_Data)
    print("\n----------------------------------------\n")
    print("List of all employees:")
    for i in range(size):
        print("\nEmployee", (i + 1),": \n")
        for key, value in Emp_Data[i].items():
            print(f"{key} : {value}")

def EMPDETAILS_DEP():
    size = len(Emp_Data)
    print("\n----------------------------------------")
    Given_Dep = input("\nEnter specific department that you want to look up: ")
    found = False
    print("\nList of Employees in", Given_Dep, "department are:")
    for i in range(size):
        if Given_Dep == Emp_Data[i]["Employee Department"]:
            found = True
            print("\nEmployee", (i + 1), ": \n")
            for key, value in Emp_Data[i].items():
                print(f"{key} : {value}")
    if not found:
        print("\nOpps..there are no Employee's in this department")

def EMPID_SORT():
    while True:
        print("\n----------------------------------------")
        order = input("\nType A to sort in Ascending Order \nOR \nType D to sort in Descending Order\n \nWhat do you choose?: ")
        if order == "A":
            size = len(Emp_Data)
            for a in range(0, (size - 1)):
                min_value = a
                for b in range((a + 1), size):
                    if Emp_Data[b]["Employee ID"] < Emp_Data[min_value]["Employee ID"]:
                        min_value = b
                Emp_Data[a], Emp_Data[min_value] = Emp_Data[min_value], Emp_Data[a]
            print("\n----------------------------------------")
            print("\nEmployee Data in Ascending Order of Employee ID:")
            sorted_data = Emp_Data
            for i in range(len(sorted_data)):
                print("\nEmployee", (i + 1), ": \n")
                for key, value in sorted_data[i].items():
                    print(f"{key} : {value}")
            break
        elif order == "D":
            size = len(Emp_Data)
            for a in range(0, (size - 1)):
                min_value = a
                for b in range((a + 1), size):
                    if Emp_Data[b]["Employee ID"] > Emp_Data[min_value]["Employee ID"]:
                        min_value = b
                Emp_Data[a], Emp_Data[min_value] = Emp_Data[min_value], Emp_Data[a]
            print("\n----------------------------------------")
            print("Employee Data in Descending Order of Employee ID:")
            sorted_data = Emp_Data
            for i in range(len(sorted_data)):
                print("\nEmployee", (i + 1), ": \n")
                for key, value in sorted_data[i].items():
                    print(f"{key} : {value}")
            break
        else:
            print("\nInvalid sorting choice! Please try again..")

def EMP_EDIT():
    while True:
        print("\n----------------------------------------\n")
        add = input("Type Add to Insert new Employee details \nOR\nType Delete to Remove an Employee's Details\n \nWhat do you chose to do: ")
        if add == "Add":
            New_Data = {}
            print("\n----------------------------------------\n")
            print("Enter employee details here", "\n")
            Empid = int(input("Enter employee's ID: "))
            if Empid <= 0:
                print("Invalid input. Enter a positive number! Try Again")
            else:
                if Empid in [emp["Employee ID"] for emp in Emp_Data.values()]:
                    print("\nEmployee ID already exists!")
                else:
                    Empname = input("Enter employee's Full Name: ")
                    Emp_Designation = input("Enter employee's designated position: ")
                    Emp_Department = input("Enter employee's Department: ")
                    Emp_Salary = eval(input("Enter employees's Salary: "))

                    New_Data["Employee ID"] = Empid
                    New_Data["Employee Name"] = Empname
                    New_Data["Employee Designation"] = Emp_Designation
                    New_Data["Employee Department"] = Emp_Department
                    New_Data["Employee Salary"] = Emp_Salary
                    print("\n----------------------------------------")

                    Emp_Data[len(Emp_Data)] = New_Data
                    print("\nEmployee details added successfully!\n")
                    print("Updated employee details:")
                    Emp_Details(Emp_Data)
                    break
        elif add == "Delete":
            empid = int(input("\nEnter ID of employee to be deleted: "))
            found = False
            for key, value in Emp_Data.copy().items():
                if value["Employee ID"] == empid:
                    found = True
                    del Emp_Data[key]
                    print("\nEmployee details deleted successfully!")
                    Emp_Details(Emp_Data)
            break
            if not found:
                print("\nEmployee not found in records. Please try again!")
        else:
            print("\nInvalid input. Please try again!")
            
def Emp_Details(Data):
    for key in Data:
        print("\nEmployee", (key + 1), ": \n")
        for sub_key, value in Data[key].items():
            print(f"{sub_key} : {value}")

def EMP_MENU():
    while True:
        print("\n----------------------------------------")
        print("\nMenu Options:\n")
        print("1. Accept Employee Details")
        print("2. Display Employee Details")
        print("3. Department of Employee")
        print("4. Sort Employee Details by Employee ID")
        print("5. Add/Delete Employee Details")
        print("6. Quit")

        menu = int(input("\nEnter your choice: "))
        if menu == 1:
            INPUTDETAILS()
        elif menu == 2:
            EMPDETAILS()
        elif menu == 3:
            EMPDETAILS_DEP()
        elif menu == 4:
            EMPID_SORT()
        elif menu == 5:
            EMP_EDIT()
        elif menu == 6:
            print("Exciting program...")
            print("Thank You for using TeamTracker")
            break
        else:
            print("Invalid choice entered!")

EMP_MENU()
