from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



mydata=[]
class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1430x790+0+0")
        self.root.title("Attendance using Face Recognition")

        # ============ Variables ==============
        
        self.var_atten_id = StringVar(self.root)
        self.var_attend_roll = StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_dep = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_attendence = StringVar()



        img = Image.open(r"college_images\smart-attendance.jpg")
        img = img.resize((1500, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1500, height=200)

        img2 = Image.open(r"college_images\bg_img.jpg")
        img2 = img2.resize((1500, 780), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=200, width=1500, height=780)
        
        title_lbl = Label(bg_img, text="STUDENT ATTENDANCE", font=("Times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1530, height=55)

         # Main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=60, width=1410, height=600)

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("Times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=700, height=570)

        # Load image for Left_frame
        img_left = Image.open(r"college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((690, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        # Add image to Left_frame
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=690, height=130)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=690, height=400)

        # labels and entry 

        # Attendence id 
        attendenceID_label=Label(left_inside_frame,text="AttendencdeID:",font=("Times new roman", 12, "bold"),bg="white")
        attendenceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendenceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("Times new roman",13,"bold"))
        attendenceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
# lable 
        roll_label=Label(left_inside_frame,text="Roll:",font=("times new roman", 12, "bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_roll,font=("times new roman",13,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,pady=8,sticky=W)

        name_label=Label(left_inside_frame,text="Name:",font=("times new roman", 12, "bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_name,font=("times new roman",13,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=8,sticky=W)

        department_label=Label(left_inside_frame,text="Department:",font=("times new roman", 12, "bold"),bg="white")
        department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        department_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_dep,font=("times new roman",13,"bold"))
        department_entry.grid(row=1,column=3,padx=10,pady=8,sticky=W)

        time_label=Label(left_inside_frame,text="Time:",font=("times new roman", 12, "bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_time,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=8,sticky=W)

        date_label=Label(left_inside_frame,text="Date:",font=("times new roman", 12, "bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_date,font=("times new roman",13,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=8,sticky=W)

        attendence_label=Label(left_inside_frame,text="Attendencde Status:",font=("times new roman", 12, "bold"),bg="white")
        attendence_label.grid(row=3,column=0)

        self.atten_combo=ttk.Combobox(left_inside_frame,font=("times new roman", 13, "bold"),width=18,textvariable=self.var_attend_attendence,state="readonly")
        self.atten_combo["values"]=("Status","Present","Absent")
        self.atten_combo.current(0)
        self.atten_combo.grid(row=3,column=1,pady=8)

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=685,height=35)

        save_btn=Button(btn_frame,text="Import csv",command= self.importCSV,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCSV,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="update",width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=16,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)





        
        # Right Frame - Attendance Table
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=720, y=10, width=660, height=580)

        table_frame = Frame(right_frame, bd=2,relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=640, height=545)

         #  =====Scrollbar table=====
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="Attendence ID")
        self.AttendenceReportTable.heading("roll",text="Roll")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence")

        self.AttendenceReportTable["show"]="headings"
        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)

        # =================fetch data==========
    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)

    # ===========import csv=========
    def importCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename( initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread= csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # ==========export csv===========
    def exportCSV(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV As",
                filetypes=(("CSV File","*.csv"),("All File","*.*")),
                defaultextension=".csv",
                parent=self.root
            )
            with open(fln, mode="w", newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Expott","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendence.set(rows[6])

     # =======reset==============
    def  reset_data(self):
        self.var_atten_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendence.set("")





if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()

