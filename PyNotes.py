from tkinter import *
from tkinter.filedialog import *
import tkinter.font as tkfont

filename = None
current_font_size = 12
dark_mode = False
wrap_on = True

# Function to create a new file
def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

# Function to save a file
def saveFile():
    global filename
    if filename == "Untitled" or filename is None:
        saveAs()
    else:
        t = text.get(0.0, END)
        with open(filename, "w") as f:
            f.write(t)

# Function to save a file with dialog box
def saveAs():
    f = asksaveasfile(mode= "w", defaultextension='.txt')
    if f:
        filename = f.name
        t = text.get(0.0, END)
        f.write(t.rstrip())
        f.close()

# Function to open a file
def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

# Functions for Text Formatting
def make_bold():
    text.tag_add("bold", "sel.first", "sel.last")

def make_italic():
    text.tag_add("italic", "sel.first", "sel.last")

def make_underline():
    text.tag_add("underline", "sel.first", "sel.last")

# Functions for Undo/Redo
def undo():
    text.edit_undo()

def redo():
    text.edit_redo()

# Functions for Zooming in and out
def zoom_in():
    global current_font_size
    current_font_size += 2
    text.config(font=("Arial", current_font_size))

def zoom_out():
    global current_font_size
    current_font_size -= 2
    text.config(font=("Arial", current_font_size))

# Function for Dark Mode
def toggle_dark_mode():
    global dark_mode
    if dark_mode:
        text.config(bg="white", fg="black", insertbackground="black")
        dark_mode = False
    else:
        text.config(bg="#1e1e1e", fg="white", insertbackground="white")
        dark_mode = True

# Function for Word Wrap
def toggle_wrap():
    global wrap_on
    if wrap_on:
        text.config(wrap=NONE)
        wrap_on = False
    else:
        text.config(wrap=WORD)
        wrap_on = True

# Tkinter GUI Code
root = Tk()

try:
    root.iconbitmap("icon.ico")
except:
    icon = PhotoImage(file="icon.png")
    root.iconbitmap(True, icon)
    
root.title("PyNotes")
root.minsize(width=1366, height=768)
root.maxsize(width=1920, height=1080)

# Text Box to enter texts
text = Text(root, width=1366, height=768, undo=True)

# Creating Font Styles
default_font = tkfont.Font(font=text["font"])

bold_font = tkfont.Font(text, default_font)
bold_font.configure(weight="bold")

italic_font = tkfont.Font(text, default_font)
italic_font.configure(slant="italic")

undeline_font = tkfont.Font(text, default_font)
undeline_font.configure(underline=1)

text.tag_configure("bold", font=bold_font)
text.tag_configure("italic", font=italic_font)
text.tag_configure("underline", font=undeline_font)

text.pack()

# Menu Bar
menubar = Menu(root)
filemenu = Menu(menubar) # File Menu
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar) # Edit Menu
editmenu.add_command(label="Undo", command=undo)
editmenu.add_command(label="Redo", command=redo)
editmenu.add_separator()
editmenu.add_command(label="Bold", command=make_bold)
editmenu.add_command(label="Italic", command=make_italic)
editmenu.add_command(label="Underline", command=make_underline)
menubar.add_cascade(label="Edit", menu=editmenu)

viewmenu = Menu(menubar) # View Menu
viewmenu.add_command(label="Zoom In", command=zoom_in)
viewmenu.add_command(label="Zoom Out", command=zoom_out)
viewmenu.add_separator()
viewmenu.add_command(label="Dark Mode", command=toggle_dark_mode)
viewmenu.add_command(label="Word Wrap", command=toggle_wrap)
menubar.add_cascade(label="View", menu=viewmenu)

root.config(menu=menubar)
root.mainloop()