from tkinter import Tk, Label, Frame, RIDGE, LabelFrame,ttk,W,Entry
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1430x790+0+0")
        self.root.title("Attendance using Face Recognition")

        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1450, height=55)

        img_top = Image.open(r"college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top = img_top.resize((1450, 800), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Add image to Left_frame
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1450, height=800)

        dev_lbl = Label(f_lbl, text="Email: imshivanisj@gmail.com", font=("times new roman", 19, "bold"), bg="white", fg="darkblue")
        dev_lbl.place(x=530, y=150)

        dev_lbl = Label(f_lbl, text="Email: guptashubhangi218@gmail.com", font=("times new roman", 19, "bold"), bg="white", fg="darkblue")
        dev_lbl.place(x=530, y=200)

        dev_lbl = Label(f_lbl, text="Email: ankitayad2505@gmail.com", font=("times new roman", 19, "bold"), bg="white", fg="darkblue")
        dev_lbl.place(x=530, y=250)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()