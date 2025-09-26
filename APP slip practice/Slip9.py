'''Slip 9: Show Movies Above Given Rating
Table: movies(movie_id INT PRIMARY KEY, title VARCHAR(100), rating FLOAT)
Problem:
Create a GUI to input a rating (e.g., 4.0) and display all movies with a rating greater than or
equal to the entered value.'''

import tkinter as tk
import mysql.connector

def show_movies():
    text_area.delete("1.0", tk.END)
    try:
        min_rating = float(entry_rating.get())
        con = mysql.connector.connect(host="localhost", user="root", password="shaurya", database="slip9")
        cur = con.cursor()
        cur.execute("SELECT title, rating FROM movies WHERE rating > %s", (min_rating,))
        rows = cur.fetchall()

        if rows:
            for title, rating in rows:
                text_area.insert(tk.END, f"Title: {title} | Rating: {rating}\n")
            print(f"Found {len(rows)} movies above rating {min_rating}")
        else:
            text_area.insert(tk.END, "No movies found above this rating.\n")
            print("No matching movies found.")

        con.close()
    except ValueError:
        text_area.insert(tk.END, "Please enter a valid number for rating.\n")
        print("Invalid rating input.")
    except Exception as e:
        text_area.insert(tk.END, f"Database Error: {e}\n")
        print("Database Error:", e)

root = tk.Tk()
root.title("Show Movies Above Given Rating")
root.geometry("400x300")

tk.Label(root, text="Enter Minimum Rating:").pack(pady=5)
entry_rating = tk.Entry(root)
entry_rating.pack(pady=5)

tk.Button(root, text="Show Movies", command=show_movies).pack(pady=10)

text_area = tk.Text(root, height=10, width=45)
text_area.pack(pady=5)

root.mainloop()
