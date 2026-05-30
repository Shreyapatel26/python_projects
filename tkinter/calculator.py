import tkinter as tk

root = tk.Tk()
root.geometry("220x300")
root.title("calculator")
root.resizable(False, False)

# themes
blue_theme = {
    "fg": "#ACDDE9",
    "window_bg": "#152835",
    "active_bg": "#0C171F",
    "active_fg": "#D5E5F0",
    "error_fg": "#FF8181",
    "equal_btn_fg": "#294F68"
}
pink_theme = {
    "fg": "#793547",
    "window_bg": "#FC80A7",
    "active_bg": "#F65F99",
    "active_fg": "#FFFEFE",
    "error_fg": "#C12525",
    "equal_btn_fg": "#F54D8D"
}

current_theme = blue_theme
root.config(
    bg=current_theme["window_bg"],
    padx=5,
    pady=5
)

# functions
def entry(value):
    entry_field.insert(tk.END, value)

def clear_button():
    entry_field.delete(0, tk.END)
    entry_field.config(fg=current_theme["fg"])

def calculate():
    try:
        expression = entry_field.get()
        result = eval(expression)
        entry_field.config(fg=current_theme["fg"])
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, result)
    except:
        entry_field.config(fg=current_theme["error_fg"])
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "error")

def apply_theme(theme):
    root.config(bg=theme["window_bg"])
    top_frame.config(bg=theme["window_bg"])
    entry_field.config(
        bg=theme["window_bg"],
        fg=theme["fg"],
        insertbackground=theme["fg"]
    )
    button_frame.config(bg=theme["window_bg"])
    clear_btn.config(
        bg=theme["window_bg"],
        fg=theme["fg"],
        activebackground=theme["active_bg"],
        activeforeground=theme["active_fg"]
    )

# small color square
    theme_btn.config(
        bg=theme["window_bg"],
        activebackground=theme["equal_btn_fg"]
    )

    for btn in normal_buttons:
        btn.config(
            bg=theme["window_bg"],
            fg=theme["fg"],
            activebackground=theme["active_bg"],
            activeforeground=theme["active_fg"]
        )

    equal_button.config(
        bg=theme["equal_btn_fg"],
        fg=theme["fg"],
        activebackground=theme["active_bg"],
        activeforeground=theme["active_fg"]
    )

def toggle_theme():
    global current_theme

    if current_theme == blue_theme:
        current_theme = pink_theme
    else:
        current_theme = blue_theme

    apply_theme(current_theme)

# top frame
top_frame = tk.Frame(root, bg=current_theme["window_bg"])
top_frame.pack(fill="x", padx=5,pady=5)

# theme button (small colored square)
theme_btn = tk.Button(
    top_frame,
    width=1,
    height=1,
    text="🎨",
    font=20,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=toggle_theme
)
theme_btn.pack(side="left", padx=(7, 5))

# entry
entry_field = tk.Entry(
    top_frame,
    font=("Ubuntu Mono", 20),
    justify="right",
    highlightthickness=0,
    relief="flat",
    bg=current_theme["window_bg"],
    fg=current_theme["fg"],
    insertbackground=current_theme["fg"]
)
entry_field.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=10
)

# buttons frame
button_frame = tk.Frame(root, bg=current_theme["window_bg"])
button_frame.pack(expand=True, fill="both")

calc_buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

normal_buttons = []
equal_button = None

for row_index, row in enumerate(calc_buttons):
    button_frame.rowconfigure(row_index, weight=1)
    for column_index, button_text in enumerate(row):
        button_frame.columnconfigure(column_index, weight=1)

        if button_text == "=":
            btn = tk.Button(
                button_frame,
                text=button_text,
                font=("Ubuntu Mono", 15),
                relief="flat",
                borderwidth=0,
                highlightthickness=0,
                bg=current_theme["equal_btn_fg"],
                fg=current_theme["fg"],
                activebackground=current_theme["active_bg"],
                activeforeground=current_theme["active_fg"],
                command=calculate
            )
            equal_button = btn
        else:
            btn = tk.Button(
                button_frame,
                text=button_text,
                font=("Ubuntu Mono", 15),
                relief="flat",
                borderwidth=0,
                highlightthickness=0,
                bg=current_theme["window_bg"],
                fg=current_theme["fg"],
                activebackground=current_theme["active_bg"],
                activeforeground=current_theme["active_fg"],
                command=lambda value=button_text: entry(value)
            )
            normal_buttons.append(btn)

        btn.grid(
            row=row_index,
            column=column_index,
            sticky="nsew",
            padx=4,
            pady=4
        )

# clear button
clear_btn = tk.Button(
    root,
    text="clear",
    font=("Ubuntu Mono", 15),
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    bg=current_theme["window_bg"],
    fg=current_theme["fg"],
    activebackground=current_theme["active_bg"],
    activeforeground=current_theme["active_fg"],
    command=clear_button
)
clear_btn.pack(fill="both", padx=4, pady=10)

apply_theme(current_theme)

root.mainloop()
