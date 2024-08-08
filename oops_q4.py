class Employee:
    def __init__(self, role, department,salary):
        self.role=role
        self.dep=department
        self.sal=salary

    #@staticmethod
    def showDetails(self):
        print("Role: ", self.role)
        print("Department: ", self.dep)
        print("Salary: ", self.sal)

class Engineer(Employee):
    def __init__(self, name, age):
         self.name=name
         self.age=age
         super().__init__("Engineer","IT",1500000)
         
    def showDetails2(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

eng1=Engineer("Manahil",21)
eng1.showDetails2()
eng1.showDetails()