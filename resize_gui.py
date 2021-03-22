# ===================================================
# Module for implementing resizing by some percentage
# ===================================================
#
# This module is used to resize an image 
# with user giving what resize ratio/percentage

# Importing libraries
from tkinter import *
import tkinter as tk
from tkinter import filedialog,messagebox
import os
from PIL import Image,ImageTk
import cv2


img=" "                        # will contain image data
root=Tk()                      # GUI window
filename=StringVar()           # stores filename for display

w=StringVar()                  # stores width of original image
h=StringVar()                  # stores height of original image
percentage=StringVar()         # stores percentage value for resizing

def browseimg():               # function to load an image
    global img                 # globalizing the variable

    # this line opens up the usual 'Open' dialog box in Windows, for the user 
    # to choose a file. For now, we accept JPG and PNG files only

    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Browse image file",filetypes=(("JPG Image",".*jpg"),("PNG Image",".*png")))
    filename.set(fln)                             # file-path for image
    img=cv2.imread(fln,cv2.IMREAD_UNCHANGED)      # img now contains all the pixel data
    
    # width and height informatation extracted from image
    w.set(img.shape[0])
    h.set(img.shape[1])

def previewimg():            # displays image in a new window
    try:
        cv2.imshow("Source Image",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        messagebox.showerror("Error","File not found.")
        return

# This function recalculates the height and width of the image
# with respect to percentage resize given by user
def recalculate():       
    try:
        p=int(percentage.get())
        new_width=int(int(w.get())*p/100)
        new_height=int(int(h.get())*p/100)
        w.set(new_width)
        h.set(new_height)
    except:
        messagebox.showerror("Error","File not found.")
        return

def resize():
    try:
        nw=int(w.get())                     #new width
        nh=int(h.get())                     #new height
        resized_img=cv2.resize(img,(nh,nw),interpolation=cv2.INTER_AREA) # resize function
        return resized_img
    except:
        messagebox.showerror("Error","File not found.")  # else, error
        return

def preview_resized_img(): # resizing image
    try:
        resized_img=resize()                               # resize function
        cv2.imshow("Preview Resized Image",resized_img)    # displaying the resized result
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        messagebox.showerror("Error","File not found.")  # else, error
        return

def save_resized_img():  # function to save the newly generated image in a different file
    try:
        # this line opens up the usual 'Save as' dialog box in Windows, for the user 
        # to chhose a directory and  name the file . For now, we accept JPG and PNG files only

        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save image file",filetypes=(("JPG Image",".*jpg"),("PNG Image",".*png")))
        resized_img=resize()
        cv2.imwrite(fln, resized_img) # 'resized' image is written in the file path specified by user
        messagebox.showinfo("Image Saved ","image has been saved to "+os.path.basename(fln)+" successfully.")
    except:
        messagebox.showerror("Error","File not found.")  # else, error
        return

# function to change properties of button on hover 
def changeOnHover(button, colorOnHover, colorOnLeave): 
  
    # adjusting background of the widget 
    # background on entering widget 
    button.bind("<Enter>", func=lambda e: button.config( 
        background=colorOnHover)) 
  
    # background color on leving widget 
    button.bind("<Leave>", func=lambda e: button.config( 
        background=colorOnLeave)) 


def main(): # driver function to implement the window

    global root         # globalizing the variable
    global filename     # globalizing the variable

    # customizing background

    bg = ImageTk.PhotoImage(Image.open('bg2.jpg'))
    C = Canvas(root, height=700, width=900)
    background_label = Label(root, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # adding wrappers to divide the window into subsections
    

    # this one is for loading the image
    # 
    #
    wrapper=LabelFrame(root,text="Source File",bg="#a0cfe7")
    wrapper.pack(fill='both',expand='yes',padx=20,pady=20)

    # label
    lbl=Label(wrapper,text='Source file',bg="#a0cfe7")
    lbl.pack(side=tk.LEFT,padx=10,pady=10)

    # textbox box to display filepath
    ent=Entry(wrapper,textvariable=filename)
    ent.pack(side=tk.LEFT,padx=10,pady=10)

    # button to browse for image
    btn=Button(wrapper,text="Browse",command=browseimg,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    btn.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(btn, "#ff910c", "#e2c0b3")


    # button to view the original image 
    btn2=Button(wrapper,text="Preview",command=previewimg,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    btn2.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(btn2, "#ff910c", "#e2c0b3")


    # this one is for showing image details
    # 
    #
    wrapper2=LabelFrame(root,text="Image Details",bg="#a4b3da")
    wrapper2.pack(fill='both',expand='yes',padx=20,pady=20)

    
    #label
    lbl2=Label(wrapper2,text='Dimension',bg="#a4b3da")
    lbl2.pack(side=tk.LEFT,padx=10,pady=10) 

    #text field for width
    ent2=Entry(wrapper2,textvariable=w)
    ent2.pack(side=tk.LEFT,padx=10,pady=10)

    #label
    lbl3=Label(wrapper2,text='X',bg="#a4b3da")
    lbl3.pack(side=tk.LEFT,padx=5,pady=10) 

    #text field for height
    ent3=Entry(wrapper2,textvariable=h)
    ent3.pack(side=tk.LEFT,padx=5,pady=10)

    # this one is for getting user input for resizing percentage
    # 
    #
    wrapper3=LabelFrame(root,text="Pixel Safe",bg="#a4b3da")
    wrapper3.pack(fill='both',expand='yes',padx=20,pady=20)

    #label
    lbl4=Label(wrapper3,text='%',bg="#a4b3da")
    lbl4.pack(side=tk.LEFT,padx=10,pady=10) 

    #text field for percentage
    ent4=Entry(wrapper3,textvariable=percentage)
    ent4.pack(side=tk.LEFT,padx=10,pady=10)

    #button for recalculating dimenesions
    btn3=Button(wrapper3,text="Recalculate Dimension",command=recalculate,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    btn3.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(btn3, "#ff910c", "#e2c0b3")


    # this section is for viewing result and saving
    # 
    #
    wrapper4=LabelFrame(root,text="Actions",bg="#819dc7")
    wrapper4.pack(fill='both',expand='yes',padx=20,pady=20)

    #button to view the resized image before saving
    prvbtn=Button(wrapper4,text="Preview",command=preview_resized_img,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    prvbtn.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(prvbtn, "#ff910c", "#e2c0b3")


    #button to save the resized image
    savebtn=Button(wrapper4,text="Save",command=save_resized_img,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    savebtn.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(savebtn, "#ff910c", "#e2c0b3")


    root.title("Resize GUI")    # title of window
    root.geometry("800x600")    # size of window
    root.mainloop()             # keeps the window and its functionalities
                                # until it is closed

# actual main function                                
if __name__=="__main__":
    main()