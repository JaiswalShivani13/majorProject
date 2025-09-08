from tkinter import Button, Tk, Label, Frame, RIDGE, LabelFrame, ttk, W, Entry
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import os
import numpy as np
import csv

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1430x790+0+0")
        self.root.title("Attendance using Face Recognition")

        self.marked_ids = set()  # Initializing the set to store marked attendance

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1450, height=55)

        img_top = Image.open(r"college_images\face_detector1.jpg")
        img_top = img_top.resize((650, 800), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Add image to Left_frame
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=800)

        img_bottom = Image.open(r"college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom = img_bottom.resize((950, 800), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        # Add image to Left_frame
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=800)

        b_student_lbl = Button(f_lbl, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 15, "bold"), bg="red", fg="white")
        b_student_lbl.place(x=370, y=700, width=200, height=40)

    # ================Attendance Function=======
    def mark_attendence(self, i, r, n, d):
        with open("shivani.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    # ==========Face Recognition=========
    def face_recog(self):
        self.marked_ids = set()  # Reset the marked_ids set at the start of each new session
        
        def draw_boundray(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                _id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Shivani@123", database="face_recogination")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id=" + str(_id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Roll from student where Student_id=" + str(_id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Dep from student where Student_id=" + str(_id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select Student_id from student where Student_id=" + str(_id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                if confidence > 70:
                    cv2.putText(img, f"ID::{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll::{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name::{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department::{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    if _id not in self.marked_ids:
                        self.mark_attendence(i, r, n, d)
                        self.marked_ids.add(_id)
                        cv2.putText(img, "Attendance Marked", (x, y + h + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
                    else:
                        cv2.putText(img, "Already Marked", (x, y + h + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 0), 2)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascard = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascard)
            cv2.imshow("Welcome to Face Recognition", img)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 13 or key == 27:  # Stop if 'q', 'Enter', or 'Esc' is pressed
                break
        video_cap.release()
        cv2.destroyAllWindows()
        cv2.waitKey(1)

    # Show Attendance Function
    def show_attendance(self):
        top = Toplevel(self.root)
        top.title("Attendance Sheet")
        top.geometry("900x500")

        # Table frame
        table_frame = Frame(top, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=10, width=880, height=480)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_table = ttk.Treeview(table_frame,
                                             columns=("id", "roll", "name", "dep", "time", "date", "status"),
                                             xscrollcommand=scroll_x.set,
                                             yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("id", text="Student ID")
        self.attendance_table.heading("roll", text="Roll No")
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("dep", text="Department")
        self.attendance_table.heading("time", text="Time")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("status", text="Status")
        self.attendance_table["show"] = "headings"

        self.attendance_table.column("id", width=100)
        self.attendance_table.column("roll", width=100)
        self.attendance_table.column("name", width=100)
        self.attendance_table.column("dep", width=100)
        self.attendance_table.column("time", width=100)
        self.attendance_table.column("date", width=100)
        self.attendance_table.column("status", width=100)

        self.attendance_table.pack(fill=BOTH, expand=1)

        # Load CSV data
        self.fetch_csv_data("shivani.csv")

    def fetch_csv_data(self, file_path):
        with open(file_path) as f:
            reader = csv.reader(f)
            next(reader)  # Skip header if any
            self.attendance_table.delete(*self.attendance_table.get_children())
            for row in reader:
                self.attendance_table.insert("", END, values=row)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

