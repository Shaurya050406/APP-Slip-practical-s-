'''Slip 10: Export Employee Records to CSV
Table: employee(emp_id INT PRIMARY KEY, name VARCHAR(50), salary FLOAT)
Problem:
Add a button to your GUI that exports all employee records to a .csv file saved locally.'''


import tkinter as tk
import mysql.connector
import csv

def export_to_csv():
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="shaurya", database="slip1")
        cur = con.cursor()
        cur.execute("SELECT * FROM employee")
        rows = cur.fetchall()

        if not rows:
            print("No employee records found.")
            return

        with open("employee_records.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["emp_id", "name", "salary"])
            writer.writerows(rows)

        print("Employee records exported to employee_records.csv")
        con.close()
    except Exception as e:
        print("Error:", e)

root = tk.Tk()
root.title("Export Employee Records")

tk.Button(root, text="Export to CSV", command=export_to_csv, bg="lightblue", font=("Arial", 12)).pack(pady=20)

root.mainloop()
