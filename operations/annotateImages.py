from functools import partial
import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image
import cv2


def selectDir(dirs):
    folder_selected = filedialog.askdirectory()
    print(folder_selected)
    dirs.delete(0, tk.END)
    dirs.insert(0, folder_selected)


def drawBoundBox(event,x,y,flags,param):
    global x1,y1,x2,y2,dragging
    dragging = False
    if (event == cv2.EVENT_LBUTTONDOWN):
        x1,y1 = x,y
        dragging = True

    elif (event == cv2.EVENT_MOUSEMOVE):
        if(dragging == True):
            cv2.rectangle(param[0],(x1,y1),(x,y),(255,0,0))
           
            

    elif (event == cv2.EVENT_LBUTTONUP):
        x2,y2 = x,y
        dragging=False
        cv2.rectangle(param[0],(x1,y1),(x2,y2),(255,0,0))
        print(x1,y1,x2,y2)
        


        



def iterateImages(dirs):
    for images in os.listdir(dirs.get()):
        
        gg = str(dirs.get()+"/"+images)
        gg.replace('/','\\')
        print(gg)
        im = cv2.imread(gg)
        im = cv2.resize(im,(600,600))
        cv2.namedWindow("bru")
        param = [im,images]
        cv2.setMouseCallback('bru',drawBoundBox,param)
        while(1):
            cv2.imshow("bru",im)
            k = cv2.waitKey(1) & 0xFF
            if (k==27):
                break;
        cv2.destroyAllWindows()
            
    
       
      



def annotateImages():
    win = tk.Tk()
    win.title("Image Annotation")
    ffg = 'black'
    win.geometry("300x200")

    head = tk.Label(win, text="Please select path to images:-")
    head.config(font=('Open Sans', 10), fg=ffg)
    head.place(x=5, y=13)
    
  

    dirs = tk.Entry(win, bd=3, width=30)
    dirs.config(font=('Open Sans', 10), fg=ffg)
    dirs.place(x=16, y=63)

    enterBorder = tk.Frame(
        win, highlightbackground="black", highlightthickness=2, bd=0)
    enter = tk.Button(enterBorder, text='..', fg='black', font=(
        ("Times New Roman"), 11), command=partial(selectDir, dirs))
    enter.pack()
    enterBorder.place(x=240, y=60)

    executeBorder = tk.Frame(
        win, highlightbackground="black", highlightthickness=2, bd=0)
    execute = tk.Button(executeBorder, text='Begin', fg='black', font=(
        ("Times New Roman"), 15),command=partial(iterateImages,dirs))
    execute.pack()
    executeBorder.place(x=200, y=150)
    

    win.mainloop()
