from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Face_Recognition_System:
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

        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font = ("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=130)

        img5=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI2.jpeg")
        # to set image size
        img5=img5.resize((220,220))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 =Button(bg_img,image=self.photoimg5,cursor = "hand2")
        b1.place(x=200,y=100,width = 220,height=220)
        title_lbl1 = Button(bg_img,text="STUDENT DETAILS",font = ("times new roman",10,"bold"),bg="darkblue",fg="red",cursor="hand2")
        title_lbl1.place(x=200,y=300,width=220,height=40)
# detect face
        img6=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI2.jpeg")
        # to set image size
        img6=img6.resize((220,220))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 =Button(bg_img,image=self.photoimg6,cursor = "hand2")
        b1.place(x=500,y=100,width = 220,height=220)
        title_lbl2 = Button(bg_img,text="FACE RECOGNITION",font = ("times new roman",10,"bold"),bg="darkblue",fg="red",cursor="hand2")
        title_lbl2.place(x=500,y=300,width=220,height=40)
# attendence 
        img7=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI2.jpeg")
        # to set image size
        img7=img7.resize((220,220))
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 =Button(bg_img,image=self.photoimg7,cursor = "hand2")
        b1.place(x=800,y=100,width = 220,height=220)
        title_lbl3 = Button(bg_img,text="ATTENDANCE",font = ("times new roman",10,"bold"),bg="darkblue",fg="red",cursor="hand2")
        title_lbl3.place(x=800,y=300,width=220,height=40)
# help
        img8=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI2.jpeg")
        # to set image size
        img8=img8.resize((220,220))
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 =Button(bg_img,image=self.photoimg8,cursor = "hand2")
        b1.place(x=1100,y=100,width = 220,height=220)
        title_lbl4 = Button(bg_img,text="HELP",font = ("times new roman",10,"bold"),bg="darkblue",fg="red",cursor="hand2")
        title_lbl4.place(x=1100,y=300,width=220,height=40)
        # Train face
        img9=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI2.jpeg")
        # to set image size
        img9=img9.resize((220,220))
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1 =Button(bg_img,image=self.photoimg9,cursor = "hand2")
        b1.place(x=200,y=400,width = 220,height=220)
        title_lbl5 = Button(bg_img,text="TRAIN DATA",font = ("times new roman",10,"bold"),bg="darkblue",fg="red",cursor="hand2")
        title_lbl5.place(x=200,y=600,width=220,height=40)
        # photos face
        img10=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI2.jpeg")
        # to set image size
        img10=img10.resize((220,220))
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 =Button(bg_img,image=self.photoimg10,cursor = "hand2")
        b1.place(x=500,y=400,width = 220,height=220)
        title_lbl6 = Button(bg_img,text="PHOTOS",font = ("times new roman",10,"bold"),bg="lightblue",fg="red",cursor="hand2")
        title_lbl6.place(x=500,y=600,width=220,height=40)
        # developer 
        img11=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI2.jpeg")
        # to set image size
        img11=img11.resize((220,220))
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b1 =Button(bg_img,image=self.photoimg11,cursor = "hand2")
        b1.place(x=800,y=400,width = 220,height=220)
        title_lbl7 = Button(bg_img,text="DEVELOPER",font = ("times new roman",10,"bold"),bg="lightblue",fg="red",cursor="hand2")
        title_lbl7.place(x=800,y=600,width=220,height=40)
        # Exit face
        img12=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI2.jpeg")
        # to set image size
        img12=img12.resize((220,220))
        self.photoimg12 = ImageTk.PhotoImage(img12)
        b1 =Button(bg_img,image=self.photoimg10,cursor = "hand2")
        b1.place(x=1100,y=400,width = 220,height=220)
        title_lbl7 = Button(bg_img,text="EXIT",font = ("times new roman",10,"bold"),bg="darkblue",fg="LIGHTBLUE",cursor="hand2")
        title_lbl7.place(x=1100,y=600,width=220,height=40)
# to call main
if __name__ =="__main__":
    # to call root from toolkit
    root =Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()