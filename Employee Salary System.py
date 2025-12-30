class Employe:
    def __init__(self,name,emp_id,salary):
        self.name = name
        self.empl_id = emp_id
        self.__salary = salary

    def get_salary (self):
        return self.__salary

    def increment_salary(self, amount):
        if amount >0:
            self.__salary += amount
            print("salary incremented")

        else:
            print("invalid amount")

    def display_emp(self):
        print("-----Employe Details----")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.empl_id}")


name = input("Enter employe name: ")
emp_id = input("Enter employe Id: ")
salary = float(input("Enter initial salary: "))


emp = Employe(name,emp_id,salary)

while True:
    print("\n-----Employee salary system-----")
    print("1. View employe info")
    print("2. View salary")
    print("3. Increment salary ")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice =="1":
        emp.display_emp()

    elif choice == "2":
        print("Salary", emp.get_salary())

    elif choice =="3":
        amount =float(input("Enter increment amount: "))
        emp.increment_salary(amount)

    elif choice == "4":
        print("By! Exited Program.")
        break

    else:
        print("invalid choice,Try Again.")
        
















    






            
        
    
