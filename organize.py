__author__ = "Manish Choudhary @expert.py"
__copyright__ = "Copyright (C) 2022 Manish Choudharye"
__license__ = "Public Domain"
__version__ = "1.0"


import os
import shutil
from tkinter import *
from tkinter import filedialog, messagebox

Gopen_file = ''

def foldername(extension):
    if(extension == ""):
        return None
    else:
        switcher = {
            "exe"  : "Software", 
            "msi"  : "Software", 
            "txt"  : "Notes-Text", 
            "text"  : "Notes-Text", 
            "pdf"  : "PDFs", 
            "c"    : "C programs", 
            "py"   : "Python files",
            "java" : "Java programs",
            "class": "Java programs", 
            "cpp"  : "Cpp programs", 
            "jpg"  : "Images", 
            "png"  : "Images",
            "bmp"  : "Images",
            "gif"  : "Images",  
            "jpeg" : "Images", 
            "raw"  : "Images",
            "mp3"  : "Music",
            "wav"  : "Music", 
            "mp4"  : "Videos", 
            "mkv"  : "Videos",
            "ppt"  : "Ppt files",
            "pptx"  : "Ppt files",
            "doc"  : "Documents",
            "docx"  : "Documents",
            "rtf"  : "Documents",
            "cdr"  : "Corel Draw",
            "psd" : "photoshop file",
            "dll"  : "Operating system files",
            "xls" : "Spreadsheet files",
            "xlsx" : "Spreadsheet files",
            "xlr" : "Spreadsheet files",
            "csv" : "Spreadsheet files",
            "zip" : "Compress File",
            "7zip" : "Compress File",
            "apk" : "Android Application",
            "avi" : "Videos",	
            "flv" : "Videos",	
            "h264" : "Videos",	
            "m4v" : "Videos",	
            "mkv" : "Videos",
            "mov" : "Videos",
            "mp4" : "Videos",
            "mpg" : "Videos",
            "mpeg" : "Videos",	
            "rm" : "Videos",	
            "swf" : "Videos",	
            "vob" : "Videos",	
            "wmv" : "Videos",	
            "3g2" : "Videos",	
            "3gp" : "Videos",
            "asf" : "Videos",
            "7z" : "Compress File",
            "arj" : "Compress File",
            "deb" : "Compress File",
            "pkg" : "Compress File",
            "rpm" : "Compress File",
            "rar" : "Compress File",
            "targz" : "Compress File",
            "fnt" : "Font Files",
            "fon" : "Font Files",
            "otf" : "Font Files",
            "ttf" : "Font Files",
            "ai" : "Vector file",
            "bmp" : "Images",
            "gif" : "Images",
            "ico" : "Vector file",
            "svg" : "Vector file",
            "tif" : "Vector file",
            "tiff" : "Vector file"
        }
        return switcher.get(extension, "Extras") #returns "Extras" if not in dictionary


FILE_NAME = "organize.py"


def organize_files(path):
    global Gopen_file
    if not os.path.exists(path):
        print("ERROR! Invalid location")
        messagebox.showerror("Error", "Invalid location")
        return

    files = os.listdir(path)
    extns = {os.path.splitext(file)[1].strip(".") for file in files}

    # Create Folders
    for ext in extns:
        folder = foldername(ext) or ''
        new = os.path.join(path, folder)
        if folder and not os.path.exists(new):
            os.makedirs(new)

    # Move Files To Folders
    for file in files:
        if file in [FILE_NAME]:
            continue

        ext = os.path.splitext(file)[1].strip(".")
        folder = foldername(ext)
        if not folder:
            continue

        src = os.path.join(path, file)
        dest = os.path.join(path, folder, file)

        if not os.path.exists(dest):
            shutil.move(src, dest)
            print(f"Moved {file} to {folder}")

    print(f"\nSUCCESS! All files organized in {path}")
    # messagebox
    messagebox.showinfo("Success", "All files organized in " + path)
    Gopen_file = ''
    lbl2.config(text='')





def organize_files2():
    global Gopen_file
    location = Gopen_file
    if not location:
        print("ERROR! Invalid location")
        messagebox.showerror("Error", "Invalid location")
    else:
        organize_files(location)







win=Tk()
win.title('Instagram : @Expert.py File Organizer')
win.geometry("800x300")




lbl1=Label(win, text='Choose Location :  ')
lbl1.grid(row=1,column=0, sticky=E)

# label 
lbl3=Label(win, fg='green', text='Selected folder : ')
lbl3.grid(row=2,column=0, sticky=E)

lbl2=Label(win, fg='green', text='--Not Selected--')
lbl2.grid(row=2,column=1,sticky = W)

def organize_files3():
    global Gopen_file
    open_file = filedialog.askdirectory() # Returns opened path as str
    Gopen_file = open_file
    lbl2.config(text=open_file)

# button
btn1=Button(win, text='Browse', width=70 ,bg='Brown', fg='White',command=organize_files3)
btn1.grid(row=1,column=1,pady=30)


btn1 = Button(win, text='Organize', bg='blue', fg='White',command=organize_files2, font=('Arial', 15), width=20, height=2, relief=RAISED, bd=5, activebackground='red', activeforeground='white', cursor='hand2', state=NORMAL, overrelief=RIDGE)
btn1.grid(row=3,column=0,columnspan=2,pady=30)

lll = Label(win, text='Developed by : Manish Choudhary    Instagram : @Expert.py', fg='blue', font=('Arial', 10))
lll.grid(row=4,column=0,columnspan=2,pady=30)


win.mainloop()