from tkinter import *
import sqlite3

# Create main window
root = Tk()
root.title('My SQLITE3 Project')  # Corrected 'tittle' to 'title'
root.geometry("500x500")

# Database setup
conn = sqlite3.connect('lemhyldb.db')  # Added .db extension for SQLite
c = conn.cursor()

# Create table if it doesn't exist
c.execute("""
CREATE TABLE IF NOT EXISTS myinfo (
    first_name TEXT,
    last_name TEXT,
    age TEXT,
    address TEXT,
    email TEXT
)""")
conn.commit()

# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
age = Entry(root, width=30)
age.grid(row=2, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=3, column=1, padx=20)
email = Entry(root, width=30)
email.grid(row=4, column=1, padx=20)  # Changed to row 4

# Create textbox labels
f_name_label = Label(root, text="Firstname")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Lastname")
l_name_label.grid(row=1, column=0)
age_label = Label(root, text="Age")
age_label.grid(row=2, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=3, column=0)
email_label = Label(root, text="Email")  # Changed text to "Email"
email_label.grid(row=4, column=0)  # Changed to row 4

# Function to submit data to the database
def submit():
    # Insert into table
    c.execute("INSERT INTO myinfo (first_name, last_name, age, address, email) VALUES (?, ?, ?, ?, ?)", 
              (f_name.get(), l_name.get(), age.get(), address.get(), email.get()))
    conn.commit()

    # Clear the input fields
    f_name.delete(0, END)
    l_name.delete(0, END)
    age.delete(0, END)
    address.delete(0, END)
    email.delete(0, END)

    # Fetch and display records
    c.execute("SELECT *, oid FROM myinfo")
    records = c.fetchall()
    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + "\n"

    query_label.config(text=print_records)

# Create submit button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Label to display records
query_label = Label(root, text="")
query_label.grid(row=7, column=0, columnspan=2)

# Close the connection when the application is closed
def on_closing():
    conn.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
