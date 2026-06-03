import tkinter as tk
import random, string

root = tk.Tk()
root.title("password generator")
root.geometry("520x470")
root.resizable(False, False)
root.config(bg="#14141C")
root.option_add("*HighlightThickness", 0)
root.option_add("*Bd", 0)

# colors
bg = "#14141C"
card_bg = "#1E1E2A"
box_bg = "#2A2A3D"
text_color = "#E6E6FA"
accent = "#7C5CFF"
generate_pink = "#FFA7F2" 
click_pink = "#CA85C0"

# variables
use_upper = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)

# FUNCTIONS 
def check_strength(password):
    strength_label.config(text="")

    point = 0
    if len(password) >= 8:
        point += 1
    if any(char.islower() for char in password):
        point += 1
    if any(char.isupper() for char in password):
        point += 1
    if any(char.isdigit() for char in password):
        point += 1
    if any(char in string.punctuation for char in password):
        point += 1

    if point <= 2:
        strength_label.config(text="Weak", fg="#FF6B6B")
    elif point <= 4:
        strength_label.config(text="Medium", fg="#FFB84C")
    else:
        strength_label.config(text="Strong", fg="#4CAF50")

def generate_password():
    try:
        strength_label.config(text="")
        copy_label.config(text="")
        error_label.config(text="")

        length = int(length_entry.get())

        if length <= 0:
            password_var.set("")
            error_label.config(text="Length must be greater than 0")
            return

        characters = string.ascii_lowercase

        if use_upper.get():
            characters += string.ascii_uppercase
        if use_digits.get():
            characters += string.digits
        if use_symbols.get():
            characters += string.punctuation

        password = "".join(random.choice(characters) for _ in range(length))

        password_var.set(password)
        check_strength(password)

    except ValueError:
        password_var.set("")
        strength_label.config(text="")
        error_label.config(text="Enter numbers only")

def copy_password():
    password = password_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        copy_label.config(text=" Password copied!")

# UI 
outer = tk.Frame(root, bg=bg)
outer.pack(fill="both", expand=True)

main = tk.Frame(outer, bg=card_bg, padx=23, pady=23)
main.pack(fill="both", expand=True, padx=23, pady=23)

# title
title = tk.Label(
    main,
    text="🔐 Password Generator",
    bg=card_bg,
    fg=text_color,
    font=("Arial", 20, "bold")
)
title.pack(anchor="w", pady=(0, 5))

subtitle = tk.Label(
    main,
    text="Generate secure, random passwords instantly",
    bg=card_bg,
    fg=generate_pink,
    font=("Arial", 10)
)
subtitle.pack(anchor="w", pady=(0, 12))

include_label = tk.Label(
    main,
    text="⚙️ Include:",
    bg=card_bg,
    fg=text_color,
    font=("Arial", 11, "bold")
)
include_label.pack(anchor="w", pady=(0, 5))

# checkbox
cb_style = {
    "bg": card_bg,
    "fg": text_color,
    "activebackground": card_bg,
    "activeforeground": text_color,
    "selectcolor": accent,
    "font": ("Arial", 10),
}
tk.Checkbutton(main, text="Uppercase", variable=use_upper, **cb_style).pack(anchor="w")
tk.Checkbutton(main, text="Numbers", variable=use_digits, **cb_style).pack(anchor="w")
tk.Checkbutton(main, text="Symbols", variable=use_symbols, **cb_style).pack(anchor="w")

tk.Frame(main, bg="#2F2F44", height=2).pack(fill="x", pady=10)

# password length
length_label = tk.Label(
    main,
    text="Password Length",
    bg=card_bg,
    fg=text_color,
    font=("Arial", 11, "bold")
)
length_label.pack(anchor="w")

length_frame = tk.Frame(main, bg=card_bg)
length_frame.pack(fill="x", pady=10)

length_entry = tk.Entry(
    length_frame,
    font=("Arial", 12),
    bg=box_bg,
    fg=text_color,
    insertbackground=text_color,
    relief="flat",
    width=10
)
length_entry.pack(side="left", ipady=9)

gen_btn = tk.Button(
    length_frame,
    text="GENERATE",
    command=generate_password,
    bg=generate_pink,
    fg=bg,
    relief="flat",
    font=("Arial", 10, "bold"),
    width=18,
    activebackground=click_pink,
    activeforeground="white"
)
gen_btn.pack(side="left", padx=10, ipady=6)

error_label = tk.Label(main, text="", 
        bg=card_bg,
        fg="#FF6B6B",
        font=("Arial", 10)
)
error_label.pack(anchor="w")

# generated password
pass_frame = tk.Frame(main, bg=card_bg)
pass_frame.pack(fill="x", pady=12)

password_var = tk.StringVar()

password_entry = tk.Entry(
    pass_frame,
    textvariable=password_var,
    font=("Consolas", 13),
    bg=box_bg,
    fg=text_color,
    insertbackground=text_color,
    relief="flat"
)
password_entry.pack(side="left", fill="x", expand=True, ipady=8)

copy_btn = tk.Button(
    pass_frame,
    text="📋 COPY",
    command=copy_password,
    bg=card_bg,
    fg=text_color,
    relief="flat",
    font=("Arial", 10, "bold"),
    activebackground=click_pink,
    activeforeground="white",
    highlightthickness=1,
    highlightbackground="white",
    bd=0
)
copy_btn.pack(side="left", padx=10, ipady=7)

status_frame = tk.Frame(main, bg=card_bg)
status_frame.pack(fill="x", pady=(5, 0))

strength_label = tk.Label(
    status_frame,
    text="",
    bg=card_bg,
    fg=text_color,
    font=("Arial", 11, "bold")
)
strength_label.pack(side="left")

copy_label = tk.Label(
    status_frame,
    text="",
    bg=card_bg,
    fg=generate_pink,
    font=("Arial", 11)
)
copy_label.pack(side="right")

root.mainloop()
