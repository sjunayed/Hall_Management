import sys
from tkinter import*
from tkinter import messagebox

from setuptools import Command
from hall import hall
from tkinter import ttk

class login:
    def __init__(self, root):
        self.root = root
        self.root.title("LogIn System")
        self.root.geometry("800x650+300+50")
        self.root.resizable(False, False)

        # ======= Login Frame ============#
        f_Login = Frame(self.root, bg="white")
        f_Login.place(x=160, y=100, height=430, width=500)

        #========= Title & Subtitle -==========#
        title=Label(f_Login, text="Login Here", font=("impact", 35, "bold"), fg="#6162FF", bg="white").place(x=90, y=30)
        subtitle=Label(f_Login, text="Members Login Area", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=90, y=90)

        #========== UserName ============#
        lbl_user=Label(f_Login, text="Username", font=("Goudy old style", 15, "bold"), fg="Grey", bg="white").place(x=90, y=140)
        self.username=ttk.Entry(f_Login, font=("Goudy old style", 15))
        self.username.place(x=90, y=180, width=320, height=35)
        
         #========== Password ==========#
        lbl_password=Label(f_Login, text="Password", font=("Goudy old style", 15, "bold"), fg="Grey", bg="white").place(x=90, y=220)
        self.password=ttk.Entry(f_Login, show="*", font=("Goudy old style", 15))
        self.password.place(x=90, y=260, width=320, height=35)
        
        #========== Show Password =========#
        cb=IntVar(value=0)
        def my_show():
            if(cb.get()==1):
                self.password.config(show="")
            else:
                self.password.config(show="*")
        check_box=ttk.Checkbutton(f_Login, text="Show Password", variable=cb, onvalue=1, offvalue=0, command=my_show)
        check_box.place(x=90,y=300)



        #======== Button =========#
        #forget = Button(f_Login, text="Forget Password?", cursor="hand2", bd=0, font=("Goudy old style", 12), fg="#6162FF", bg="white").place(x=90, y=300)
        submit = Button(f_Login, command=self.check_function, text="LogIn", cursor="hand2", bd=0, font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=90, y=340, width=180, height=40)

    #========== UserName and Password ==========#
    def check_function(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.username.get()!="Admin" or self.password.get()!="123456":
            messagebox.showerror("Error", "Invalid UserName or Password", parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")
            self.new_win=Toplevel(self.root)
            self.app=hall(self.new_win)
            


    


if __name__ == "__main__":
    root=Tk()
    obj=login(root)
    root.mainloop()


