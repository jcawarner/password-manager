from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)


def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Blank Fields", message="Please fill in all fields!!!!")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"Details entered:\n Website: {website}\n "
                                                                          f"Email: {email}"f"\nPassword: "
                                                                          f"{password} \nWould like to Save?")


        if is_ok:
            with open("passwords.txt", "a") as file:
                file.write(f"\n{website_entry.get()} | {email_entry.get()} | {password_entry.get()}")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky=W)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky=W)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky=W, pady=5)
email_entry.insert(0, "jlwarner0903@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky=W)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=W)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=1, columnspan=2, sticky=E)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2, sticky=W, pady=5)

window.mainloop()
