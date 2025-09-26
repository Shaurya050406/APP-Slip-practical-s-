'''Slip 3: Update Customer Email
Table: customer(cust_id INT PRIMARY KEY, name VARCHAR(50), email
VARCHAR(100))
Problem:
Allow the user to enter a customer ID and a new email address. On clicking Update, the
customer's email in the database should be updated.'''

import tkinter as tk
import mysql.connector

def update_email():
    try:
        cust_id = int(entry_id.get())
        new_email = entry_email.get()
        con = mysql.connector.connect(host="localhost", user="root", password="shaurya", database="slip3")
        cursor = con.cursor()
        cursor.execute("UPDATE customer SET email=%s WHERE cust_id=%s", (new_email, cust_id))
        con.commit()
        print("Customer email updated successfully!" if cursor.rowcount else "Customer ID not found!")
        entry_id.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        cursor.close()
        con.close()
    except Exception as e:
        print("Error:", e)

root = tk.Tk()
root.title("Update Customer Email")

tk.Label(root, text="Customer ID").grid(row=0, column=0, padx=10, pady=5)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="New Email").grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Update Email", command=update_email).grid(row=2, column=0, columnspan=2, pady=10)
root.mainloop()
