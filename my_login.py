from tkinter import *

import mysql.connector
mydb = mysql.connector.connect(
	host = 'localhost', 
	user = 'root', 
	password ='Mudah222.',
	database = 'mydatabase')   ### CHECK THIS OUT LATER
mycursor = mydb.cursor()    ###CHECK THIS OUT LATER
  
# COLORS
bgclr ='#282828'
fgclr='#cecece'
clr='#004a95'


def login():
	u = user_Entry.get()             #input("Enter user name: ")
	p =password_Entry.get()

	

	check=f"""
				SELECT name,password  FROM users 
				WHERE name='{u}' AND 
				password= '{p}
				"""

	cmd.execute(check)
	result = cmd.fetchall()

	if (u,p) in result :

		warn.config(text=u, fg='yellow')  ## can be removed
		warn.config(text='User Authentication', fg ='green')
	else:
		warn.config(text='User Details Invalid')


def add_user():
	u = user_Entry.get()
	p = password_Entry.get()

	this =f"""
		INSERT INTO users
		VALUES(Null,'{u}','{p}')  """

	cmd.execute(this)
	cmd.commit()
	warn.config(text="User added", fg="green")


w=Tk()
w.title('Login')
w.geometry('500x300')
w.config(bg = '#282828')
w.resizable()



user =Label(w,
	          text= 'User',
	          font = ('blod',15),
	          bg= bgclr,
	          fg= fgclr)

user.place(x=20,y=40)
bgclr ='#282828'
fgclr='#cecece'
clr='#004a95'

user_Entry=Entry(w,bg=bgclr,
					fg='white',
					relief=GROOVE,
					highlightcolor='white',
					highlightthickness=2,
					highlightbackground=clr,
					width=40,
					font=10,
					bd=5)

user_Entry.place(x=20,y=80)
password=Label(w,
	        text='Password',
	        font=('bold',15),
	        bg= bgclr,
	        fg= fgclr
	        )	
password.place(x=20,y=120)


password_Entry=Entry(w,bg=bgclr,
					fg='white',
					relief=GROOVE,
					highlightcolor='white',
					highlightthickness=2,
					highlightbackground=clr,
					width=40,
					font=10,
					show='*',
					bd =5)
password_Entry.place(x=20,y=160)

warn=Label(w,font=('bold',10),bg= bgclr)
warn.place(x=80,y=200)

button=Button(w,
				text='Login',
				bg=clr,
				fg='White',
				relief=GROOVE,
				highlightcolor=clr,
				highlightthickness=2,
				width=40,
				font=10,
				command=login )

button.place(x=20,y=240)

add_btn= Button(w,
				text='Login',
				bg=clr,
				fg='White',
				relief=GROOVE,
				highlightcolor=clr,
				highlightthickness=2,
				width=40,
				font=10,
				command= add_user)



w.mainloop()


				
