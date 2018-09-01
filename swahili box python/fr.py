# first_object
class First():
    pass
fr = First()
print(type(fr))
print(type(First))



# second_object
class Cat:
    def __init__(self, name):
        self.name = name
missy = Cat("Missy")
lucky = Cat("Lucky")

print(missy.name)
print(lucky.name)

# third_object
class Work():
    def __init__ (self, name, age, gender):
        self.name = name
        self.name = age
        self.gender = gender
emp_1 = Work("yahya",32,"Male")
emp_2 = Work("jane", 50,"Female")
emp_3 = Work("pi", 40,"Male")
print(emp_2.gender)
