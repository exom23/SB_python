employees = dict()             ##local function
slips = dict()                ## Local
basic_salary = 15,000

def file_employeedetails():
    global employees
    name = input("Enter employee's name: ")
    kra_pin = input("Enter employee's KRA pin: ")

    employees[name] = [name, kra_pin]

def employee_sales_record(employee_name):   ## should be removed
    pass


def update_sales_record(employee_name):
    hours = input("Enter Number of Hours: ")     
    quantity = input("Enter Quantity sold: ")
    amount =("Payment : ")

    com = (float(amount) * float(quantity)) * (10/100)   ## try:                                          ##com for commmodities
                                                             ## amount = float(amount)
                                                             ## quantity = float(quantity)
                                                             ##except:
                                                                ##pass
                                                             ## com = (quantity * amount) * (10/100)
    employees[employee_name].append(amount)
    employees[employee_name].append(quantity)
    employees[employee_name].append(com)
    

    
def calculate_tax(employee_name):
    gross = basic_salary + employees[employee_name][4]
    employees[employee_name].append(gross)

    taxs = None

    if gross > 100000:
        tax = 0.25
    elif gross > 50000:    ## start from 50,001
         tax = .2
    elif gross > 30000:     ##starts from 30,001
         tax = .15
    elif gross > 10000:     
         tax = .1
    elif gross > 5000:      
         tax = .05
    else:
        tax = 0

    return tax


    
def net_salary(employee_name):
   net = (employees[employee_name][5] * calculaate_tax(employee_name))
return net



    
def generate_slip(employee_name):
      global slips
      details = employees[employee_name]
      name = details[0]
      pin = details[1]
      tax = calculate_tax(employee_name)
      net = net_salary(employee_name)
      amount = details[2]
      gross = details[5]
      slip = f"""
          ------------------------------------------------
          :		JUMIA ENTERPRISE PAYROLL SLIP	        :
	  ------------------------------------------------
	  Name:  {name}                  KRA Pin: {pin}
	  -------------------------------------------------
	  : Hours 		Quantity sold             Amount :
	  -------------------------------------------------


	  Tax Rate:      {tax*100 }%             Tax Due: Ksh. {amount}      
	  -------------------------------------------------
	  Gross Salary: Ksh {gross}		  Net Sal: Ksh. {net} 
	  -------------------------------------------------

			"""

      slips[employee_name] =slip
	## / extend to the next line   ## """ """ for multie line string


def print_payslip(employee_name):
      slip = slips[employee_name]
      print(slip)
      ## global function ## this is the key{employees[employee_name][0]}    ##{employees[employee_name][1]}

def print_all_slips():
    global slips

    for slip in slips.values():
        print(slip)
        print("\n...........................................................................................\n")


def get_gross_salary(employee_name):
    pass



if __name__ == "__main__":
    running= True
    import sys
    sys.clear

    while running:
        task = input("Enter a command: ")
        if task == "add employee":
            file_employeedetails()
            
        elif task == "update employee":
            name = input("For which employee: ")
            update_sales_records(name)                ##changed
            employee_sales_record(name)
      
        elif task == "print slip":
            name = input("For Whom: ")
            generate_slip(name)
            print_payslip(name)
            
        elif task == "get gross salary":
            name = input("For Whom: ")
            print(f"The gross salary for {name} is {get_gross_salary(name)}")
            ##for the whole finance ##print("{} : {}".format()) anoter way to format this string

        elif task == "quit":
            running = False
            ## f has to be in uppercase so as to define it

        else:
            print("Sorry, I am not programed to perform this task ")
            print(f"I can't {task}")
