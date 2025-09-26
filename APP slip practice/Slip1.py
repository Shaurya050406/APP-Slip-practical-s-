'''Slip 1: Employee Record Insertion
Table: employee(emp_id INT PRIMARY KEY, name VARCHAR(50), salary FLOAT)
Problem:
Create a Tkinter form to accept employee ID, name, and salary. On clicking Submit, insert the
data into the employee table.'''

import tkinter as tk
import mysql.connector

def submit():
    try:
        conn = mysql.connector.connect(host="127.0.0.1", user="root", password="shaurya", database="slip1")
        conn.cursor().execute("INSERT INTO employee VALUES (%s, %s, %s)", 
                              (empid.get(), name.get(), sal.get()))
        conn.commit()
        print("Data inserted!")
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

root = tk.Tk()
root.title("Employee Form")

tk.Label(root, text="Employee ID").grid(row=0, column=0, padx=10, pady=5)
empid = tk.Entry(root)
empid.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Name").grid(row=1, column=0, padx=10, pady=5)
name = tk.Entry(root)
name.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Salary").grid(row=2, column=0, padx=10, pady=5)
sal = tk.Entry(root)
sal.grid(row=2, column=1, padx=10, pady=5)

submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()

