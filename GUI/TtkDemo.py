import tkinter.ttk
from tkinter.ttk import *

mainWindow = tkinter.Tk(screenName="mainWindow")
mainWindow.title("home screen")
mainWindow.geometry("500x600")

style = tkinter.ttk.Style()
style.configure("Main.Heading",font=("arial",20,"bold"),foreground="black")

demolabel = tkinter.ttk.Label(master=mainWindow,name="demo1",text="welcome to tkinter")
demolabel.configure(font=("Arial",20,"bold"),foreground="#088a3e")
demolabel.pack()
labelGroup = tkinter.ttk.Frame(master=mainWindow,width=500,height=600,borderwidth=10,relief="solid")

firstLabel = tkinter.ttk.Label(master=labelGroup,text="first label",style="Main.Heading")
firstLabel.pack(ipadx=20,pady=20)
secondLabel = tkinter.ttk.Label(master=labelGroup,text="second label")
secondLabel.pack()


labelGroup.pack(side="top",padx=10,pady=10)
labelGroup.pack_propagate(0)
mainWindow.mainloop()