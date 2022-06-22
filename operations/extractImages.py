import tkinter as tk
from tkinter import filedialog
from functools import partial
from bing_images import bing
import subprocess
import sys
import webbrowser





def extract(a,b,c):
    bing.download_images(str(b.get()),
                      int(c.get()),
                      output_dir=str(a.get()),
                      pool_size=1,
                      file_type="jpg",
                      force_replace=True,
                      extra_query_params='&first=1')

    path = str(a.get())
    webbrowser.open(path)
    a.delete(0, tk.END)
    b.delete(0, tk.END)
    c.delete(0, tk.END)
    
   

    


def selectDir(dirs):
    folder_selected = filedialog.askdirectory()
    print(folder_selected)
    dirs.delete(0, tk.END)
    dirs.insert(0, folder_selected)


def extractImages():
    win = tk.Tk()
    win.title("Image Extraction")
    ffg = 'black'
    win.geometry("700x300")

    head = tk.Label(win, text="Please select path to store respective images")
    head.config(font=('Open Sans', 10), fg=ffg)
    head.place(x=5, y=13)
    paths = tk.StringVar()
    query = tk.StringVar()
    imgnum = tk.IntVar()
    paths.set("dsf")

    dirs = tk.Entry(win, bd=3, width=40)
    dirs.config(font=('Open Sans', 10), fg=ffg)
    dirs.place(x=280, y=13)

    enterBorder = tk.Frame(
        win, highlightbackground="black", highlightthickness=2, bd=0)
    enter = tk.Button(enterBorder, text='..', fg='black', font=(
        ("Times New Roman"), 11), command=partial(selectDir, dirs))
    enter.pack()
    enterBorder.place(x=570, y=13)

    searchs = tk.Label(win, text="Enter search query to extract images:")
    searchs.config(font=('Open Sans', 10), fg=ffg)
    searchs.place(x=50, y=103)

    searchQuery = tk.Entry(win, bd=3, width=40)
    searchQuery.config(font=('Open Sans', 10), fg=ffg)
    searchQuery.place(x=280, y=103)

    images = tk.Label(win, text="Number of Images needed? :")
    images.config(font=('Open Sans', 10), fg=ffg)
    images.place(x=50, y=143)

    image_num = tk.Entry(win, bd=3, width=10)
    image_num.config(font=('Open Sans', 10), fg=ffg)
    image_num.place(x=280, y=143)

    executeBorder = tk.Frame(
        win, highlightbackground="black", highlightthickness=2, bd=0)
    execute = tk.Button(executeBorder, text='Submit', fg='black', font=(
        ("Times New Roman"), 15), command=partial(extract, dirs,searchQuery,image_num))
    execute.pack()
    executeBorder.place(x=300, y=250)

    win.mainloop()
