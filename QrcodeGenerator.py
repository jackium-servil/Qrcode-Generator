import qrcode
import image
import random
from tkinter import *
import string
import os

window = Tk()
window.config(background="red")
window.title("QRCode Generator")

def Generator():
    os.system("clear")
    qr = qrcode.QRCode(
        version = 15,
        box_size =10,
        border = 5
    )

    data = entry.get()
    
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill = "black", back_color = "pink", front_color="green")
    source = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase
    save = ""
    file_name = entry2.get()
    file_name2 = bool(file_name)
    
    if file_name2 == False:
        for x in range(5):
            save += random.choice(source)
        img.save(f"{save}.png")
        print(f"QRCode for : {data} is successfully createred\n\tAnd it is saved as {save}.png")
    
    else:
        img.save(f"{file_name}.png")
        print(f"QRCode for : {data} is successfully createred\n\tAnd it is saved as {file_name}.png")

def clear():
    entry.delete(0, END)
    entry2.delete(0, END)
    
label = Label(window,
              text="Enter the link you want the QRCode to be generated from in the field below:",
              fg="red",
              bg="#000")
label2 = Label(window,
              fg="green",
              bg="#000",
              text="Input the file name (Optional the computer can generate for you)")
entry = Entry(window, 
              fg="blue",
              bg="grey")
entry2 = Entry(window,
               fg="green",
               bg="grey")
submit = Button(window,
                bg="#000",
                fg="red",
                text= "Submit",
                command=Generator)
clearBt = Button(window,
               text ="Clear",
               command=clear,
               bg="#000",
               fg="red")

label.pack()
entry.pack()
label2.pack()
entry2.pack()
submit.pack()
clearBt.pack()
window.mainloop()