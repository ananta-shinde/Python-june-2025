from tkinter import *

def saveBtnHnandler():
    print(inputText.get())

mainWindow = Tk(screenName="CreateBank")
mainWindow.title("Create New Bank")
mainWindow.geometry("500x500")

inputLabel = Label(master=mainWindow,text="Enter bank name here :").pack()
inputText = Entry(master=mainWindow)
inputText.pack()

saveBtn = Button(master=mainWindow,text="Save",command=saveBtnHnandler).pack()
mainWindow.mainloop()