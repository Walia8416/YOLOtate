import tkinter as tk
from tkinter.ttk import *
from operations.annotateImages import annotateImages

from operations.extractImages import extractImages


def operationGiver():
    if var.get() == 1:
        extractImages()

    else:
        annotateImages()


ffg = 'black'
menu = tk.Tk()
menu.resizable(False, False)
menu.title("YOLOtate")
menu.geometry("500x400")
photo = tk.PhotoImage(file="./resources/icons.png")
menu.iconphoto(False, photo)

menubar = tk.Menu(menu)

menubar.add_command(label="About")
menu.config(menu=menubar)


head = tk.Label(menu, text="YOLOtate")
head.config(font=('Courier', 35, 'bold', 'underline'), fg=ffg)
head.place(x=140, y=10)

sub = tk.Label(menu, text="Generating datasets hasn't been easier!")
sub.config(font=('Segoe Script', 10), fg=ffg)
sub.place(x=190, y=70)

var = tk.IntVar()
R1 = tk.Radiobutton(menu, text="Extract Images", variable=var, value=1)
R1.config(font=('Arial', 17))
R1.place(x=25, y=250)

R2 = tk.Radiobutton(menu, text="Annotate Images", variable=var, value=2)
R2.config(font=('Arial', 17))
R2.place(x=25, y=300)


enterBorder = tk.Frame(menu, highlightbackground="black",
                       highlightthickness=2, bd=0)
enter = tk.Button(enterBorder, text='Submit', fg='black',
                  font=(("Times New Roman"), 15), command=operationGiver)


enter.pack()
enterBorder.place(x=350, y=300)


menu.mainloop()
