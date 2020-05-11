from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()


def insert():
    idd = id_value.get()
    namee = name_value.get()
    coursee = course_value.get()
    phonee = phone_value.get()
    ctypee = ctype_value.get()

    conn = sqlite3.connect("school.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS Student_Data(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,COURSE TEXT NOT NULL,PHONE INT NOT NULL,CTYPE INT NOT NULL)''')

    conn.execute('''INSERT INTO Student_Data(ID,NAME,COURSE,PHONE,CTYPE)VALUES(?,?,?,?,?)''',(idd,namee,coursee,phonee,ctypee))
    conn.commit()
    print("record inserted")
    conn.close()
    id_value.set("")
    name_value.set("")
    course_value.set("")
    phone_value.set("")
    ctype_value.set("")
    messagebox.showinfo('Return', 'record inserted')


def data_read():
    conn=sqlite3.connect('school.db')
    fetch=conn.execute('''SELECT * FROM Student_Data''')
    for records in fetch:
        print(records)
    conn.close()


def ExitApplication():
    MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')




id=Label(root,text="student id").grid(row=1,column=0)
name=Label(root,text="name").grid(row=2,column=0)
course=Label(root,text="course").grid(row=3,column=0)
phone=Label(root,text="phone no").grid(row=4,column=0)

id_value=IntVar()
name_value=StringVar()
course_value=StringVar()
phone_value=IntVar()
ctype_value=IntVar()

id_entry=Entry(root,textvariable=id_value).grid(row=1,column=1)
name_entry=Entry(root,textvariable=name_value).grid(row=2,column=1)
course_entry=Entry(root,textvariable=course_value).grid(row=3,column=1)
phone_entry=Entry(root,textvariable=phone_value).grid(row=4,column=1)

ctype_entry=Checkbutton(root,text=("is ur course type regular"),variable=ctype_value).grid(row=5,column=1)

btn1=Button(root,text="submit",command=insert).grid(row=6,column=0)
btn2=Button(root,text="view",command=data_read).grid(row=6,column=1)
btn3 =Button(root, text='Exit Application', command=ExitApplication).grid(row=7,column=1)
root.mainloop()