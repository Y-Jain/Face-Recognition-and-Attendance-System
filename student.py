
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Student:
    def __init__(self,root):
        self.root = root 
        # initialize root
        # to set geometry
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI1.jpeg")
        # to set image size
        img1=img1.resize((500,430))
        # ANTIALIAS = to convert high level image to low level image
        # to store img in variable
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_lable1 = Label(self.root,image = self.photoimg1)
        first_lable1.place(x=0,y=0,width=550,height=130)
        
        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI2.jpeg")
        # to set image size
        img2=img2.resize((500,130))
        # ANTIALIAS = to convert high level image to low level image
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_lable2 = Label(self.root,image = self.photoimg2)
        first_lable2.place(x=500,y=0,width=550,height=130)

        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI3.jpeg")
        # to set image size
        img3=img3.resize((500,130))
        # ANTIALIAS = to convert high level image to low level image
        self.photoimg3 = ImageTk.PhotoImage(img3)

        first_lable3 = Label(self.root,image = self.photoimg3)
        first_lable3.place(x=1000,y=0,width=550,height=130)

        img4=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI7.jpg")
        # to set image size
        img4=img4.resize((1530,710))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image= self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font = ("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=100)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=70,width=1510,height=600)    

        # left Lable frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\student1.png")
        img_left=img_left.resize((720,150))
        self.photoimg_left =ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        # Current course information
        ccf=LabelFrame(Left_frame,bd=2,bg="white",relief = RIDGE,text="Current Course Information",font=("times new roman",15,"bold"),fg="darkgreen")
        ccf.place(x=5,y=135,width=720,height=120)

        d_lable=Label(ccf,text="Department",font=("times new roman",12,"bold"),fg="darkgreen")
        d_lable.grid(row=0,column=0,padx=10)

        d_combo=ttk.Combobox(ccf,font=("times new roman",12,"bold"),state="readonly")
        d_combo["values"]=("Select Department","Computer","IT","Civil","Mechnical")
        # current position
        d_combo.current(0)
        d_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course
        C_lable=Label(ccf,text="Course",font=("times new roman",12,"bold"),fg="darkgreen")
        C_lable.grid(row=0,column=2,padx=10)

        C_combo=ttk.Combobox(ccf,font=("times new roman",12,"bold"),state="readonly")
        C_combo["values"]=("Select Courses","FSDB","DS","BE","SE")
        # current position
        C_combo.current(0)
        C_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        y_lable=Label(ccf,text="Year",font=("times new roman",12,"bold"),fg="darkgreen")
        y_lable.grid(row=1,column=0,padx=10)

        y_combo=ttk.Combobox(ccf,font=("times new roman",12,"bold"),state="readonly")
        y_combo["values"]=("Select Year","1","2","3","4")
        # current position
        y_combo.current(0)
        y_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        s_lable=Label(ccf,text="Semester",font=("times new roman",12,"bold"),fg="darkgreen")
        s_lable.grid(row=1,column=2,padx=10)

        s_combo=ttk.Combobox(ccf,font=("times new roman",12,"bold"),state="readonly",width=15)
        s_combo["values"]=("Select Semester",1,2,3,4,5,6,7,8)
        # current position
        s_combo.current(0)
        s_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Student Information
        ccf=LabelFrame(Left_frame,bd=2,bg="white",relief = RIDGE,text="Student Information",font=("times new roman",15,"bold"),fg="darkgreen")
        ccf.place(x=5,y=250,width=720,height=300)

        # sid_lable=Label(ccf,text="StudentID",font=("times new roman",12,"bold"),fg="darkgreen")
        # sid_lable.grid(row=1,column=2,padx=10,sticky=W)

        # student id
        studentID_label = Label(ccf,text="StudentID: ",font=("times new roman",12,"bold"))
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(ccf,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # student Name
        studentName_label = Label(ccf,text="Student Name: ",font=("times new roman",12,"bold"))
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(ccf,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # class division
        class_div_label = Label(ccf,text="Class Division: ",font=("times new roman",12,"bold"))
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(ccf,width=20,font=("times new roman",12,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Roll no.
        studentRoll_label = Label(ccf,text="Roll no.: ",font=("times new roman",12,"bold"))
        studentRoll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentRoll_entry=ttk.Entry(ccf,width=20,font=("times new roman",12,"bold"))
        studentRoll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
        gender_label = Label(ccf,text="Gender: ",font=("times new roman",12,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(ccf,width=20,font=("times new roman",12,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # DOB
        dob_label = Label(ccf,text="DOB: ",font=("times new roman",12,"bold"))
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(ccf,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email
        email_label = Label(ccf,text="Email: ",font=("times new roman",12,"bold"))
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(ccf,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Phone number
        phone_label = Label(ccf,text="Phone No.: ",font=("times new roman",12,"bold"))
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(ccf,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address
        address_label = Label(ccf,text="Address: ",font=("times new roman",12,"bold"))
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(ccf,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teacher name
        teacher_label = Label(ccf,text="Teacher Name: ",font=("times new roman",12,"bold"))
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(ccf,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # radio button
        radiobtn1=ttk.Radiobutton(ccf,text="Take photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(ccf,text="No photo Sample",value="Yes")
        radiobtn2.grid(row=6,column=1)

        # buttons frame
        btn_frame=Frame(ccf,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=715,height=37)

        # save button
        save_btn=Button(btn_frame,text="Save",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        # take_photo_btn=Button(btn_frame,text="Save",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        # take_photo_btn.grid(row=1,column=0)

        # update_photo_btn=Button(btn_frame,text="Save",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        # update_photo_btn.grid(row=1,column=1)

        btn_frame1=Frame(ccf,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=240,width=715,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)

    # Right Lable frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        Right_frame.place(x=750,y=10,width=800,height=580)

        img_right=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\student3.jpg")
        img_right=img_right.resize((720,130))
        self.photoimg_right =ImageTk.PhotoImage(img_right)

        f_lbl1=Label(Right_frame,image=self.photoimg_right)
        f_lbl1.place(x=5,y=0,width=720,height=130)

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief = RIDGE,text="Search System",font=("times new roman",15,"bold"),fg="darkgreen")
        Search_frame.place(x=5,y=135,width=710,height=70)

        search_label = Label(Search_frame,text="Search By: ",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_lable=Label(Search_frame,text="Semester",font=("times new roman",12,"bold"),fg="darkgreen")
        search_lable.grid(row=1,column=2,padx=10)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        Search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        showAll_btn=Button(Search_frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=2,pady=10,sticky=W)

        # Table Frame
        Table_frame=Frame(Right_frame,bd=2,bg="white",relief = RIDGE)
        Table_frame.place(x=5,y=210,width=710,height=250)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone_no.","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        # To pack scroll bar
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # to show header
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone_no.",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)

        # To set column width
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone_no.",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
# to call main
if __name__ =="__main__":
    # to call root from toolkit
    root =Tk()
    obj = Student(root)
    root.mainloop()