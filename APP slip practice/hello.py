import tkinter as tk
import mysql.connector

def search_doc():
    cur.execute("SELECT * FROM doctor WHERE name LIKE %s", ('%'+name.get()+'%',))
    rows = cur.fetchall()
    txt.delete("1.0", tk.END)
    for r in rows: txt.insert(tk.END, f"{r}\n")

db = mysql.connector.connect(host="localhost", user="root", password="shaurya", database="slip5")
cur = db.cursor()

root = tk.Tk()
name = tk.Entry(root); name.pack()
tk.Button(root, text="Search", command=search_doc).pack()
txt = tk.Text(root); txt.pack()
root.mainloop()
