# ========================================
# Module for implementing Median filtering
# ========================================
#
# Median filtering is a process in image 
# processing that essentially 'smoothens'
# an image. This is particularly useful
# when we want to remove 'salt-and pepper'
# noise (small white dots, degrading quality)


# Importing libraries

from tkinter import *
import tkinter as tk
from tkinter import filedialog,messagebox
import os
from PIL import Image,ImageTk
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

def median():                                       # function to do the filtering
    try:
        degree=int(deg.get())                       # accepts the degree of filtering
        if(degree%2==0):                            # since only odd numbers are permitted by filtering function
            degree = degree+1                       # check is done and changes are made accordingly
        median_filt = cv2.medianBlur(img,degree)    # inbuilt function of OpenCV
        return median_filt                          # returns the variable with 'filtered' pixel data
    except: 
        messagebox.showerror("Error","File not found. Possibilities: File not loaded, negative kernel size or non-integral value") # else, error
        return


def preview_median_img():                           # function to preview filtered image
    try:
        median_filt=median()                        # median() is called
        cv2.imshow("Preview Median-Filtered Image",median_filt) # displays image in a new window
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        messagebox.showerror("Error","File not found.") # else, error
        return


def save_median_img():          # function to save the newly generated image in a different file
    try:    
        # this line opens up the usual 'Save as' dialog box in Windows, for the user 
        # to chhose a directory and  name the file . For now, we accept JPG and PNG files only

        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save image file",filetypes=(("JPG Image",".*jpg"),("PNG Image",".*png"),("JPEG Image",".*jpeg")))
        median_filt=median()            # median() is called
        cv2.imwrite(fln,median_filt)    # 'filtered' image is written in the file path specified by user

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

    # button to view the image before filtering is done
    btn2=Button(wrapper,text="Preview",command=previewimg,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    btn2.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(btn2, "#ff910c", "#e2c0b3")


    # this section is for taking input and filtering
    #
    #
    wrapper2=LabelFrame(root,text="Median Filtering",bg="#a4b3da")
    wrapper2.pack(fill='both',expand='yes',padx=20,pady=20)

    # label
    lbl4=Label(wrapper2,text='Enter Kernel size',bg="#a4b3da")
    lbl4.pack(side=tk.LEFT,padx=10,pady=10) 

    # text box to accept the degree of filtering
    ent4=Entry(wrapper2,textvariable=deg)
    ent4.pack(side=tk.LEFT,padx=10,pady=10)

    # button to implement median filtering
    btn3=Button(wrapper2,text="Apply Median Filtering",command=median,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    btn3.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(btn3, "#ff910c", "#e2c0b3")


    # this section is for viewing result and saving
    #
    #
    wrapper3=LabelFrame(root,text="Actions",bg="#819dc7")
    wrapper3.pack(fill='both',expand='yes',padx=20,pady=20)

    # button to view the filtered image before saving
    prvbtn=Button(wrapper3,text="Preview",command=preview_median_img,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    prvbtn.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(prvbtn, "#ff910c", "#e2c0b3")

    # button to save the filtered image
    savebtn=Button(wrapper3,text="Save",command=save_median_img,bg="#e2c0b3",activebackground='#ff910c',activeforeground='white',relief=RAISED,cursor="circle")
    savebtn.pack(side=tk.LEFT,padx=10,pady=10)
    changeOnHover(savebtn, "#ff910c", "#e2c0b3")


    root.title("Median Filtering")      # title of window
    root.geometry("500x400")            # size of window
    root.mainloop()                     # keeps the window and its functionalities
                                        # until it is closed

# actual main function
if __name__=="__main__":
    main()