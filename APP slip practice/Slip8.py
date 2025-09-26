'''Slip 8: Count Total Registered Users
Table: users(user_id INT PRIMARY KEY, username VARCHAR(50), password VARCHAR(50))
Problem:
Design a Tkinter GUI with a button "Count Users". When clicked, it should display the total
number of users in the database.'''

import tkinter as tk
import mysql.connector

def count_users():
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="shaurya", database="slip8")
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM users")
        total = cur.fetchone()[0]
        print(f"Total Registered Users: {total}")
        con.close()
    except Exception as e:
        print("Error:", e)

root = tk.Tk()
root.title("Count Registered Users")
root.geometry("300x200")

tk.Button(root, text="Count Users", command=count_users, bg="lightblue").pack(pady=50)

root.mainloop()
