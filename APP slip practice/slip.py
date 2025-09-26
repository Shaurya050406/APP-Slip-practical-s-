import tkinter as tk
import mysql.connector

def insert_employee():
    cur.execute("INSERT INTO employee VALUES (%s,%s,%s)",
                (eid.get(), name.get(), float(sal.get())))
    db.commit()

db = mysql.connector.connect(host="localhost", user="root", password="shaurya", database="slip1")
cur = db.cursor()

root = tk.Tk()
eid, name, sal = tk.Entry(root), tk.Entry(root), tk.Entry(root)
for lbl, e in [("ID", eid), ("Name", name), ("Salary", sal)]:
    tk.Label(root, text=lbl).pack(); e.pack()
tk.Button(root, text="Submit", command=insert_employee).pack()
root.mainloop()
