from tkinter import Toplevel,Button
from PIL import Image,ImageTk


def open_window(parent , pla):
    
    child = Toplevel(parent)
    child.title("Hmmmm ")
    image = Image.open("C:\\Users\\ryzen\\OneDrive\\Desktop\\Music_Player\\images.png")
    photo = ImageTk.PhotoImage(image)
    pause_btn = Button(child,image= photo, command= pla.pause_)
    pause_btn.image = photo
    pause_btn.pack(pady=50)

