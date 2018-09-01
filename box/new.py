employees = dict()
slips  = dict()

def file_employeedetails():
	global employees
	name = input("Enter employee name: ")
	kra_pin = input("Enter employee's KRA pin: ")

	employees[name] = [name, kra_pin]

def employee_sales_record(employee_name):
	pass

def calculate_tax(employee_name):
	pass

def net_salary(employee_name):
	pass
def generate_slip(employee_name):
	global slips 
	slip = f"""
			 ------------------------------------------------
			 :		JUMIA ENTERPRISE PAYROLL SLIP	        :
			 ------------------------------------------------
			 Name:   {employees[employee_name][0] }                   KRA Pin: {employees[employee_name][1]}
			 -------------------------------------------------
			 : Hours 		Quantity sold             Amount :
			 -------------------------------------------------


			 Tax Rate:      14%             Tax Due: Ksh. 0
			 -------------------------------------------------
			 Gross Salary: Ksh 0			Net Sal: Ksh. 0 
			 -------------------------------------------------

			"""
	slips[employee_name] =slip

	
def print_payslip(employee_name):
	slip =  slips[employee_name]
	print(slip)

def get_gross_salary(employee_name):
	pass

if __name__ == "__main__":
	running = True

	while running:
		task = input("Enter a command: ")

		if task == "add employee":
			file_employeedetails()
		elif task == "update records":
			name = input("For which employee: ")
			employee_sales_record(name)
		elif task == "get gross salary":
			name = input("For whom: ")
			print(f"The gross salary for {name} is {get_gross_salary(name)}")
			#print("{}  : {}".format())
		elif task == "print slip":
			name = input("For whom: ")
			generate_slip(name)
			print_payslip(name)
		elif task == "quit":
			running = False
		else:
			print("Sorry, I am not programed to perfom this task ")
			print(f"I literaly cant {task}")

		