from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import  askopenfilename , asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()

def cut():
    print(textarea.event_generate("<<Cut>>"))
def copy():
    print(textarea.event_generate("<<Copy>>"))
def paste():
    print(textarea.event_generate("<<paste>>"))




def about():
    showinfo("Notepad","by deepanshu tyagi")
root = Tk()
root.geometry("500x500")
root.title("Untitled - Notepad")
menu1 = Menu(root)
root.config(menu=menu1)
filemenu = Menu(root, tearoff=0)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Exit", command=exit)
menu1.add_cascade(label="File", menu=filemenu)

editmenu = Menu(root, tearoff=0)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)
menu1.add_cascade(label="Edit", menu=editmenu)

aboutmenu = Menu(root, tearoff=0)
aboutmenu.add_command(label="about", command=about)
menu1.add_cascade(label="Help", menu=aboutmenu)

textarea = Text(root, font="lucida 13")
textarea.pack(expand=True, fill='both')
scrollbar = Scrollbar(textarea)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=textarea.yview)
textarea.config(yscrollcommand=scrollbar.set)
root.mainloop()
