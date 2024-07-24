import qrcode
import image
import random
from tkinter import *
import string
window = Tk()
window.config(background="red")
window.title("QRCode Generator")
def Generator():
    qr = qrcode.QRCode(
        version = 15,
        box_size =10,
        border = 5
    )

    data = entry.get()
    
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill = "black", back_color = "white")
    save = ""
    Name_source = string.ascii_letters + string.ascii_uppercase + string.ascii_lowercase

    for x in range(5):
        save += random.choice(Name_source)
    print(f"saved name is: {save}")
    img.save(f"{save}.png")
    
def clear():
    entry.delete(0, END)
    
label = Label(window,
              text="Enter the link you want the QRCode to be generated from in the field below:",
              fg="#000",
              bg="red")
entry = Entry(window, 
              fg="#000",
              bg="grey")
submit = Button(window,
                bg="#000",
                fg="red",
                text= "Submit",
                command=Generator)
clearBt = Button(window,
               text ="Clear",
               command=clear,
               bg="red",
               fg="#000")

label.pack()
entry.pack()
submit.pack()
clearBt.pack()
window.mainloop()