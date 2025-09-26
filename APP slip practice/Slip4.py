'''Slip 4: Delete Book Record
Table: books(book_id INT PRIMARY KEY, title VARCHAR(100), author VARCHAR(50), price FLOAT)
Problem:
Design a GUI that allows the user to enter a Book ID and delete the corresponding book record
from the database.'''

import tkinter as tk
import mysql.connector

def delete_book():
    try:
        book_id = int(entry_id.get())
        con = mysql.connector.connect(host="localhost", user="root", password="shaurya", database="slip4")
        cursor = con.cursor()
        cursor.execute("DELETE FROM books WHERE book_id=%s", (book_id,))
        con.commit()
        print("Book record deleted successfully!" if cursor.rowcount else "Book ID not found!")
        entry_id.delete(0, tk.END)
        cursor.close()
        con.close()
    except Exception as e:
        print("Error:", e)

root = tk.Tk()
root.title("Delete Book Record")

tk.Label(root, text="Book ID").grid(row=0, column=0, padx=10, pady=5)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=10, pady=5)

tk.Button(root, text="Delete Book", command=delete_book).grid(row=1, column=0, columnspan=2, pady=10)
root.mainloop()
