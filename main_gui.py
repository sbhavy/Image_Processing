# =======================================
# Module for implementing the application
# =======================================
#
# This module combines all the
# image-processing functionalities and 
# allows the user to access them from here

# Importing libraries

import os
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk

def run_gray():                         # function to start the gray scale module when called
    root.destroy()                      # destroy the main window
    os.system('python gray_gui.py')     # the gray scale module starts
    main()                              # after exiting gray module main GUI starts again

def run_median():                       # function to start the median filter module when called
    root.destroy()
    os.system('python median_gui.py')   # the median filter module starts
    main()

def run_rotate():                       # function to start the rotate module when called
    root.destroy()
    os.system('python rotate_gui.py')   # the rotation module starts
    main()

def run_resize():                       # function to start the resize module when called
    root.destroy()
    os.system('python resize_gui.py')   # the resize module starts
    main()

def run_bright():                       # function to start the bright module when called
    root.destroy()
    os.system('python brightness_gui.py')   # the bright module starts
    main()

def run_crop():                       # function to start the crop module when called
    root.destroy()
    os.system('python crop_gui.py')   # the crop module starts
    main()

def run_binary():                       # function to start the binary module when called
    root.destroy()
    os.system('python binary_gui.py')   # the binary module starts
    main()

def run_sharp():                       # function to start the sharp module when called
    root.destroy()
    os.system('python sharp_gui.py')   # the sharp module starts
    main()

# function to change properties of button on hover 
def changeOnHover(button, colorOnHover, colorOnLeave): 
  
    # adjusting background of the widget 
    # background on entering widget 
    button.bind("<Enter>", func=lambda e: button.config( 
        background=colorOnHover)) 
  
    # background color on leving widget 
    button.bind("<Leave>", func=lambda e: button.config( 
        background=colorOnLeave)) 

# main function that implements the window to choose functionalities

def main():
    global root                         # globalising variable
    # intializes the window
    root=tk.Tk()

    bg = ImageTk.PhotoImage(Image.open('bg.jpg'))
    C = Canvas(root, height=700, width=900)
    background_label = Label(root, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


    # wrapper is used to divide the window into multiple parts
    #
    #

    # this wrapper is for some menu text
    
    wrapper=Frame(root,bg="#28394b")
    wrapper.pack(fill='both',expand='yes',padx=20,pady=20)

    

    # general menu text
    txt1=Text(wrapper,bg="#28394b",fg="white",font="Arial")
    txt1.insert(INSERT,"\t\t\t\t  Welcome!!!!!!")
    txt1.insert(INSERT,"\n\n\n\nHere are the list of functionalities provided : ")
    txt1.insert(INSERT,"\n\n 1. Gray Filter")
    txt1.insert(INSERT,"\n\n 2. Median filter")
    txt1.insert(INSERT,"\n\n 3. Image Rotation")
    txt1.insert(INSERT,"\n\n 4. Image Resize")
    txt1.insert(INSERT,"\n\n 5. Brightness Change")
    txt1.insert(INSERT,"\n\n 6. Image Crop")
    txt1.insert(INSERT,"\n\n 7. Binary Filter")
    txt1.insert(INSERT,"\n\n 8. Image Sharpening")

    txt1.insert(INSERT,"\n\n\n\nClick on the filter you want : ")
    txt1.configure(state="disabled")
    txt1.pack()
    
    # this wrapper contains buttons which
    # when clicked will redirect to
    # the desired functionality

    wrapper2=Frame(root,bg="#28394b")
    wrapper2.pack(fill='both',expand='yes',padx=40,pady=40)
    
    # gray scale button
    btn=Button(wrapper2,text="Gray",command=run_gray,bg="#9b9e9f",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    btn.pack(side=tk.LEFT,padx=10)
    changeOnHover(btn, "#ff910c", "#9b9e9f")

    # median filter button
    btn2=Button(wrapper2,text="Median",command=run_median,bg="#9b9e9f",activebackground='#ff910c',activeforeground='white',cursor="circle")
    btn2.pack(side=tk.LEFT,padx=10)
    changeOnHover(btn2, "#ff910c", "#9b9e9f")

    # rotation button
    btn3=Button(wrapper2,text="Rotate",command=run_rotate,bg="#9b9e9f",activebackground='#ff910c',activeforeground='white',cursor="circle")
    btn3.pack(side=tk.LEFT,padx=10)
    changeOnHover(btn3, "#ff910c", "#9b9e9f")

    # resizing button
    btn4=Button(wrapper2,text="Resize",command=run_resize,bg="#9b9e9f",activebackground='#ff910c',activeforeground='white',cursor="circle")
    btn4.pack(side=tk.LEFT,padx=10)
    changeOnHover(btn4, "#ff910c", "#9b9e9f")

    # brightness button
    btn5=Button(wrapper2,text="Brightness",command=run_bright,bg="#9b9e9f",activebackground='#ff910c',activeforeground='white',cursor="circle")
    btn5.pack(side=tk.LEFT,padx=10)
    changeOnHover(btn5, "#ff910c", "#9b9e9f")

    # crop button
    btn6=Button(wrapper2,text="Crop",command=run_crop,bg="#9b9e9f",activebackground='#ff910c',activeforeground='white',cursor="circle")
    btn6.pack(side=tk.LEFT,padx=10)
    changeOnHover(btn6, "#ff910c", "#9b9e9f")

    # binary button
    btn7=Button(wrapper2,text="Binary",command=run_binary,bg="#9b9e9f",activebackground='#ff910c',activeforeground='white',cursor="circle")
    btn7.pack(side=tk.LEFT,padx=10)
    changeOnHover(btn7, "#ff910c", "#9b9e9f")

    # sharpening button
    btn8=Button(wrapper2,text="Sharpen",command=run_sharp,bg="#9b9e9f",activebackground='#ff910c',activeforeground='white',cursor="circle")
    btn8.pack(side=tk.LEFT,padx=10)
    changeOnHover(btn8, "#ff910c", "#9b9e9f")

    C.pack()

    root.title("Main GUI")          # title of window
    root.geometry("900x750")        # size of window
    root.mainloop()                 # keeps the window and its functionalities
                                    # until it is closed

# actual main function                                    
if __name__=="__main__":
    main()
    
