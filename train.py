from tkinter import Button, Tk, Label, Frame, RIDGE, LabelFrame,ttk,W,Entry
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1430x790+0+0")
        self.root.title("Attendance using Face Recognition")


        title_lbl = Label(self.root, text="TRAIN DATASET", font=("times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1450, height=55)

        img_top = Image.open(r"college_images\facialrecognition.png")
        img_top = img_top.resize((1450, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Add image to Left_frame
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1450, height=325)
        # Button
        b_student_lbl = Button(self.root, text="TRAIN DATA",command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="darkblue", fg="white")
        b_student_lbl.place(x=0, y=380, width=1450, height=60)

        img_bottom = Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img_bottom = img_bottom.resize((1450, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        # Add image to Left_frame
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1450, height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]    

        faces=[]
        ids=[]

        for image in path:
          img=Image.open(image).convert('L')   #Gray scale img  
          imageNp=np.array(img,'uint8')
          _id=int(os.path.split(image)[1].split('.')[1])
          
          faces.append(imageNp)
          ids.append(_id)
          cv2.imshow("Training",imageNp)
          cv2.waitKey(1)==13
        ids=np.array(ids)

        # ===========train classifier and save=======
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed..") 


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()