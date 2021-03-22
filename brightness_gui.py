# =======================================
# Module for Changing Brightness of image
# =======================================
#
# This module allows the user to increase 
# or decrease brightness of an image


# Importing libraries

from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import filedialog,messagebox
import os
import cv2


img=" "                 # stores image data
root=Tk()               # GUI window
filename=StringVar()    # stores filename for display
deg=StringVar()         # input data for degree of filtering


def browseimg():        # function to load an image
    global img          # globalizing the variable
    global filename     # globalizing the variable

    # this line opens up the usual 'Open' dialog box in Windows, for the user 
    # to choose a file. For now, we accept JPG and PNG files only

    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Browse image file",filetypes=(("JPG Image",".*jpg"),("PNG Image",".*png")))
    filename.set(fln)                           # file-path for output
    img=cv2.imread(fln,cv2.IMREAD_UNCHANGED)    # img now contains all the pixel data
    
def previewimg():                               # to view the loaded image if loaded, else error msg
    try: 
        cv2.imshow("Source Image",img)          # displays image in a new window
        cv2.waitKey(0)                          
        cv2.destroyAllWindows()
    except:
        messagebox.showerror("Error","File not found.") # else, error
        return

def bright():    # function to change brightness
    global img
    
    try:
        degree=int(deg.get())                       # accepts the change in brightness value
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # array storing for hue, saturation, and brightness
        h, s, v = cv2.split(hsv)                    # splitting array into its smaller components
        v = cv2.add(v, degree)                      # adding the factor of brightness change
        img = cv2.merge((h, s, v))                  # merging h,s,v back
        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)  # converting back to normal format from HSV
        return img                                  # returns the variable with 'brightened' pixel data
    except: 
        messagebox.showerror("Error","Possibilities: value entered not an integer, file not loaded, or image is not in RGB format") # else, error
        return


def preview_bright_img():                           # function to preview brightened image
    try:
        brightened=bright()                        # bright() is called
        cv2.imshow("Preview brightened Image",brightened) # displays image in a new window
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        messagebox.showerror("Error","File not found.") # else, error
        return


def save_bright_img():          # function to save the newly generated image in a different file
    try:    
        # this line opens up the usual 'Save as' dialog box in Windows, for the user 
        # to chhose a directory and  name the file . For now, we accept JPG and PNG files only

        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save image file",filetypes=(("JPG Image",".*jpg"),("PNG Image",".*png"),("JPEG Image",".*jpeg")))
        brightened=bright()            # bright() is called
        cv2.imwrite(fln,brightened)    # 'brightened' image is written in the file path specified by user

        # display message of successful saving of file
        messagebox.showinfo("Image Saved ","image has been saved to "+os.path.basename(fln)+" successfully.")
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

    # box to display filepath
    ent=Entry(wrapper,textvariable=filename)
    ent.pack(side=tk.LEFT,padx=10,pady=10)

    # button to browse for image
    btn=Button(wrapper,text="Browse",command=browseimg,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    btn.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(btn, "#ff910c", "#e2c0b3")

    # button to view the image before brightness change is done
    btn2=Button(wrapper,text="Preview",command=previewimg,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    btn2.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(btn2, "#ff910c", "#e2c0b3")


    # this section is for taking input and filtering
    #
    #
    wrapper2=LabelFrame(root,text="Change Brightness",bg="#a4b3da")
    wrapper2.pack(fill='both',expand='yes',padx=20,pady=20)

    # label
    lbl4=Label(wrapper2,text='Enter change in value',bg="#a4b3da")
    lbl4.pack(side=tk.LEFT,padx=10,pady=10) 

    # text box to accept the degree of brightness
    ent4=Entry(wrapper2,textvariable=deg)
    ent4.pack(side=tk.LEFT,padx=10,pady=10)

    # button to implement brightness change
    btn3=Button(wrapper2,text="Apply Change",command=bright,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    btn3.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(btn3, "#ff910c", "#e2c0b3")


    # this section is for viewing result and saving
    #
    #
    wrapper3=LabelFrame(root,text="Actions",bg="#819dc7")
    wrapper3.pack(fill='both',expand='yes',padx=20,pady=20)

    # button to view the modified image before saving
    prvbtn=Button(wrapper3,text="Preview",command=preview_bright_img,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    prvbtn.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(prvbtn, "#ff910c", "#e2c0b3")

    # button to save the modified image
    savebtn=Button(wrapper3,text="Save",command=save_bright_img,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    savebtn.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(savebtn, "#ff910c", "#e2c0b3")


    root.title("Brightening")      # title of window
    root.geometry("500x400")            # size of window
    root.mainloop()                     # keeps the window and its functionalities
                                        # until it is closed

# actual main function
if __name__=="__main__":
    main()