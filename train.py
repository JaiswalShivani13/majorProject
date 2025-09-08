from tkinter import Button, Tk, Label
from PIL import Image, ImageTk
from tkinter import messagebox
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

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1450, height=325)

        # 🔹 "CAPTURE FACES" Button
        b_capture_lbl = Button(self.root, text="CAPTURE FACES", command=self.capture_faces, cursor="hand2",
                               font=("times new roman", 30, "bold"), bg="darkred", fg="white")
        b_capture_lbl.place(x=0, y=380, width=1450, height=60)

        # 🔹 "TRAIN DATA" Button
        b_train_lbl = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
                             font=("times new roman", 30, "bold"), bg="darkblue", fg="white")
        b_train_lbl.place(x=0, y=450, width=1450, height=60)

        img_bottom = Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img_bottom = img_bottom.resize((1450, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=510, width=1450, height=325)

    def capture_faces(self):
        import cv2
        import os
        from tkinter import simpledialog

        cam = cv2.VideoCapture(0)
        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        student_id = simpledialog.askstring("Input", "Enter Student ID:")
        name = simpledialog.askstring("Input", "Enter Student Name:")

        if not student_id or not name:
            return  # Exit if no input

        # Create data folder if it doesn't exist
        if not os.path.exists('data'):
            os.makedirs('data')

        img_id = 0

        def face_cropped(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                face = img[y:y+h, x:x+w]
                return face

        while True:
            ret, frame = cam.read()
            if face_cropped(frame) is not None:
                img_id += 1
                face = cv2.resize(face_cropped(frame), (450, 450))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                file_name_path = f"data/User.{student_id}.{img_id}.jpg"
                cv2.imwrite(file_name_path, face)

                cv2.putText(face, f"Image {img_id}/100", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                cv2.imshow("Capturing Faces", face)

            if cv2.waitKey(1) == 13 or img_id == 100:
                break

        cam.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Face Data Captured Successfully.")

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image_path in path:
            if os.path.isfile(image_path):
                try:
                    img = Image.open(image_path).convert('L')
                    imageNp = np.array(img, 'uint8')
                    _id = int(os.path.split(image_path)[1].split('.')[1])

                    faces.append(imageNp)
                    ids.append(_id)
                    cv2.imshow("Training", imageNp)
                    cv2.waitKey(1)
                except Exception as e:
                    print(f"Skipping file {image_path}: {e}")

        if faces:
            ids = np.array(ids)
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training dataset completed.")
        else:
            messagebox.showerror("Error", "No valid face data found to train.")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
