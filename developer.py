from tkinter import Tk, Label, Frame, RIDGE, LabelFrame,ttk,W,Entry
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1430x790+0+0")
        self.root.title("Attendance using Face Recognition")

        title_lbl = Label(self.root, text="DEVELOPER", font=("Times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1450, height=55)

        img_top = Image.open(r"college_images\dev.jpg")
        img_top = img_top.resize((1450, 800), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Add image to Left_frame
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1450, height=800)

        # frame 
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=900, y=0, width=500, height=650)

        img_top1= Image.open(r"college_images\tony.jpg")
        img_top1= img_top1.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        # Add image to Left_frame
        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=0, width=200, height=200)
        # Developer info 
        dev_lbl = Label(main_frame, text="Hello! we are developer", font=("times new roman", 19, "bold"), bg="white", fg="black")
        dev_lbl.place(x=0, y=5)

        dev_lbl = Label(main_frame, text="This is my finall year project", font=("times new roman", 19, "bold"), bg="white", fg="black")
        dev_lbl.place(x=0, y=40)

        img_top2 = Image.open(r"college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img_top2 = img_top2.resize((500, 450), Image.Resampling.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)

        # Add image to Left_frame
        f_lbl = Label(main_frame, image=self.photoimg_top2)
        f_lbl.place(x=0, y=210, width=500, height=450)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()