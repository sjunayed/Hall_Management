from cgitb import text
from multiprocessing import parent_process
from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class student_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Add Student Details")
        self.root.geometry("1136x550+225+100")
        self.root.resizable(False, False)

        #============== Variables =============#
        self.var_roll=StringVar()
        self.var_dept=StringVar()
        self.var_stdnt_name=StringVar()
        self.var_fname=StringVar()
        self.var_mname=StringVar()
        self.var_address=StringVar()
        self.var_pcode=StringVar()
        self.var_email=StringVar()
        self.var_mobile=StringVar()
        self.var_idtype=StringVar()
        self.var_idnumber=StringVar()
        self.var_room=StringVar()

        #========== Title =========#
        title=Label(self.root, text="ADD STUDENT DETAILS", font=("Times New Roman", 18, "bold"), bg="Black", fg="#6162FF", bd=4, relief=RIDGE)
        title.place(x=0,y=0, width=1136, height=40)

        #======= Label Frame =========#
        lframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Student Details",font=("Times New Roman", 12, "bold"), padx=2)
        lframeleft.place(x=5, y=40, width=425, height=500)

        #============== Label and Entries =============#
        #--- Roll ---#
        roll=Label(lframeleft, font=("arial",12,"bold"), text="Roll Number: ", padx=2, pady=6)
        roll.grid(row=0, column=0, sticky=W)
        txtroll=ttk.Entry(lframeleft, textvariable=self.var_roll , font=("arial",13,"bold"), width=29)
        txtroll.grid(row=0, column=1)

        #--- Department ---#
        dept=Label(lframeleft, font=("arial",12,"bold"), text="Department: ", padx=2, pady=6)
        dept.grid(row=1, column=0, sticky=W)
        combodept=ttk.Combobox(lframeleft, textvariable=self.var_dept ,font=("arial", 13, "bold"), width=27, state="readonly")
        combodept["value"]=("CE", "CSE", "EEE")
        combodept.current(0)
        combodept.grid(row=1, column=1)

        #--- Name ---#
        sname=Label(lframeleft, font=("arial",12,"bold"), text="Student Name: ", padx=2, pady=6)
        sname.grid(row=2, column=0, sticky=W)
        txtsname=ttk.Entry(lframeleft, textvariable=self.var_stdnt_name ,font=("arial",13,"bold"), width=29)
        txtsname.grid(row=2, column=1)

        #--- Father Name ---#
        fname=Label(lframeleft, font=("arial",12,"bold"), text="Father Name: ", padx=2, pady=6)
        fname.grid(row=3, column=0, sticky=W)
        txtfname=ttk.Entry(lframeleft, textvariable=self.var_fname ,font=("arial",13,"bold"), width=29)
        txtfname.grid(row=3, column=1)

        #--- Mother Name ---#
        mname=Label(lframeleft, font=("arial",12,"bold"), text="Mother Name: ", padx=2, pady=6)
        mname.grid(row=4, column=0, sticky=W)
        txtmname=ttk.Entry(lframeleft, textvariable=self.var_mname ,font=("arial",13,"bold"), width=29)
        txtmname.grid(row=4, column=1)

        #--- Address ---#
        address=Label(lframeleft, font=("arial",12,"bold"), text="Address: ", padx=2, pady=6)
        address.grid(row=5, column=0, sticky=W)
        txtaddress=ttk.Entry(lframeleft, textvariable=self.var_address,font=("arial",13,"bold"), width=29)
        txtaddress.grid(row=5, column=1)

        #--- PostCode ---#
        pcode=Label(lframeleft, font=("arial",12,"bold"), text="Post Code: ", padx=2, pady=6)
        pcode.grid(row=6, column=0, sticky=W)
        txtpcode=ttk.Entry(lframeleft, textvariable=self.var_pcode,font=("arial",13,"bold"), width=29)
        txtpcode.grid(row=6, column=1)

        #--- Email ---#
        email=Label(lframeleft, font=("arial",12,"bold"), text="Email: ", padx=2, pady=6)
        email.grid(row=7, column=0, sticky=W)
        txtemail=ttk.Entry(lframeleft, textvariable=self.var_email,font=("arial",13,"bold"), width=29)
        txtemail.grid(row=7, column=1)

        #--- Phone Number ---#
        pnumber=Label(lframeleft, font=("arial",12,"bold"), text="Mobile Number: ", padx=2, pady=6)
        pnumber.grid(row=8, column=0, sticky=W)
        txtpnumber=ttk.Entry(lframeleft, textvariable=self.var_mobile,font=("arial",13,"bold"), width=29)
        txtpnumber.grid(row=8, column=1)

        #--- ID Proof Type ---#
        idtype=Label(lframeleft, font=("arial",12,"bold"), text="ID Proof Type: ", padx=2, pady=6)
        idtype.grid(row=9, column=0, sticky=W)
        comboidtype=ttk.Combobox(lframeleft, textvariable=self.var_idtype,font=("arial", 13, "bold"), width=27, state="readonly")
        comboidtype["value"]=("Birth Certificate", "NID", "Passport")
        comboidtype.current(0)
        comboidtype.grid(row=9, column=1)

        #--- Id Number ---#
        idnumber=Label(lframeleft, font=("arial",12,"bold"), text="ID Number: ", padx=2, pady=6)
        idnumber.grid(row=10, column=0, sticky=W)
        txtidnumber=ttk.Entry(lframeleft, textvariable=self.var_idnumber,font=("arial",13,"bold"), width=29)
        txtidnumber.grid(row=10, column=1)

        #--- Room Number ---#
        room=Label(lframeleft, font=("arial",12,"bold"), text="Room Number: ", padx=2, pady=6)
        room.grid(row=11, column=0, sticky=W)
        txtroom=ttk.Entry(lframeleft, textvariable=self.var_room,font=("arial",13,"bold"), width=29)
        txtroom.grid(row=11, column=1)

        #================ Buttons ==============#
        btnframe=Frame(lframeleft,bd=2,relief=RIDGE)
        btnframe.place(x=0, y=425, width=412, height=40)

        btnadd=Button(btnframe, text="ADD", command=self.add_stdnt, font=("arial",12,"bold"), bg="Black", fg="Gold", width=9)
        btnadd.grid(row=0,column=0, padx=1)

        btnupdate=Button(btnframe, text="Update", command=self.update, font=("arial",12,"bold"), bg="Black", fg="Gold", width=9)
        btnupdate.grid(row=0,column=1, padx=1)

        btndlt=Button(btnframe, text="Delete", command=self.dDelete, font=("arial",12,"bold"), bg="Black", fg="Gold", width=9)
        btndlt.grid(row=0,column=2, padx=1)

        btnrst=Button(btnframe, text="Reset", command=self.reset, font=("arial",12,"bold"), bg="Black", fg="Gold", width=9)
        btnrst.grid(row=0,column=3, padx=1)


        #=============== Table Frame Search =========================#
        tableframe=LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",font=("Times New Roman", 12, "bold"), padx=2)
        tableframe.place(x=435, y=40, width=690, height=500)

        lblsearchby=Label(tableframe, font=("arial",12,"bold"), text="Search By: ", bg="red", fg="white")
        lblsearchby.grid(row=0,column=0, padx=4)

        self.search_val=StringVar()
        combo_seach=ttk.Combobox(tableframe, textvariable=self.search_val, font=("arial", 13, "bold"), width=10, state="readonly")
        combo_seach["value"]=("Roll", "Mobile", "Room")
        combo_seach.current(0)
        combo_seach.grid(row=0, column=1, padx=4)
        
        self.txt_search=StringVar()
        txtsearch=ttk.Entry(tableframe, textvariable=self.txt_search, font=("arial",13,"bold"), width=24)
        txtsearch.grid(row=0, column=2, padx=4)

        btnsearch=Button(tableframe, text="Search", command=self.search, font=("arial",12,"bold"), bg="Black", fg="Gold", width=9)
        btnsearch.grid(row=0,column=3, padx=4)

        btnshowall=Button(tableframe, text="Show All", command=self.fetch_data, font=("arial",12,"bold"), bg="Black", fg="Gold", width=9)
        btnshowall.grid(row=0,column=4, padx=4)

         #=============== Show Data Table =================#
        dataframe=Frame(tableframe,bd=2,relief=RIDGE)
        dataframe.place(x=0,y=50,width=680, height=420)

        scroll_x=ttk.Scrollbar(dataframe, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(dataframe, orient=VERTICAL)

        self.Student_details=ttk.Treeview(dataframe, columns=("roll", "dept", "name", "fname", "mname", "address", "pcode", "email", "mobile", "idtype", "idnumber", "room"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_details.xview)
        scroll_y.config(command=self.Student_details.yview)

        self.Student_details.heading("roll", text="Roll Number")
        self.Student_details.heading("dept", text="Department")
        self.Student_details.heading("name", text="Student Name")
        self.Student_details.heading("fname", text="Fathers Name")
        self.Student_details.heading("mname", text="Mothers Name")
        self.Student_details.heading("address", text="Address")
        self.Student_details.heading("pcode", text="Post Code")
        self.Student_details.heading("email", text="Email")
        self.Student_details.heading("mobile", text="Mobile Number")
        self.Student_details.heading("idtype", text="Id Proof Type")
        self.Student_details.heading("idnumber", text="ID Number")
        self.Student_details.heading("room", text="Room Number")

        self.Student_details["show"]="headings"

        self.Student_details.column("roll", width=50)
        self.Student_details.column("dept", width=100)
        self.Student_details.column("name", width=200)
        self.Student_details.column("fname", width=200)
        self.Student_details.column("mname", width=200)
        self.Student_details.column("address", width=200)
        self.Student_details.column("pcode", width=100)
        self.Student_details.column("email", width=200)
        self.Student_details.column("mobile", width=100)
        self.Student_details.column("idtype", width=100)
        self.Student_details.column("idnumber", width=200)
        self.Student_details.column("room", width=100)

        self.Student_details.pack(fill=BOTH,expand=1)
        self.Student_details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    #=========== ADD ============#
    def add_stdnt(self):
        if self.var_mobile.get()=="" or self.var_idnumber.get()=="":
            messagebox.showerror("Error", "All Fields are Required!!!", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="root", database="hall_management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_roll.get(), self.var_dept.get(), self.var_stdnt_name.get(), self.var_fname.get(), self.var_mname.get(), self.var_address.get(), self.var_pcode.get(), self.var_email.get(), self.var_mobile.get(), self.var_idtype.get(), self.var_idnumber.get(), self.var_room.get()))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student info has been added!!!", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warnings",f"Some things went wrong:{str(es)}", parent=self.root)
    
    #========== Showing Data on Table===========#
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="root", database="hall_management")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Student_details.delete(*self.Student_details.get_children())
            for i in rows:
                self.Student_details.insert("", END, values=i)
            conn.commit()
        conn.close()

    #========= Get the Data on Left Side to Edit By SELECTING ===============#
    def get_cursor(self,event=""):
        cursor_row=self.Student_details.focus()
        content=self.Student_details.item(cursor_row)
        row=content["values"]
        
        self.var_roll.set(row[0]),
        self.var_dept.set(row[1]),
        self.var_stdnt_name.set(row[2]),
        self.var_fname.set(row[3]),
        self.var_mname.set(row[4]),
        self.var_address.set(row[5]),
        self.var_pcode.set(row[6]),
        self.var_email.set(row[7]),
        self.var_mobile.set(row[8]),
        self.var_idtype.set(row[9]),
        self.var_idnumber.set(row[10]),
        self.var_room.set(row[11])
    
    
    #=========== UPDATE ===========#
    def update(self):
        if self.var_mobile.get=="":
            messagebox.showerror("Error", "Please Enter Mobile Number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="root", database="hall_management")
            my_cursor=conn.cursor()
            my_cursor.execute("update student set dept=%s, name=%s, fname=%s, mname=%s, address=%s, pcode=%s, email=%s, mobile=%s, idtype=%s, idnumber=%s, room=%s where roll=%s",(self.var_dept.get(), self.var_stdnt_name.get(), self.var_fname.get(), self.var_mname.get(), self.var_address.get(), self.var_pcode.get(), self.var_email.get(), self.var_mobile.get(), self.var_idtype.get(), self.var_idnumber.get(), self.var_room.get(), self.var_roll.get()))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Student Data Updated Successfully", parent=self.root)
    
    #============ DELETE DATA ============#
    def dDelete(self):
        dDelete=messagebox.askyesno("Student Data", "Do you want to Delete this Student Data???", parent=self.root)
        if dDelete>0:
            conn=mysql.connector.connect(host="localhost", username="root", password="root", database="hall_management")
            my_cursor=conn.cursor()
            query="delete from student where roll=%s"
            value=(self.var_roll.get(),)
            my_cursor.execute(query,value)
        else:
            if not dDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    
    #======== RESET =============#
    def reset(self):
        self.var_roll.set(""),
        self.var_dept.set(""),
        self.var_stdnt_name.set(""),
        self.var_fname.set(""),
        self.var_mname.set(""),
        self.var_address.set(""),
        self.var_pcode.set(""),
        self.var_email.set(""),
        self.var_mobile.set(""),
        self.var_idtype.set(""),
        self.var_idnumber.set(""),
        self.var_room.set("")
    

    def search(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="root", database="hall_management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from student where "+str(self.search_val.get())+" LIKE'%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Student_details.delete(*self.Student_details.get_children())
            for i in rows:
                self.Student_details.insert("", END, values=i)
            conn.commit()
        conn.close()














if __name__=="__main__":
    root=Tk()
    obj=student_win(root)
    root.mainloop()