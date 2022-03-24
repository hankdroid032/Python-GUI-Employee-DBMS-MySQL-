from tkinter import *
from PIL import ImageTk, Image  #pip install pillow 
import mysql.connector as connector  #pip install mysql-connector and mysql-connector-python

#-----------------------------------MAIN--functions 1------------------------------------------# 

def connection():  #connection to data base 
    global con
    con = connector.connect(host='localhost', user='root', password='root') #ENTER HOST ,USER AND PASSWORD MANUALLY 

def database():
    connection()
    query = " CREATE DATABASE IF NOT EXISTS employeesdb" #Default database 
    cur = con.cursor()
    cur.execute(query)
    

def usedb():
    connection()
    query = "USE employeesdb" #Database selection command
    cur = con.cursor()
    cur.execute(query)
    

def newtab():
    def okay():
        global z
        z=tab_name.get()
        connection()
        usedb()
        query = "CREATE TABLE" + " " + z + "(emp_id INT(20),f_name VARCHAR(20),l_name VARCHAR(20),salary INT(9),dept_name VARCHAR(20))"
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        root.destroy()

    root = Tk()
    root.title('New Table')
    root.geometry("400x100")

    #text box

    tab_name = Entry(root,width=30)
    tab_name.grid(row=2,column=1)

    #label

    tab_name_label = Label(root,text="Enter table name")
    tab_name_label.grid(row=0,column=0,pady =(10,0))

    #submit_btn
    
    submit_btn = Button(root,text="CREATE",command=okay)
    submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

    root.mainloop()

def showtables():
    connection()
    usedb()

    
    root = Tk()
    root.title('Tables Recorded')
    root.geometry("300x70")


    query = "SHOW TABLES"
    cur = con.cursor()
    cur.execute(query)
    record=cur.fetchall()
    con.commit()

    output = Label(root,text=record)
    output.grid(row=0,column=0,pady =(10,0))

    root.mainloop()

def submit():
    def insert():
        p = table_name.get()
        q = emp_id.get()
        r = f_name.get()
        s = l_name.get()
        t = salary.get()
        u = dept_name.get()
        connection()
        usedb()
        query = "INSERT INTO" + " " + p + "(emp_id,f_name,l_name,salary,dept_name) VALUES (" + q + ","+ " ' "+r+" ' " +","+" ' "+s+" ' "+ "," + t + ","+" ' " + u +" ' " + ")" 
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        root.destroy()
  
    
    #---------------------------------------------------- SUB---main---gui----------------------------#
    root = Tk()
    root.title('Enter values')
    root.geometry("400x400")
    
    #-------------------------------------------------------text boxes main----------------------------# 
    
    emp_id = Entry(root,width=30)
    emp_id.grid(row=0,column=1,padx=20,pady=(10,0))
    
    f_name = Entry(root,width=30)
    f_name.grid(row=1,column=1)
    
    
    l_name = Entry(root,width=30)
    l_name.grid(row=2,column=1)
    
    
    salary = Entry(root,width=30)
    salary.grid(row=3,column=1)
    
    dept_name = Entry(root,width=30)
    dept_name.grid(row=4,column=1)
    
    table_name = Entry(root,width=30)
    table_name.grid(row=5,column=1)
    
    #---------------------------------------------------------labels---------------------------------# 
    
    emp_id_label = Label(root,text="Employee ID")
    emp_id_label.grid(row=0,column=0,pady =(10,0))
    
    f_name_label = Label(root,text="First Name")
    f_name_label.grid(row=1,column=0)
    
    
    l_name_label = Label(root,text="Last Name")
    l_name_label.grid(row=2,column=0)
    
    salary_label = Label(root,text="Salary")
    salary_label.grid(row=3,column=0)
    
    dept_name_label = Label(root,text="Dept Name")
    dept_name_label.grid(row=4,column=0)
    
    
    table_name_label = Label(root,text="Enter Table Name ")
    table_name_label.grid(row=5,column=0)

    #-------------------------------------SUB---submit button------------------------------------#
    
    submit_btn = Button(root,text="Add Record to Database",command=insert)
    submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

    
    root.mainloop()

#------------------------------------------MAIN--FUNCTIONS--2---------------------------------------#

def delete():
    def erase():
        connection()
        usedb()
        g = select_box.get()
        b = table_box.get()
        query = "DELETE FROM"+ " " + b +" "+"WHERE emp_id =" +g 
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        root.destroy()


    root = Tk()
    root.title('Select ID')
    root.geometry("400x100")

    #ID select box
    select_box = Entry(root,width =30)
    select_box.grid(row=0,column=1,pady=5)

    #table name box
    table_box = Entry(root,width =30)
    table_box.grid(row=1,column=1,pady=5)
    
    
    #select box label
    
    select_box_label = Label(root,text="Enter ID")
    select_box_label.grid(row=0,column=0,pady=5)

    #table box label

    table_box_label = Label(root,text="Enter  Table name")
    table_box_label.grid(row=1,column=0,pady=5)

    #erase btn

    erase_btn = Button(root,text="ERASE",command=erase)
    erase_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

    
    root.mainloop()
          
def update():
    def upgrade():
        p = table_box.get()
        q = select_box.get()
        r = f_name.get()
        s = l_name.get()
        t = salary.get()
        u = dept_name.get()
        connection()
        usedb()
        
        query = "UPDATE"+ " " +p+ " " + "SET f_name ="+ " ' " +r+" ' " " ," + "l_name =" + " ' " +s+" ' " " ,"  + "salary =" + " ' " +t+" ' " " ," + "dept_name =" + " ' " +u+" ' "+ "WHERE emp_id =" +q        
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        root.destroy()

       

    root = Tk()
    root.title('Select ID')
    root.geometry("400x400")

    #ID select box
    select_box = Entry(root,width =30)
    select_box.grid(row=0,column=1,pady=5)

    #table name box
    table_box = Entry(root,width =30)
    table_box.grid(row=1,column=1,pady=5)

    f_name = Entry(root,width=30)
    f_name.grid(row=2,column=1)
    
    ar
    l_name = Entry(root,width=30)
    l_name.grid(row=3,column=1)
    
    
    salary = Entry(root,width=30)
    salary.grid(row=4,column=1)
    
    dept_name = Entry(root,width=30)
    dept_name.grid(row=5,column=1)
    
    
    
    #label
    
    select_box_label = Label(root,text="Enter ID")
    select_box_label.grid(row=0,column=0,pady=5)

    table_box_label = Label(root,text="Enter  Table name")
    table_box_label.grid(row=1,column=0,pady=5)

    f_name_label = Label(root,text="First Name")
    f_name_label.grid(row=2,column=0)
    
    
    l_name_label = Label(root,text="Last Name")
    l_name_label.grid(row=3,column=0)
    
    salary_label = Label(root,text="Salary")
    salary_label.grid(row=4,column=0)
    
    dept_name_label = Label(root,text="Dept Name")
    dept_name_label.grid(row=5,column=0)
    

    #update btn

    upgrade_btn = Button(root,text="EDIT",command=upgrade)
    upgrade_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

    
    root.mainloop()
   
       
def showent():
    def fetch():

        M = table_entry.get()
        connection()
        usedb()
        query = "SELECT * FROM " + " " + M
        cur = con.cursor()
        cur.execute(query)
        record=cur.fetchall()
        con.commit()

        root = Tk()
        root.title('Entries Recorded')
        root.geometry("500x500")


        output_label = Label(root,text=record)
        output_label.grid(row=0,column=0,pady =(50,50))


        root.mainloop()
      

    root = Tk()
    root.title('Entries Recorded')
    root.geometry("400x100")

    #table_box

    table_entry = Entry(root,width =30)
    table_entry.grid(row=0,column=1,pady=5)

    #table_box_label

    table_entry_label = Label(root,text="Enter Table name")
    table_entry_label.grid(row=0,column=0,pady=5)
    
    #fetch btn 

    fetch_btn = Button(root,text="FETCH",command=fetch)
    fetch_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
    
    root.mainloop()
   
       
def deletetable():
    def delquery():
        L=deltable_entry.get()
        connection()
        usedb()
        query = "DROP TABLE" + " " + L
        cur = con.cursor()
        cur.execute(query)
        con.commit()

    root = Tk()
    root.title('Table Deletion')
    root.geometry("400x100")

    #table_box

    deltable_entry = Entry(root,width =30)
    deltable_entry.grid(row=0,column=1,pady=5)

    #table_box_label

    deltable_entry_label = Label(root,text="Enter Table name to delete")
    deltable_entry_label.grid(row=0,column=0,pady=5)

    #confirm_btn

    confirm_btn = Button(root,text="CONFIRM",command=delquery)
    confirm_btn.grid(row=1,column=0,columnspan=2,pady=10,padx=10,ipadx=100)


#----------------------------------#################  MAIN-GUI  ############---------------------------#
root = Tk()
root.title('Employee Database')
root.geometry("400x500")

#buttons 

#New table button

newtab_btn = Button(root,text="CREATE NEW TABLE",command=newtab)
newtab_btn.grid(row=0,column=0,columnspan=2,pady=10,padx=10,ipadx=100)


#show tables button 

showtab_btn= Button(root,text="SHOW TABLES",command=showtables)
showtab_btn.grid(row=1,column=0, columnspan=2,pady=10,padx=10,ipadx=100)


#Insert values btn 

ins_btn= Button(root,text="ADD DATA",command=submit)
ins_btn.grid(row=2,column=0, columnspan=2,pady=10,padx=10,ipadx=100)

#Delete btn

delete_btn= Button(root,text="DELETE ENTRY",command=delete)
delete_btn.grid(row=3,column=0, columnspan=2,pady=10,padx=10,ipadx=100)

#Update btn 

update_table= Button(root,text="EDIT",command=update)
update_table.grid(row=4,column=0, columnspan=2,pady=10,padx=10,ipadx=100)

#show_entry btn 

show_entries= Button(root,text="SHOW ENTRIES",command=showent)
show_entries.grid(row=13,column=0, columnspan=2,pady=10,padx=10,ipadx=100)

#delete_table btn

delete_table= Button(root,text="DELETE TABLE",command=deletetable)
delete_table.grid(row=14,column=0, columnspan=2,pady=10,padx=10,ipadx=100)

database()


root.mainloop()