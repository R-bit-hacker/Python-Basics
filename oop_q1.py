class Student:
    def __init__(self, name,sub_marks):
        self.name=name
        self.sub_marks=sub_marks

    def get_avg(self):
        sum=0
        for i in self.sub_marks:
            sum+=i
        print(f"Hi {self.name} your average score is: ", sum/3)

s1=Student("Esha", [99,87,89]) 
s1.get_avg()   
        