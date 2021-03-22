# =========================================
# Module for implementing Binary conversion 
# =========================================
#
# This module is used for converting an
# image to binary format (pure black 
# and white)


# Importing libraries

from tkinter import *
import tkinter as tk        
from tkinter import filedialog,messagebox
from PIL import Image,ImageTk
import os
import cv2

img=""                      # stores image data
root=Tk()                   # GUI window
filename=StringVar()        # stores filename for display


def browseimg():            # function to load an image
    global img              # globalizing the variable
    global filename         # globalizing the variable

    # this line opens up the usual 'Open' dialog box in Windows, for the user 
    # to choose a file. For now, we accept JPG and PNG files only

    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Browse image file",filetypes=(("JPG Image",".*jpg"),("PNG Image",".*png")))
    filename.set(fln)                           # file-path for image
    img=cv2.imread(fln,cv2.IMREAD_UNCHANGED)    # img now contains all the pixel data

def previewimg():                               # to view the loaded image if loaded, else error msg
    try: 
        cv2.imshow("Source Image",img)          # displays image in a new window
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        messagebox.showerror("Error","File not found.") # else, error
        return

def preview_binary_image():
    try:
        img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)               # grayscale conversion    
        ret, img2=cv2.threshold(img1,128,255,cv2.THRESH_BINARY) # binary conversion 
                                                                # if pixel value is more than 128 it
                                                                # is converted to white
        cv2.imshow("Binary image",img2)                         # displaying binary image
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return img2                     # returning binary image data
    except:     
        messagebox.showerror("Error","File not found.")         # else, error
        return


def save_binary_img():      # function to save the newly generated image in a different file

    try:

        # this line opens up the usual 'Save as' dialog box in Windows, for the user 
        # to chhose a directory and  name the file . For now, we accept JPG and PNG files only\

        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save image file",filetypes=(("JPG Image",".*jpg"),("PNG Image",".*png")))
        img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)               # grayscale conversion 
        ret, img2=cv2.threshold(img1,128,255,cv2.THRESH_BINARY) # binary conversion 
        cv2.imwrite(fln,img2)       # binary image is written in path specified by user
        messagebox.showinfo("Image Saved ","image has been saved to "+os.path.basename(fln)+" successfully.")   # confirmation of save
    except:
        messagebox.showerror("Error","File not found.") # else, error
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


def main():             # driver function to implement the window 
    global root         # globalizing the variable
    global filename     # globalizing the variable
  
    # background customization

    bg = ImageTk.PhotoImage(Image.open('bg2.jpg'))
    C = Canvas(root, height=700, width=900)
    background_label = Label(root, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # adding wrappers to divide the window into subsections
    

    # this one is for loading the image
    # 
    #
    wrapper=LabelFrame(root,text="Source",bg="#a0cfe7")
    wrapper.pack(fill='both',expand='yes',padx=20,pady=20)

    # label
    lbl=Label(wrapper,text='Source file : ',bg="#a0cfe7")
    lbl.pack(side=tk.LEFT,padx=10,pady=10)

    # textbox box to display filepath
    ent=Entry(wrapper,textvariable=filename)
    ent.pack(side=tk.LEFT,padx=10,pady=10)

    # button to browse for image
    btn=Button(wrapper,text="Browse",command=browseimg,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    btn.pack(side=tk.LEFT,padx=10)
    changeOnHover(btn, "#ff910c", "#e2c0b3")

    # button to view the image before binary conversion is done
    btn2=Button(wrapper,text="Preview",command=previewimg,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    btn2.pack(side=tk.LEFT,padx=10)
    changeOnHover(btn2, "#ff910c", "#e2c0b3")

    # this section is for viewing result and saving
    #
    #
    wrapper2=LabelFrame(root,text="Binary Conversion",bg="#a4b3da")
    wrapper2.pack(fill='both',expand='yes',padx=20,pady=20)
    
    # button to view the binary image before saving
    prvbtn=Button(wrapper2,text="Preview",command=preview_binary_image,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    prvbtn.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(prvbtn, "#ff910c", "#e2c0b3")

    # button to save the binary image
    savebtn=Button(wrapper2,text="Save",command=save_binary_img,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    savebtn.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(savebtn, "#ff910c", "#e2c0b3")


    root.title("Color to binary")       # title of window
    root.geometry("500x300")            # size of window
    root.mainloop()                     # keeps the window and its functionalities
                                        # until it is closed

# actual main function
if __name__=="__main__":
    main()