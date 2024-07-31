from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

WHITE = "#FFFFFF"
BLACK = "#000000"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_lets = [choice(letters) for _ in range(randint(8,10))]
    pw_syms = [choice(symbols) for _ in range(randint(2, 4))]
    pw_nums = [choice(numbers) for _ in range(randint(2, 4))]
    pw_list = pw_lets+pw_syms+pw_nums
    shuffle(pw_list)
    password = "".join(pw_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

# take inputs and save them into a file called data.txt then clear the fields
# Website | email | password 
def add_pw():
    web = website_entry.get()
    email = email_entry.get()
    pw = password_entry.get()
    new_data = {
        web: {
            "email": email,
            "password": pw
        }
    }

    if len(web) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                #read +  old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                #write back to json
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    
def find_password():
    web = website_entry.get()
    email = email_entry.get()
    if len(web) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any website name empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Password Information", message="No Data File Found.")
        else:
            if web in data and data[web]["email"] == email:
                messagebox.showinfo(title=web, message=f"Email: {email}\nPassword: {data[web]['password']}")
            else:
                messagebox.showinfo(title="Oops", message="No details for the website exist.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE )

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg=WHITE, fg = BLACK)
website_label.grid(row=1, column=0)

website_entry = Entry(width=21, bg=WHITE, fg = BLACK, highlightthickness=0)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_btn = Button(text="Search", bg=WHITE, fg=BLACK, highlightbackground=WHITE, width=11, command=find_password)
search_btn.grid(row=1, column=2)

email_label = Label(text="Email/Username:", bg=WHITE, fg = BLACK)
email_label.grid(row=2, column=0)

email_entry = Entry(width=37, bg=WHITE, fg = BLACK, highlightthickness=0)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "atijmahesh914@gmail.com")

password_label = Label(text="Password:", bg=WHITE, fg = BLACK)
password_label.grid(row=3, column=0)

password_entry = Entry(width=21, bg=WHITE, fg = BLACK, highlightthickness=0)
password_entry.grid(row=3, column=1)

gen_pw = Button(text="Generate Password", bg=WHITE, fg = BLACK, highlightbackground= WHITE,  width=11, command=generate_pw)
gen_pw.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, bg=WHITE, fg = BLACK, highlightbackground=WHITE, command=add_pw)
add_btn.grid(row=4, column=1, columnspan=3)


window.mainloop()