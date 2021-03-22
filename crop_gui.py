# ======================================
# Module for implementing Image cropping
# ======================================
#
# This module deals with the cropping of
# images by making the user create a 
# rectangular region which they want to 
# extract.

# Importing libraries

from tkinter import *
import tkinter as tk
from tkinter import filedialog,messagebox
from PIL import Image,ImageTk
import os
import cv2


img=" "                 # stores image data
img1=" "                # stores copy of above variable
root=Tk()               # GUI window
filename=StringVar()    # stores filename for display
crop_region = []        # stores coordinates for cropping
crop_img=" "            # saving the cropped part

def browseimg():        # function to load an image
    global img          # globalizing the variable
    global img1
    global filename     # globalizing the variable

    # this line opens up the usual 'Open' dialog box in Windows, for the user 
    # to choose a file. For now, we accept JPG and PNG files only

    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Browse image file",filetypes=(("JPG Image",".*jpg"),("PNG Image",".*png")))
    filename.set(fln)                           # file-path for output
    img=cv2.imread(fln,cv2.IMREAD_UNCHANGED)    # img now contains all the pixel data
    img1=cv2.imread(fln,cv2.IMREAD_UNCHANGED)
    
def previewimg():                               # to view the loaded image if loaded, else error msg
    try: 
        cv2.imshow("Source Image",img1)          # displays image in a new window
        cv2.waitKey(0)                          
        cv2.destroyAllWindows()
    except:
        messagebox.showerror("Error","File not found.") # else, error
        return

def shape_selection(event,x,y,flags,param):     # utility function to draw a rectangle around
                                                # the crop region to make the user aware
    
    global crop_region, img, img1               # globalizing the variables
    
    if event == cv2.EVENT_LBUTTONDOWN:          # when left mouse button is first pressed the coordinates are recorded
        crop_region = [(x, y)] 
  
    elif event == cv2.EVENT_LBUTTONUP:           # when left mouse button is released the coordinates are recorded
        crop_region.append((x, y)) 
  
        cv2.rectangle(img, crop_region[0], crop_region[1], (0, 255, 0), 2)  # drawing rectangle around cropping region
        cv2.imshow("image", img)  # displaying image + the region
    
    img=img1.copy()               # clearing the image for next iteration, if any

def crop_out():                   # function to do the cropping
    global crop_img, img, img1    # globalizing the variables                      
    try:
        clone = img.copy()            # creating copy of current image
        cv2.namedWindow("image")      # giving name to window in which cropping area will be selected
        cv2.setMouseCallback("image", shape_selection)  # shape-selection is invoked
        cv2.imshow("image", img) 
        
        while True:     # infinite loop for infinite tries at cropping
            key = cv2.waitKey(1) & 0xFF 
        
            if key == ord("c"): # if keyboard 'C' is pressed then loop is exited
                break
        
        if len(crop_region) == 2: # if cropping area is decided, then region is extracted
            crop_img = clone[crop_region[0][1]:crop_region[1][1], crop_region[0][0]: 
                                                                crop_region[1][0]] 
        cv2.destroyAllWindows()
    except:
        messagebox.showerror("Error","File not found.") # else, error
        return

def preview_crop_img():                           # function to preview cropped part image
    try:
        cv2.imshow("Preview Cropped Image",crop_img) # displays image in a new window
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        messagebox.showerror("Error","File not found.") # else, error
        return


def save_crop_img():          # function to save the newly generated image in a different file
    try:    
        # this line opens up the usual 'Save as' dialog box in Windows, for the user 
        # to chhose a directory and  name the file . For now, we accept JPG and PNG files only

        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save image file",filetypes=(("JPG Image",".*jpg"),("PNG Image",".*png"),("JPEG Image",".*jpeg")))
        cv2.imwrite(fln,crop_img)    # 'cropped' image is written in the file path specified by user

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

    # button to view the image before cropping is done
    btn2=Button(wrapper,text="Preview",command=previewimg,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    btn2.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(btn2, "#ff910c", "#e2c0b3")

    # this section is for cropping
    #
    #
    wrapper2=LabelFrame(root,text="Cropping",bg="#a4b3da")
    wrapper2.pack(fill='both',expand='yes',padx=20,pady=20)

    lbl=Label(wrapper2,text='Press C to exit after choosing area or to redo cropping',bg="#a4b3da")
    lbl.pack(side=tk.LEFT,padx=10,pady=10)

    # button to implement cropping
    btn3=Button(wrapper2,text="Crop Image",command=crop_out,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    btn3.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(btn3, "#ff910c", "#e2c0b3")

    # this section is for viewing result and saving
    #
    #
    wrapper3=LabelFrame(root,text="Actions",bg="#819dc7")
    wrapper3.pack(fill='both',expand='yes',padx=20,pady=20)

    # button to view the cropped image before saving
    prvbtn=Button(wrapper3,text="Preview",command=preview_crop_img,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    prvbtn.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(prvbtn, "#ff910c", "#e2c0b3")

    # button to save the cropped image
    savebtn=Button(wrapper3,text="Save",command=save_crop_img,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    savebtn.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(savebtn, "#ff910c", "#e2c0b3")

    root.title("Cropping")              # title of window
    root.geometry("500x400")            # size of window
    root.mainloop()                     # keeps the window and its functionalities
                                        # until it is closed

# actual main function
if __name__=="__main__":
    main()