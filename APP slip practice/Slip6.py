'''Slip 6: Insert and Validate Flight Booking
Table: flight_booking(booking_id INT PRIMARY KEY, passenger_name VARCHAR(100), destination VARCHAR(100),
fare FLOAT)
Problem:
Build a Tkinter form to insert a new flight booking. Validate that:
● Passenger name is not empty
● Fare is a positive number'''

import tkinter as tk
import mysql.connector

def insert_booking():
    try:
        booking_id = int(entry_id.get())
        passenger_name = entry_name.get().strip()
        destination = entry_dest.get().strip()
        fare_text = entry_fare.get().strip()

        if not passenger_name:
            print("Passenger name cannot be empty!")
            return
        if not destination:
            print("Destination cannot be empty!")
            return
        try:
            fare = float(fare_text)
            if fare <= 0:
                print("Fare must be a positive number!")
                return
        except ValueError:
            print("Fare must be a valid number!")
            return

        con = mysql.connector.connect(host="localhost", user="root", password="shaurya", database="slip6")
        cur = con.cursor()
        cur.execute("INSERT INTO flight_booking (booking_id, passenger_name, destination, fare) VALUES (%s, %s, %s, %s)",
                    (booking_id, passenger_name, destination, fare))
        con.commit()
        con.close()

        print("Booking inserted successfully!")
        entry_id.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_dest.delete(0, tk.END)
        entry_fare.delete(0, tk.END)

    except mysql.connector.Error as e:
        print("Database Error:", e)
    except ValueError:
        print("Booking ID must be an integer!")

root = tk.Tk()
root.title("Flight Booking Form")

tk.Label(root, text="Booking ID").grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Label(root, text="Passenger Name").grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Label(root, text="Destination").grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Label(root, text="Fare").grid(row=3, column=0, padx=10, pady=5, sticky="w")

entry_id = tk.Entry(root)
entry_name = tk.Entry(root)
entry_dest = tk.Entry(root)
entry_fare = tk.Entry(root)

entry_id.grid(row=0, column=1, padx=10, pady=5)
entry_name.grid(row=1, column=1, padx=10, pady=5)
entry_dest.grid(row=2, column=1, padx=10, pady=5)
entry_fare.grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Insert Booking", command=insert_booking).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
