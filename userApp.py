import os,shutil,os.path, sys
from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox,filedialog

app = Tk()
app.title("User: Create and Copy file to folder")
#=======Layout window====================
label1 = Label(app, text='Enter text:')
label1.grid(column=0, row=0, sticky='W')
label2 = Label(app, text='Save text as name:')
label2.grid(column=1, row=0,sticky='E')
save_path = StringVar()
copy_path = StringVar()
label3 = Label(app, textvariable=save_path) #Label to show save directory
label4 = Label(app, textvariable=copy_path) #Label to show copy directory


#=======Browse to Save function========================
def browseBtnSave():
    global save_path
    user_input = var.get()
    askDirectorySave = filedialog.askdirectory()
    save_path.set(askDirectorySave) #
    os.chdir(askDirectorySave) #change current directory to that directory
butBrsSv = Button(app, text='Choose directory to save',command=browseBtnSave) #Button_browse directory to SAVE file

#=======Save file as name that user typed==============
var = StringVar()
editName = Entry(app,textvariable=var) #Entry to type name of file 
editName.grid(column=1,row=1,ipady=5,ipadx=5,sticky='NE')
def saveFileAsName():
    saveFileAsName = open((a),'w')
    saveFileAsName.write(a)
    saveFileAsName.close()
    return

#=======Write to file and save to that directory=====
textIn = Text(app,height=5, width=30) #Enter user's text here
textIn.grid(column=0,row=1)
def wrFile():
    file = open(var.get()+'.txt','w+')
    file.write(textIn.get('1.0',END) + '\n')
    file.close()
    if os.path.isfile(var.get()+'.txt'):
        messagebox.showinfo("User Application","Successfully save file to folder!") #check if file exists or not, show messagebox!
    else:
        print("File not exist! Try again!")
buttonWr = Button(app)
buttonWr.config(text="Save",command = wrFile)
buttonWr.grid(row=5, column=1,sticky='W')

#========Browse to copy that defined file to folder================
def browseBtnCopy():  #  Button to browse _Copy
    global copy_path
    askDirectoryCopy = filedialog.askdirectory()
    copy_path.set(askDirectoryCopy)
    os.chdir(askDirectoryCopy)
butBrsCopy = Button(app, text='Choose directory to copy',command=browseBtnCopy)
#=========Copy defined file to another folder=================
src = "C:/Users/phanh/source/repos/Lab1/private/"
dst = "C:/Users/phanh/source/repos/Lab1/public/"
def copyFile():
    res = os.path.exists(src+varCopy.get()+'.txt')
    if res is False:
        messagebox.showerror("User Application","No such file or directory! Type again!")
    else:
        shutil.copy(src+varCopy.get()+'.txt',dst)
        if os.path.isfile(dst+varCopy.get()+'.txt'):
            messagebox.showinfo("User Application","Successfully copy file to another folder!") #check if file exists or not, show messagebox!
        
butCopy = Button(app, text='Copy',command=copyFile)
butCopy.grid(row=9, column=1, sticky='W')

label5 = Label(app, text="Enter name of file to be copied:")
label5.grid(row=7,column=0,sticky='W')

varCopy = StringVar()
nameToCopy = Entry(app,textvariable=varCopy) #Entry to type name of file that you want to copy
nameToCopy.grid(column=0,row=8,ipady=5,ipadx=5,sticky='W')

#========Active Layout Window=============
label3.grid(row=5, column=0,sticky='W')
label4.grid(row=10,column=0,sticky='W')
butBrsSv.grid(row=4, column=0,sticky='W')
butBrsCopy.grid(row=9, column=0,sticky='W')
app.mainloop()
