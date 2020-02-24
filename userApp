import os
from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
from tkinter import filedialog
import os.path

app = Tk()
app.title("User: Create and save file in folder")
label1 = Label(app, text='Enter text:')
label1.grid(column=0,row=0,sticky='W')
label2 = Label(app,text='Save text as file by name:')
label2.grid(column=1,row=0,sticky='E')

#Ham de save file as name duoc nguoi dung dinh nghia
var = StringVar()
editName = Entry(app,textvariable=var)
editName.grid(column=1,row=1,ipady=5,ipadx=5,sticky='NE')
def saveFileAsName():
    user_input=var.get()
    saveFileAsName = open((a + '.txt'),'w')
    saveFileAsName.write(a)
    saveFileAsName.close()
    return

#Phim chuc nang Browse cho phep duyet directory
def browse_button():
    global folder_path
    fileName = filedialog.askdirectory()
    folder_path.set(fileName)
    os.chdir(fileName)
folder_path = StringVar()
lbl = Label(app, textvariable=folder_path)
lbl.grid(row=5, column=0,sticky='W')
butBrs = Button(app, text='Choose directory to save',command=browse_button)
butBrs.grid(row=4, column=0,sticky='W')

#In va Save text vao file trong thu muc da chi dinh/ mac dinh la folder cua project
def wrFile():
    file = open(var.get()+'.txt','w+')
    file.write(textIn.get('1.0',END) + '\n')
    file.close()
textIn = Text(app,height=5, width=30)
textIn.grid(column=0, row=1)
#buttonWr = Button(app)
#buttonWr.config(text="Save",command = wrFile)
#buttonWr.grid(row=5, column=1,sticky='W')

def onClick():
    messagebox.showinfo("Message Box","Successfully save file to folder!")
buttonWr = Button(app)
buttonWr.config(text="Save",command = wrFile)
buttonWr.grid(row=5, column=1,sticky='W')

'''
class Test():
    def __init__(self):
        self.app = Tk()
        self.svButton = Button(self.app,text="Save",command=self.combineFunc(self.funcA,self.funcB))
        self.svButton.grid(column=1,row=5)
        self.app.mainloop()
    def combineFunc(self, *funcs):
       def combinedFunc(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
       return combinedFunc
    def funcA(self):
        self.buttonWr = Button(app)
        buttonWr.config(self.app,command=wrFile)
        buttonWr.grid(column=1,row=5)
    def funcB(self):
        messagebox.showinfo("Message box","Successfully save file to folder!")
app = Test()
'''
app.mainloop()
