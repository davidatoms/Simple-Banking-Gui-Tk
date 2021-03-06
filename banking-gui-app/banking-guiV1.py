# imports
from tkinter import *
import os
from PIL import ImageTk, Image

# main screen
master = Tk()
master.title('Banking App')

# functions
def finish_reg():
	name = temp_name.get()
	password = temp_password.get()
	all_accounts = os.listdir()

	if name == "" or password == "":
		notif.config(fg="red",text="All fields are required *")
		return

	for name_check in all_accounts:
		if name == name_check:
			notif.config(fg="red",text="Account already exists")
			return
		else:
			new_file = open(name, "w")
			new_file.write(name+'\n')
			new_file.write(password+'\n')
			new_file.close()
			notif.config(fg="green",text="Account has been created")

def register():
	# register screen
	register_screen = Toplevel(master)
	register_screen.title('Register')

	# vars
	global temp_name
	global temp_password
	global notif
	temp_name = StringVar()
	temp_password = StringVar()


	# labels
	Label(register_screen, text="Please enter your details below to register", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
	Label(register_screen, text="Name", font=('Calibri',12)).grid(row=2,sticky=W)
	Label(register_screen, text="Password", font=('Calibri',12)).grid(row=4,sticky=W)
	notif = Label(register_screen, font=("Calibri",12))
	notif.grid(row=6,sticky=N,pady=10)


	# entries
	Entry(register_screen,textvariable=temp_name).grid(row=2,column=0)
	Entry(register_screen,textvariable=temp_password,show="*").grid(row=4,column=0)


	# buttons
	Button(register_screen,text="Register",command = finish_reg, font=('Calibri',12)).grid(row=5,sticky=N,pady=10)

def login():
	print('This is a login page.')



# image import
img = Image.open('asset_1.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

# labels for screen
Label(master, text = "House of David Banking Beta", font=('Calibri', 14)).grid(row=0,sticky=N,pady=10)
Label(master, text = "The newest bank on the market", font=('Calibri', 12)).grid(row=1,sticky=N)
Label(master, image=img).grid(row=2, sticky=N,pady=15)

# buttons
Button(master, text="Register", font=('Calibri',12),width=20,command=register).grid(row=3,sticky=N)
Button(master, text="Login", font=('Calibri',12),width=20,command=login).grid(row=4,sticky=N,pady=10)

master.mainloop()

