from tkinter import*
from PIL import Image, ImageTk
from student import student_win
from details import RoomBooking


class hall:
    def __init__(self,root):
        self.root = root
        self.root.title("Hall Management System")
        self.root.geometry("1366x768+0+0")

        #======== Upper Image ======= #
        #img1=Image.open(r"Images\Front.jpg")
        #img1=img1.resize((1366,300), Image.ANTIALIAS)
        #self.photoimg1=ImageTk.PhotoImage(img1)

        #lblimg1=Label(self.root, image=self.photoimg1,bd=4,relief=RIDGE)
        #lblimg1.place(x=0,y=0, width=1366, height=140)

        #========== Title =========#
        title=Label(self.root, text="Hall Management System", font=("Times New Roman", 30, "bold"), bg="Black", fg="#6162FF", bd=4, relief=RIDGE)
        title.place(x=0,y=0, width=1366, height=60)

        #========= Main Frame ==========#
        mframe=Frame(self.root, bd=4, relief=RIDGE, bg="#b2beb5")
        mframe.place(x=0, y=60, width=1366, height=680)
        
        #======== Logo =========#
        img2=Image.open(r"Images\MECLogo.jpg")
        img2=img2.resize((230,170), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(mframe, image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=0, width=230, height=180)

        #=========== Menu ========#
        menu=Label(mframe, text="Menu", font=("Times New Roman", 20, "bold"), bg="Black", fg="#6162FF", bd=4, relief=RIDGE)
        menu.place(x=0,y=180, width=230)

        #========= Button Frame ==========#
        buttonframe=Frame(mframe, bd=4, relief=RIDGE)
        buttonframe.place(x=0, y=220, width=228, height=118)

        student=Button(buttonframe, text="ADD STUDENT", command=self.student ,cursor="hand2", font=("Times New Roman", 14, "bold"), bg="Black", fg="#6162FF", bd=0, width=22)
        student.grid(row=0,column=0, pady=1)

        #checkout=Button(buttonframe, text="CHECKOUT",cursor="hand2", font=("Times New Roman", 14, "bold"), bg="Black", fg="#6162FF", bd=0, width=22)
        #checkout.grid(row=1,column=0, pady=1)

        fees=Button(buttonframe, text="FEES", command=self.fees, cursor="hand2", font=("Times New Roman", 14, "bold"), bg="Black", fg="#6162FF", bd=0, width=22)
        fees.grid(row=2,column=0, pady=1)

        #search=Button(buttonframe, text="SEARCH",cursor="hand2", font=("Times New Roman", 14, "bold"), bg="Black", fg="#6162FF", bd=0, width=22)
        #search.grid(row=3,column=0, pady=1)

        logout=Button(buttonframe, text="Log Out", command=self.logout,cursor="hand2", font=("Times New Roman", 14, "bold"), bg="Black", fg="#6162FF", bd=0, width=22)
        logout.grid(row=4,column=0, pady=1)

        #======= Right Side Image ===========#
        img3=Image.open(r"Images\Muktijoddha.jpg")
        img3=img3.resize((1130,670), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg3=Label(mframe, image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg3.place(x=228,y=0, width=1130, height=670)


    
    
    #========= Button Function ==========#
    def student(self):
        self.new_win=Toplevel(self.root)
        self.app=student_win(self.new_win)
    
    #========= Button Function ==========#
    def fees(self):
        self.new_win=Toplevel(self.root)
        self.app=RoomBooking(self.new_win)
    
    #========= Logout ==========#
    def logout(self):
        self.root.destroy()




if __name__ == "__main__":
    root=Tk()
    obj=hall(root)
    root.mainloop()