class Student():
    def __init__(self,name,reg_no,gender):
        self.name  = name
        self.reg_no = reg_no
        self.gender = gender
    def getDetails(self):
        print(self.name)
        print(self.reg_no)
        print(self.gender)
name=input("Enter name: ")
reg_no=input("Enter reg_no: ")
gender=input("Enter your gender: ")
std1 = Student(name,reg_no,gender)
std1.getDetails()
