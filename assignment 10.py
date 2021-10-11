from tkinter import *
import pymysql
from tkinter import messagebox as m
from functools import partial

root = Tk()
root.geometry("500x350")
root.title("Form Fill")

def create():
    return pymysql.connect(host="localhost", database="tkinter form", user="root", password="", port=3306)

def insertdata():
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()

    if(firstname=="" or lastname=="" or email=="" or contact==""):
        m.showinfo("Insert status", "All The Field Mandatory")
    else:
        conn = create()
        cursor = conn.cursor()
        args = (firstname, lastname, email, contact)
        query = "insert into form(FirstName, LastName, Email, Contact)values(%s, %s, %s, %s)"
        cursor.execute(query, args)
        conn.commit()
        m.showinfo("Insert Status", "Data Inserted Successfully")
        conn.close()

def Search(No):
        No = srno_entry.get()
        conn = create()
        cursor = conn.cursor()
        args = (No)
        query = "select * from form where No=%s"
        cursor.execute(query, args)
        result = cursor.fetchall()
        for i in result:
            m.showinfo("Your Result", i)

def Update(firstname, lastname, email, contact, No):
    No = srno_entry.get()
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()

    conn = create()
    cursor = conn.cursor()
    args = (firstname, lastname, email, contact, No)
    query = "update Form set FirstName=%s, LastName=%s, Email=%s ,Contact=%s where No=%s"
    cursor.execute(query, args)
    conn.commit()
    m.showinfo("Update into", "Data Updated Successfully")
    conn.close()

def Delete(No):
    No = srno_entry.get()
    conn = create()
    cursor = conn.cursor()
    args = (No)
    query = "delete from Form where No=%s"
    cursor.execute(query, args)
    conn.commit()
    m.showinfo("Delete", "Your Data Deleted Successfully")
    conn.close()

my = Label(root, text="Assignment Form Fill", font="Pixel 25 bold underline", pady=4,
           padx=25, fg="white", bg="grey", relief=RAISED)
my.place(x=50, y=20)

srno = Label(root, text="Sr.no", font="simple 13 bold").place(x=20, y=90)
firstname = Label(root, text="First Name", font="simple 13 bold").place(x=20, y=120)
lastname = Label(root, text="Last Name", font="simple 13 bold").place(x=20, y=150)
email = Label(root, text="Email", font="simple 13 bold").place(x=20, y=180)
contact = Label(root, text="Contact", font="simple 13 bold").place(x=20, y=210)

srno_entry = Entry(root)
firstname_entry = Entry(root)
lastname_entry = Entry(root)
email_entry = Entry(root)
contact_entry = Entry(root)

srno_entry.place(x=130, y=90)
firstname_entry.place(x=130, y=120)
lastname_entry.place(x=130, y=150)
email_entry.place(x=130, y=180)
contact_entry.place(x=130, y=210)

inset = Button(root, text="Insert", font="poetry 13 bold", command=insertdata).place(x=20, y=250)
search = Button(root, text="Search", font="poetry 13 bold", command=partial(Search, 1)).place(x=120, y=250)
update = Button(root, text="Update", font="poetry 13 bold", command =partial(Update, firstname, lastname, email, contact, 1)).place(x=220, y=250)
delete = Button(root, text="Delete", font="poetry 13 bold", command=partial(Delete, 1)).place(x=320, y=250)

root.mainloop()