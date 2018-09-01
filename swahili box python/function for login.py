
##calling the function with sir patrick
##def greeting(name):
  ##  print("Hello",name )

##greeting("moses")

##function for login
def login(username, password):
    user = "moses"
    pin = "abcd"

    if username == user:
        if password == pin:
            print("logged in")
        else:
            print("Wrong pin")
   
name = input("Enter username: ")
code = input("Enter password: ")
login(name,code)


