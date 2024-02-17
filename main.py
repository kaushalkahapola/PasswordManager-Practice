from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def pass_gen():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_lettes = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_lettes + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password_entry.get())
    
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def copy():
    pyperclip.copy(password_entry.get())

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if not (website and email and password):
        messagebox.showinfo(title="Missing Values", message="Some values are missing, please fill all to continue saving.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered. Can we continue?\nEmail/Username: {email}\nPassword: {password}\n")
        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            
            website_entry.delete(0, END)
            password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=64)
website_entry.grid(row=1, column=1, columnspan=2,sticky="W")
website_entry.focus()
email_entry = Entry(width=64)
email_entry.grid(row=2, column=1, columnspan=2,sticky="W")
email_entry.insert(0,'kaushal@gmail.com')
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1,sticky="W")

# Buttons
pass_gen_button = Button(text='Generate password',command=pass_gen,width=25)
pass_gen_button.grid(row=3, column=2, sticky="E")  # Align to the left (west)
add_button = Button(text='Add', width=25,command=save)
add_button.grid(row=4, column=1,sticky="W")
copy_button = Button(text='Copy Password', width=25,command=copy)
copy_button.grid(row=4, column=2,sticky="W")

window.mainloop()
