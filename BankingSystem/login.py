import tkinter
import tkinter.ttk


root = tkinter.Tk(screenName="root")
root.title("Banking Management System")
root.geometry("900x700")
root.resizable(False,False)

loginFrame = tkinter.ttk.Frame(master=root,borderwidth=10,relief="solid",width=500,height=500)
usernameLabel = tkinter.ttk.Label(master=loginFrame,text="Username :")
passwordLabel = tkinter.ttk.Label(master=loginFrame,text="Password :")
usernameEntry = tkinter.ttk.Entry(master=loginFrame)
passwordEntry = tkinter.ttk.Entry(master=loginFrame)
loginButton = tkinter.ttk.Button(master=loginFrame,text="Login")


usernameLabel.grid(row=0,column=0)
usernameEntry.grid(row=0,column=1)
passwordLabel.grid(row=1,column=0)
passwordEntry.grid(row=1,column=1)
loginButton.grid(row=2,column=0)



loginFrame.grid_propagate(0)
loginFrame.pack(pady=300)
root.mainloop()