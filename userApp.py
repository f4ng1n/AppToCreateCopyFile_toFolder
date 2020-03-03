import os,shutil,os.path, sys
from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox,filedialog
import ntpath as path


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
    fileName = filedialog.askdirectory()
    save_path.set(fileName)
    os.chdir(fileName)
butBrsSv = Button(app, text='Choose directory to save',command=browseBtnSave) #Button_browse directory to SAVE file

#=======Save file as name that user typed==============
var = StringVar()
editName = Entry(app,textvariable=var) #Entry to type name of file 
editName.grid(column=1,row=1,ipady=5,ipadx=5,sticky='NE')
def saveFileAsName():
    user_input=var.get()
    saveFileAsName = open((a),'w')
    #saveFileAsName = open((a + '.txt'),'w')
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

#========Browse to copy file to folder================
def browseBtnCopy():
    global copy_path
    fileName2 = filedialog.askdirectory()
    copy_path.set(fileName2)
    os.chdir(fileName2)
butBrsCopy = Button(app, text='Choose directory to copy',command=browseBtnCopy)

#=========Copy file to another folder=================
def CopyFile():
    src = 'C:/Users/phanh/source/repos/Lab1/private/'+var.get()+'.txt'
    dst = 'C:/Users/phanh/source/repos/Lab1/public'
   # src = 'save_path/'+var.get()+'.txt'
   # dst = 'copy_path/'+var.get()+'.txt'
    shutil.copyfile(src, dst[, length])

butCopy = Button(app, text='Copy',command=CopyFile)
butCopy.grid(row=7, column=1, sticky='W')


#========Active Layout Window=============
label3.grid(row=5, column=0,sticky='W')
label4.grid(row=7,column=0,sticky='W')
butBrsSv.grid(row=4, column=0,sticky='W')
butBrsCopy.grid(row=6, column=0,sticky='W')

current_work_directory = os.getcwd()    # Return a string representing the current working directory.
print('Current work directory: {}'.format(current_work_directory))
# Make sure it's an absolute path.
abs_work_directory = os.path.abspath(current_work_directory)
print('Current work directory (full path): {}'.format(abs_work_directory))
print()
script_directory = os.path.split(os.path.abspath(__file__))[0]
print(script_directory)


app.mainloop()
