from msilib.schema import File
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1360x800+0+0")

        #========= BG IMAGE ============#
        self.bg=ImageTk.PhotoImage(file=r"F:\3. Hostel Management\Images\MECLogo.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        
        # ========== FRAME ===========#
        frame=Frame(self.root,bg="white")
        frame.place(relx=0.5,rely=0.5, anchor=CENTER, width=340,height=450)

        img1=Image.open(r"F:\3. Hostel Management\Images\Login.png")
        img1=img1.resize((100,100), Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.img1,bg="white", borderwidth=0)
        lblimg1.place(relx=0.45,rely=0.25)

        text1=Label(frame,text="Get Started", font=("Times New Roman",20,"bold"), fg="Black", bg="White")
        text1.place(relx=0.3,rely=0.3)






if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()
