# Class definition
class Animal:
  """Makes cute animals."""
  # For initializing our instance objects
def __init__(self, name, age, is_hungry):
 self.name = name
 self.age = age
 self.is_hungry = is_hungry
# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print(zebra.name, zebra.age, zebra.is_hungry)
print(giraffe.name, giraffe.age, giraffe.is_hungry)
print(panda.name, panda.age, panda.is_hungry)
