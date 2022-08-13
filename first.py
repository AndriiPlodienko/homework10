from logging import root
import tkinter as tk
import mysql.connector


connection = mysql.connector.connect(host="localhost",
                                    user="",
                                    password="",
                                    database="db")
cursor = connection.cursor()

w = tk.Tk()
label = tk.Label(
    text="Ведите информацию:",
    bg="white", 
    fg="black"
)

f1 = tk.Frame(relief=tk.SUNKEN, borderwidth=3)

l1 = tk.Label(master=f1, text="Name:")
e1 = tk.Entry(master=f1, width=50)

l2 = tk.Label(master=f1, text="Email:")
e2 = tk.Entry(master=f1, width=50)

 
l3 = tk.Label(master=f1, text="Street:")
e3 = tk.Entry(master=f1, width=50)

def inform():
    name = e1.get()
    email = e2.get()
    street = e3.get()
    cursor.execute("select name, email, street from vacancy where name = %s and email = %s and street = %s",
    (name, email, street))

    if cursor.fetchone() is None:
        cursor.execute("insert into vacancy(name, email, street) values(%s, %s, %s)",
        (name, email, street))
        connection.commit()
button_f = tk.Frame()
button_f.pack(fill=tk.X, ipadx=5, ipady=5)
btn_submit = tk.Button(master=button_f, text="Save", command=inform)


btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
l3.grid(row=2, column=0)
e3.grid(row=2, column=1)
l2.grid(row=1, column=0)
e2.grid(row=1, column=1)
l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
label.pack()
f1.pack()
w.mainloop()
     