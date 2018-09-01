class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
emp_1 = Employee("Moses", 23)
emp_2 = Employee("Peter", 32)
print(emp_1.name + " is " + str(emp_1.age) + " year(s) old.")

print(emp_2.name + " is " + str(emp_2.age) + " year(s) old.")
