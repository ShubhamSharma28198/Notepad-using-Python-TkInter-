from Tkinter import *
import tkFileDialog
import tkMessageBox


def doNothing():
    print("Hello.!!")


# ******** New ********

def new():
        f = root.title("Safwan's Notepad -New File-")
        s = None
        f.text.delete(1.0, END)
        s.read()

# ******** Open ********


def open():
    f = tkFileDialog.askopenfile(parent=root, mode='rb', title='Select a file')
    if f != None:
        contents = f.read()
        text.insert('1.0', contents)
        f.close()


# ******** Save ********

def save():
    contents = text.get(1.0, "end-1c")
    try:
        with open(str.f, 'w') as outputFile:
            outputFile.write(contents)
    except AttributeError:
        saveAs()


# ******** Save As ********

def saveAs():
    f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    textToSave = str(text.get(1.0, END))
    f.write(textToSave)
    f.close()

# ******** Cut ********


def cut():
        f = text.event_generate("<<Cut>>")
        f.generate()

# ******** Copy ********


def copy():
    f = text.event_generate("<<Copy>>")
    f.generate()

# ******** Paste ********


def paste():
    f = text.event_generate("<<Paste>>")
    f.generate()

# ******** About ********


def about():
        f = tkMessageBox.showinfo("About", "Safwan's Notepad \nBy Syed Safwan")
        f.append()

root = Tk()

root.title("Safwan's Editor")

# ******** Window Size ********


class windowSize:
    def __init__(self, master):
        master.minsize(width=500, height=400)

w = windowSize(root)

#root.geometry("500x500")


# ******** Text & Scroll Bar ********

text = Text(root)
text.pack(side=LEFT, fill=BOTH, expand=YES)
s = Scrollbar(root, command=text.yview)
s.pack(side=RIGHT, fill=Y)
text.configure(yscrollcommand=s.set, undo=True)


# ******** Menu Bar ********

menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=new)
fileMenu.add_command(label="Open", command=open)
fileMenu.add_separator()
fileMenu.add_command(label="Save", command=save)
fileMenu.add_command(label="Save As", command=saveAs)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

editMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

helpMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=about)

root.mainloop()