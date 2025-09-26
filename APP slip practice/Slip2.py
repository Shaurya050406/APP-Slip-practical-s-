'''Slip 2: Display Product Inventory
Table: product(prod_id INT PRIMARY KEY, prod_name VARCHAR(100), quantity
INT, price FLOAT)
Problem:
Create a GUI with a "Show Inventory" button. When clicked, display all products with their
details in a text area.'''

import tkinter as tk
from tkinter import scrolledtext, messagebox
import mysql.connector

def show_inventory():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="shaurya",
            database="slip2"
        )
        cursor = con.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()

        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, f"{'ID':<10}{'Name':<25}{'Quantity':<10}{'Price':<10}\n")
        text_area.insert(tk.END, "-"*55 + "\n")

        for row in rows:
            text_area.insert(tk.END, f"{row[0]:<10}{row[1]:<25}{row[2]:<10}{row[3]:<10}\n")

        con.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error connecting to MySQL: {err}")

# GUI Setup
root = tk.Tk()
root.title("Product Inventory")

tk.Button(root, text="Show Inventory", command=show_inventory).pack(pady=10)
text_area = scrolledtext.ScrolledText(root, width=60, height=15)
text_area.pack(pady=10)

root.mainloop()

