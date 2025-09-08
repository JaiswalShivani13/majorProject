from tkinter import Tk, Label, Button, Toplevel
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import Developer
from help import Help


class AttendenceUsingFaceRecogination:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1430x790+0+0")
        self.root.title("Attendance using Face Recognition")

        # First image
        img = Image.open(r"college_images\bg.jpg")
        img = img.resize((1430, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1430, height=130)

        # Background image
        img3 = Image.open(r"college_images\bg_img.jpg")
        img3 = img3.resize((1500, 780), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1500, height=780)

        title_lbl = Label(bg_img, text="Attendance Using Face Recognition", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=55)

        # Function buttons
        # Student Details Button
        img4 = Image.open(r"college_images\studentsss.jpg")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b_student = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b_student.place(x=200, y=100, width=220, height=220)

        b_student_lbl = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b_student_lbl.place(x=200, y=300, width=220, height=40)

        # Face Detector Button
        img5 = Image.open(r"college_images\face_detector1.jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b_face_detector = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b_face_detector.place(x=500, y=100, width=220, height=220)

        b_face_detector_lbl = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b_face_detector_lbl.place(x=500, y=300, width=220, height=40)

        # Attendance Button
        img6 = Image.open(r"college_images\AdobeStock_303989091.jpeg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b_attendance = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendence_data)
        b_attendance.place(x=800, y=100, width=220, height=220)

        b_attendance_lbl = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendence_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b_attendance_lbl.place(x=800, y=300, width=220, height=40)

        # Help Desk Button
        img7 = Image.open(r"college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b_help = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.help_data)
        b_help.place(x=1100, y=100, width=220, height=220)

        b_help_lbl = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b_help_lbl.place(x=1100, y=300, width=220, height=40)

        # Train Button
        img8 = Image.open(r"college_images\Train.jpg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b_train = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b_train.place(x=200, y=400, width=220, height=220)

        b_train_lbl = Button(bg_img, text="Train", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b_train_lbl.place(x=200, y=620, width=220, height=40)

        # Photo Button
        img9 = Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b_photo = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b_photo.place(x=500, y=400, width=220, height=220)

        b_photo_lbl = Button(bg_img, text="Photo", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b_photo_lbl.place(x=500, y=620, width=220, height=40)

        # Developer Button
        img10 = Image.open(r"college_images\developer.jpg")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b_developer = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.developer_data)
        b_developer.place(x=800, y=400, width=220, height=220)

        b_developer_lbl = Button(bg_img, text="Developer", cursor="hand2",command=self.developer_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b_developer_lbl.place(x=800, y=620, width=220, height=40)

        # Exit Button
        img11 = Image.open(r"college_images\exit.jpg")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b_exit = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iexit)
        b_exit.place(x=1100, y=400, width=220, height=220)

        b_exit_lbl = Button(bg_img, text="Exit", cursor="hand2",command=self.iexit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b_exit_lbl.place(x=1100, y=620, width=220, height=40)

    def open_img(self):
        os.startfile("data")


    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iexit >0:
            self.root.destroy()
        else:
            return

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendence_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendence(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = AttendenceUsingFaceRecogination(root)
    root.mainloop()
