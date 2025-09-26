'''Slip 5: Search Doctor by Name
Table: doctor(doc_id INT PRIMARY KEY, name VARCHAR(50), specialty VARCHAR(50))
Problem:
Create a GUI to search for a doctor by name (partial search allowed) and display matching
records with their specialty.'''

import tkinter as tk
import mysql.connector

def search_doctor():
    try:
        search_name = entry_name.get()
        con = mysql.connector.connect(host="localhost", user="root", password="shaurya", database="slip5")
        cur = con.cursor()
        cur.execute("SELECT name, specialty FROM doctor WHERE name LIKE %s", ("%" + search_name + "%",))
        records = cur.fetchall()
        text_area.delete("1.0", tk.END)
        if records:
            for name, specialty in records:
                text_area.insert(tk.END, f"Name: {name}, Specialty: {specialty}\n")
        else:
            text_area.insert(tk.END, "No doctor found.\n")
        con.close()
    except Exception as e:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, f"Error: {e}\n")

root = tk.Tk()
root.title("Search Doctor by Name")

tk.Label(root, text="Enter Doctor Name:").grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Search", command=search_doctor).grid(row=0, column=2, padx=10, pady=10)

text_area = tk.Text(root, width=50, height=10)
text_area.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
