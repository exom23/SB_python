name = "John"

age = "20"
 
print("Is name a digit ", name.isdigit())
print("Is age a digit ", age.isdigit())

#----------------------{ Lists}------------------#


my_list = ["Tom","cat",100]

for num in range(5):
	my_list.append(num)

for item in my_list:
	print("List item: ", item)


#----------------------{ Dictionaries}------------------#

print("#----------------------{ Dictionaries}------------------#")
my_dict = dict()


my_dict["ball"] = "A sphere"
my_dict["Tom"] = "My friend"
my_dict["Fish"] = "food "


for key, value in my_dict.items():
	print(f"Key: {key}       Value: {value}")

