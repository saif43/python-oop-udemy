class Employee:
    company_name = "Some Company"

    def __init__(self, name):
        self.name = name

    def displayEmployeeDetails(self):
        print(self.name)


a = Employee("a_name")
b = Employee("b_name")


a.displayEmployeeDetails()
b.displayEmployeeDetails()
