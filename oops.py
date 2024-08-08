class Student:
    college_name="CUI"
    name= "anonymous"

    def __init__(self,name, marks):
        self.name= name
        self.marks= marks
        print("...Adding new student to database...")

    def hello(self):
        print("hello",self.name)

s1= Student("usman", 99)
#print(s1.name)
#print(s1.marks)
s1.hello()

s2=Student("ahmad", 88)
print(s2.name)
print(s2.marks)

print(Student.college_name)