from cgitb import text
from multiprocessing import parent_process
from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Room Booking")
        self.root.geometry("1136x550+225+100")
        self.root.resizable(False, False)


        #============ Variables ===========#
        self.var_mobile=StringVar()
        self.var_date=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_noofmonths=StringVar()
        self.var_room=StringVar()
        self.var_total=StringVar()

        #========== Title =========#
        title=Label(self.root, text="Room Booking", font=("Times New Roman", 18, "bold"), bg="Black", fg="#6162FF", bd=4, relief=RIDGE)
        title.place(x=0,y=0, width=1136, height=40)

        #======= Label Frame =========#
        lframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking",font=("Times New Roman", 12, "bold"), padx=2)
        lframeleft.place(x=5, y=40, width=425, height=500)

        #============== Label and Entries =============#
        #--- Fetching Contact Number ---#
        roll=Label(lframeleft, font=("arial",12,"bold"), text="Mobile Number: ", padx=2, pady=6)
        roll.grid(row=0, column=0, sticky=W)

        txtroll=ttk.Entry(lframeleft, textvariable=self.var_mobile, font=("arial",13,"bold"), width=20)
        txtroll.grid(row=0, column=1, sticky=W)

        #============== Fetch Data Button ==============#
        btnFetchData=Button(lframeleft, command=self.Fetch_data, text="Fetch Data", font=("arial",10,"bold"), bg="Black", fg="Gold", width=8)
        btnFetchData.place(x=330,y=4)
        
        #--- Date ---#
        date=Label(lframeleft, font=("arial",12,"bold"), text="Date: ", padx=2, pady=6)
        date.grid(row=1, column=0, sticky=W)
        
        txtdate=ttk.Entry(lframeleft, textvariable=self.var_date, font=("arial",13,"bold"), width=29)
        txtdate.grid(row=1, column=1)

        #--- Checkin Month ---#
        check_in_month=Label(lframeleft, font=("arial",12,"bold"), text="Month From: ", padx=2, pady=6)
        check_in_month.grid(row=2, column=0, sticky=W)
        
        txtcheck_in_month=ttk.Entry(lframeleft, textvariable=self.var_checkin, font=("arial",13,"bold"), width=29)
        txtcheck_in_month.grid(row=2, column=1)


        #--- Checkout Month ---#
        check_out_month=Label(lframeleft, font=("arial",12,"bold"), text="Month To: ", padx=2, pady=6)
        check_out_month.grid(row=3, column=0, sticky=W)
        
        txtcheck_out_month=ttk.Entry(lframeleft, textvariable=self.var_checkout, font=("arial",13,"bold"), width=29)
        txtcheck_out_month.grid(row=3, column=1)



        #--- No of Months ---#
        NoOfMonths=Label(lframeleft, font=("arial",12,"bold"), text="No Of Months: ", padx=2, pady=6)
        NoOfMonths.grid(row=4, column=0, sticky=W)
        
        txtNoOfMonths=ttk.Entry(lframeleft, textvariable=self.var_noofmonths, font=("arial",13,"bold"), width=29)
        txtNoOfMonths.grid(row=4, column=1)
       
        #--- No of Months ---#
        Room=Label(lframeleft, font=("arial",12,"bold"), text="Room Number: ", padx=2, pady=6)
        Room.grid(row=5, column=0, sticky=W)
        
        txtroom=ttk.Entry(lframeleft, textvariable=self.var_room, font=("arial",13,"bold"), width=29)
        txtroom.grid(row=5, column=1)


        #--- Total Cost ---#
        TotalCost=Label(lframeleft, font=("arial",12,"bold"), text="Total Cost: ", padx=2, pady=6)
        TotalCost.grid(row=6, column=0, sticky=W)
        
        txtTotalCost=ttk.Entry(lframeleft, textvariable=self.var_total, font=("arial",13,"bold"), width=29)
        txtTotalCost.grid(row=6, column=1)

        #================ Bill ================#
        btnbill=Button(lframeleft, text="Bill", command=self.total, font=("arial",12,"bold"), bg="Black", fg="Gold", width=9)
        btnbill.grid(row=7,column=0, padx=1, sticky=W)

        #================ Buttons ==============#
        btnframe=Frame(lframeleft,bd=2,relief=RIDGE)
        btnframe.place(x=0, y=400, width=412, height=40)

        btnadd=Button(btnframe, text="ADD", command=self.add_fees, font=("arial",12,"bold"), bg="Black", fg="Gold", width=9)
        btnadd.grid(row=0,column=0, padx=1)

        btnupdate=Button(btnframe, text="Update", command=self.update, font=("arial",12,"bold"), bg="Black", fg="Gold", width=9)
        btnupdate.grid(row=0,column=1, padx=1)

        btndlt=Button(btnframe, text="Delete", command=self.dDelete, font=("arial",12,"bold"), bg="Black", fg="Gold", width=9)
        btndlt.grid(row=0,column=2, padx=1)

        btnrst=Button(btnframe, text="Reset", command=self.reset, font=("arial",12,"bold"), bg="Black", fg="Gold", width=9)
        btnrst.grid(row=0,column=3, padx=1)

        #=============== Table Frame Search System =========================#
        tableframe=LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",font=("Times New Roman", 12, "bold"), padx=2)
        tableframe.place(x=435, y=180, width=690, height=360)

        lblsearchby=Label(tableframe, font=("arial",12,"bold"), text="Search By: ", bg="red", fg="white")
        lblsearchby.grid(row=0,column=0, padx=4)

        self.search_val=StringVar()
        combo_search=ttk.Combobox(tableframe, textvariable=self.search_val, font=("arial", 13, "bold"), width=10, state="readonly")
        combo_search["value"]=("Mobile", "Room")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=4)
        
        self.txt_search=StringVar()
        txtsearch=ttk.Entry(tableframe, textvariable=self.txt_search, font=("arial",13,"bold"), width=24)
        txtsearch.grid(row=0, column=2, padx=4)

        btnsearch=Button(tableframe, text="Search", command=self.search, font=("arial",12,"bold"), bg="Black", fg="Gold", width=9)
        btnsearch.grid(row=0,column=3, padx=4)

        btnshowall=Button(tableframe, text="Show All", command=self.fetch_data, font=("arial",12,"bold"), bg="Black", fg="Gold", width=9)
        btnshowall.grid(row=0,column=4, padx=4)

        #=============== Show Data Table =================#
        dataframe=Frame(tableframe,bd=2,relief=RIDGE)
        dataframe.place(x=0,y=50,width=680, height=290)

        scroll_x=ttk.Scrollbar(dataframe, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(dataframe, orient=VERTICAL)

        self.fees_table=ttk.Treeview(dataframe, columns=("mobile", "date", "checkin", "checkout", "numberofmonths", "room", "bill"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.fees_table.xview)
        scroll_y.config(command=self.fees_table.yview)

        
        self.fees_table.heading("mobile", text="Mobile")
        self.fees_table.heading("date", text="Date")
        self.fees_table.heading("checkin", text="Month From")
        self.fees_table.heading("checkout", text="Month To")
        self.fees_table.heading("numberofmonths", text="Total Months")
        self.fees_table.heading("room", text="Room Number")
        self.fees_table.heading("bill", text="Total Bill")
        

        self.fees_table["show"]="headings"

        self.fees_table.column("mobile", width=100)
        self.fees_table.column("date", width=100)
        self.fees_table.column("checkin", width=100)
        self.fees_table.column("checkout", width=100)
        self.fees_table.column("numberofmonths", width=100)
        self.fees_table.column("room", width=100)
        self.fees_table.column("bill", width=100)

        self.fees_table.pack(fill=BOTH,expand=1)
        self.fees_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    #=========== ADD ============#
    def add_fees(self):
        if self.var_mobile.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error", "All Fields are Required!!!", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="root", database="hall_management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into fees values(%s,%s,%s,%s,%s,%s,%s)",(self.var_mobile.get(), self.var_date.get(),self.var_checkin.get(), self.var_checkout.get(), self.var_noofmonths.get(), self.var_room.get(), self.var_total.get()))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Fees info has been added!!!", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warnings",f"Some things went wrong:{str(es)}", parent=self.root)
    
    
    #========== Showing Data on Table===========#
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="root", database="hall_management")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from fees")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.fees_table.delete(*self.fees_table.get_children())
            for i in rows:
                self.fees_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
    #========= Get the Data on Left Side to Edit By SELECTING ===============#
    def get_cursor(self,event=""):
        cursor_row=self.fees_table.focus()
        content=self.fees_table.item(cursor_row)
        row=content["values"]
        
        self.var_mobile.set(row[0]),
        self.var_date.set(row[1]),
        self.var_checkin.set(row[2]), 
        self.var_checkout.set(row[3]), 
        self.var_noofmonths.set(row[4]),
        self.var_room.set(row[5])
        
    #=========== UPDATE ===========#
    def update(self):
        if self.var_mobile.get=="":
            messagebox.showerror("Error", "Please Enter Mobile Number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="root", database="hall_management")
            my_cursor=conn.cursor()
            my_cursor.execute("update fees set mobile=%s, checkin=%s, checkout=%s, numberofmonths=%s, room=%s, bill=%s where date=%s",(self.var_mobile.get(),self.var_checkin.get(), self.var_checkout.get(), self.var_noofmonths.get(), self.var_room.get(), self.var_total.get(), self.var_date.get()))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Fees Data Updated Successfully", parent=self.root)
            
    #============ DELETE DATA ============#
    def dDelete(self):
        dDelete=messagebox.askyesno("Fee Data", "Do you want to Delete this Fee Data???", parent=self.root)
        if dDelete>0:
            conn=mysql.connector.connect(host="localhost", username="root", password="root", database="hall_management")
            my_cursor=conn.cursor()
            query="delete from fees where date=%s"
            value=(self.var_date.get(),)
            my_cursor.execute(query,value)
        else:
            if not dDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    
    #======== RESET =============#
    def reset(self):
        self.var_mobile.set(""),
        self.var_date.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_noofmonths.set(""),
        self.var_room.set(""),
        self.var_total.set(""),
        
    
    
    
    #============== Data Fetch ===================#
    def Fetch_data(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error", "Please Enter Mobile Number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="root", database="hall_management")
            my_cursor=conn.cursor()
            query=("Select name from student where mobile=%s")
            value=(self.var_mobile.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()


            if row==None:
                messagebox.showerror("Error", "This Number is Not Found!!!", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame=Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataFrame.place(x=455,y=55,width=350,height=100)

                showDataFrame2=Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataFrame2.place(x=800,y=55,width=320,height=100)

                #=========== Name ===========#
                lblName=Label(showDataFrame, text="Name: ", font=("arial",12, "bold"))
                lblName.grid(row=0,column=0, sticky=W)

                lbl=Label(showDataFrame,text=row, font=("arial",12, "bold"))
                lbl.grid(row=0,column=1, sticky=W)

                #=========== Roll ===========#
                conn=mysql.connector.connect(host="localhost", username="root", password="root", database="hall_management")
                my_cursor=conn.cursor()
                query=("Select roll from student where mobile=%s")
                value=(self.var_mobile.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblRoll=Label(showDataFrame2, text="Roll Number: ", font=("arial",12, "bold"))
                lblRoll.grid(row=0,column=0, sticky=W)

                lbl=Label(showDataFrame2,text=row, font=("arial",12, "bold"))
                lbl.grid(row=0,column=1, sticky=W)
                
                #=========== Dept ===========#
                conn=mysql.connector.connect(host="localhost", username="root", password="root", database="hall_management")
                my_cursor=conn.cursor()
                query=("Select dept from student where mobile=%s")
                value=(self.var_mobile.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblRoll=Label(showDataFrame2, text="Department: ", font=("arial",12, "bold"))
                lblRoll.grid(row=1,column=0, sticky=W)

                lbl=Label(showDataFrame2,text=row, font=("arial",12, "bold"))
                lbl.grid(row=1,column=1, sticky=W)

                #=========== Email ===========#
                conn=mysql.connector.connect(host="localhost", username="root", password="root", database="hall_management")
                my_cursor=conn.cursor()
                query=("Select email from student where mobile=%s")
                value=(self.var_mobile.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblRoll=Label(showDataFrame, text="Email: ", font=("arial",12, "bold"))
                lblRoll.grid(row=1,column=0, sticky=W)

                lbl=Label(showDataFrame,text=row, font=("arial",12, "bold"))
                lbl.grid(row=1,column=1, sticky=W)

                #=========== IDType ===========#
                conn=mysql.connector.connect(host="localhost", username="root", password="root", database="hall_management")
                my_cursor=conn.cursor()
                query=("Select idtype from student where mobile=%s")
                value=(self.var_mobile.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblRoll=Label(showDataFrame, text="ID Type: ", font=("arial",12, "bold"))
                lblRoll.grid(row=2,column=0, sticky=W)

                lbl=Label(showDataFrame,text=row, font=("arial",12, "bold"))
                lbl.grid(row=2,column=1, sticky=W)

                #=========== IDNumber ===========#
                conn=mysql.connector.connect(host="localhost", username="root", password="root", database="hall_management")
                my_cursor=conn.cursor()
                query=("Select idnumber from student where mobile=%s")
                value=(self.var_mobile.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblRoll=Label(showDataFrame2, text="Id Number: ", font=("arial",12, "bold"))
                lblRoll.grid(row=2,column=0, sticky=W)

                lbl=Label(showDataFrame2,text=row, font=("arial",12, "bold"))
                lbl.grid(row=2,column=1, sticky=W)
    
    #=================== Search System =================#
    def search(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="root", database="hall_management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from fees where "+str(self.search_val.get())+" LIKE'%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.fees_table.delete(*self.fees_table.get_children())
            for i in rows:
                self.fees_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    
    #=================== TOTAL COST ==================#
    def total(self):
        bill=int(300)
        months=int(self.var_noofmonths.get())
        totalbill=int(bill*months)
        self.var_total.set(totalbill)
        







        





if __name__=="__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()
