import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_random_passwords():
    quantity = int(quantity_entry.get())
    length = int(length_entry.get())
    include_uppercase = uppercase_var.get()
    include_symbols = symbols_var.get()
    include_numbers = numbers_var.get()
    avoid_begin_number_symbol = avoid_begin_var.get()
    avoid_repeated_characters = avoid_repeated_var.get()
    avoid_sequential_characters = avoid_sequential_var.get()

    passwords = []
    for _ in range(quantity):
        characters = string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_symbols:
            characters += string.punctuation
        if include_numbers:
            characters += string.digits

        password = ''
        while len(password) < length:
            char = random.choice(characters)
            if avoid_repeated_characters and char in password:
                continue
            if avoid_sequential_characters and len(password) >= 2:
                if ord(char) == ord(password[-1]) + 1 and ord(password[-1]) == ord(password[-2]) + 1:
                    continue
            password += char

        if avoid_begin_number_symbol and password[0] in string.punctuation + string.digits:
            password = random.choice(string.ascii_lowercase) + password[1:]

        passwords.append(password)

    password_listbox.delete(0, tk.END)
    for password in passwords:
        password_listbox.insert(tk.END, password)

def copy_to_clipboard():
    selected_password = password_listbox.get(tk.ACTIVE)
    if selected_password:
        root.clipboard_clear()
        root.clipboard_append(selected_password)
        messagebox.showinfo("Password Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator  @swiv")

window_width = 270
window_height = 530

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

quantity_label = tk.Label(root, text="Quantity of Passwords:")
quantity_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

quantity_entry = tk.Entry(root)
quantity_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
quantity_entry.insert(0, "1")  

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

length_entry = tk.Entry(root)
length_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
length_entry.insert(0, "12")  

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_checkbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")
uppercase_var.set(True)

symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_checkbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")
symbols_var.set(True)

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_checkbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="w")
numbers_var.set(True)

avoid_begin_var = tk.BooleanVar()
avoid_begin_checkbox = tk.Checkbutton(root, text="Avoid Beginning with Number or Symbol", variable=avoid_begin_var)
avoid_begin_checkbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="w")
avoid_begin_var.set(True)

avoid_repeated_var = tk.BooleanVar()
avoid_repeated_checkbox = tk.Checkbutton(root, text="Avoid Repeated Characters", variable=avoid_repeated_var)
avoid_repeated_checkbox.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="w")
avoid_repeated_var.set(True)

avoid_sequential_var = tk.BooleanVar()
avoid_sequential_checkbox = tk.Checkbutton(root, text="Avoid Sequential Characters e.g. abc, 789", variable=avoid_sequential_var)
avoid_sequential_checkbox.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="w")
avoid_sequential_var.set(True)

generate_button = tk.Button(root, text="Generate Passwords", command=generate_random_passwords)
generate_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

password_listbox = tk.Listbox(root, width=40)
password_listbox.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

copy_button = tk.Button(root, text="Copy Selected to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
