'''Slip 7: Display Orders by Date
Table: orders(order_id INT PRIMARY KEY, order_date DATE, amount FLOAT)
Problem:
Create a GUI to input a specific date and display all orders placed on that date, including total
amount.'''

import tkinter as tk
import mysql.connector

def show_orders():
    date_value = entry_date.get().strip()
    text_area.delete("1.0", tk.END)

    if not date_value:
        text_area.insert(tk.END, "Please enter a date (YYYY-MM-DD)\n")
        return

    try:
        con = mysql.connector.connect(host="localhost", user="root", password="shaurya", database="slip7")
        cur = con.cursor()
        cur.execute("SELECT order_id, order_date, amount FROM orders WHERE order_date = %s", (date_value,))
        rows = cur.fetchall()

        if not rows:
            text_area.insert(tk.END, "No orders found for this date.\n")
        else:
            total = 0
            text_area.insert(tk.END, f"Orders on {date_value}:\n\n")
            for order_id, order_date, amount in rows:
                text_area.insert(tk.END, f"Order ID: {order_id} | Date: {order_date} | Amount: ₹{amount}\n")
                total += amount
            text_area.insert(tk.END, f"\nTotal Amount: ₹{total}\n")

        con.close()
    except mysql.connector.Error as e:
        text_area.insert(tk.END, f"Database Error: {e}\n")

root = tk.Tk()
root.title("Display Orders by Date")

tk.Label(root, text="Enter Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_date = tk.Entry(root)
entry_date.grid(row=0, column=1, padx=10, pady=5)

tk.Button(root, text="Show Orders", command=show_orders).grid(row=1, column=0, columnspan=2, pady=10)

text_area = tk.Text(root, width=50, height=15)
text_area.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
