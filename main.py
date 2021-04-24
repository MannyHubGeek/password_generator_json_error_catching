from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    let_list = [random.choice(letters)for _ in range(nr_letters)]



    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    symbol_list = [random.choice(symbols)for _ in range(nr_symbols)]



    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    numbers_list = [random.choice(numbers)for _ in range(nr_numbers)]

    password_list = let_list + symbol_list + numbers_list
    # Shuffle the numbers
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char
    password = "".join(password_list)

    password_textbox_entry_box.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_textbox_entry_box.get()
    username = email_username_entry_box.get()
    password = password_textbox_entry_box.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(password) == 0 or len(website) == 0 or len(username) == 0:
        messagebox.showinfo(title="Validation Failed", message="Don't leave any fields empty")
    else:


        is_ok = messagebox.askokcancel(title=website, message=f"These are the detils entered: \n Email/Username : {username}, \nPassword: {password}, \nDo you want to save entries?")
        if is_ok:
            try:

                with open("data.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)
                    # file.write(f"{username} | ")
                    # file.write(f"{website} | ")
                    # file.write(f"{password}\n")
                    # website_textbox_entry_box.delete(0, END) # Deletes entries in box after save action
                    # password_textbox_entry_box.delete(0, END)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
                    website_textbox_entry_box.delete(0, END) # Deletes entries in box after save action
                    password_textbox_entry_box.delete(0, END)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
                    website_textbox_entry_box.delete(0, END) # Deletes entries in box after save action
                    password_textbox_entry_box.delete(0, END)
            finally:
                website_textbox_entry_box.delete(0, END)  # Deletes entries in box after save action
                password_textbox_entry_box.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #
def search():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            website = website_textbox_entry_box.get()
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f" Email: {email} \n Password: {password}")
    except FileNotFoundError:
        messagebox.showerror(title="Error!!!", message="No Data File Found")
    except KeyError:
        messagebox.showerror(title="Error!!!", message="No details for the website exit")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PassMan")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg="yellow", highlightthickness=0)
key_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_image)
#timer_text = canvas.create_text(103, 130, text="", fill="white", font=('italic', 35, "bold"))
canvas.grid(row=1, column=2)

# Labels
website_label = Label(window, text="Website:")
website_label.grid(row=2, column=1)

email_username_label = Label(window, text="Email/Username:")
email_username_label.grid(row=3, column=1)

password_label = Label(window, text="Password:")
password_label.grid(row=4, column=1)


# Create 3 Entry text boxes below
website_textbox_entry_box = Entry(window, width=35)
website_textbox_entry_box.grid(row=2, column=2, columnspan=1)
website_textbox_entry_box.focus() # This focus the cursor in that box when app is launched

email_username_entry_box = Entry(window, width=35)
email_username_entry_box.grid(row=3, column=2, columnspan=2)
email_username_entry_box.insert(0, "ohueus@yahoo.com")

password_textbox_entry_box = Entry(window, width=21)
password_textbox_entry_box.grid(row=4, column=2)


# Create buttons widget
generate_password_button = Button(window, text="Generate Password", command=gen_password)
generate_password_button.grid(row=4, column=3)

add_password_button = Button(window, width=36, text="Add", command=add)
add_password_button.grid(row=5, column=2, columnspan=2)

search_entries_button = Button(window, width=15, text="Search", command=search)
search_entries_button.grid(row=2, column=3)



window.mainloop()

