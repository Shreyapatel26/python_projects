import tkinter as tk

root = tk.Tk()
root.geometry("220x300")
root.title("calculator")
root.resizable(False, False)

# variables
all_fore="#ACDDE9"
frame_bg="#152835"
active_bg="#0C171F"
active_fg="#A4CFEB"

root.config(bg=frame_bg, padx=5, pady=5)

entry_field = tk.Entry(
    root,
    font=("Ubuntu Mono", "20"),
    justify="right",
    highlightthickness=0,
    relief="flat",
    bg=frame_bg,
    fg=all_fore,
    insertbackground=all_fore
    
)
entry_field.pack(fill="both", padx=5, pady=5, ipady=10)

# functions
def entry(value):
    entry_field.insert(tk.END, value)

def clear_button():
    entry_field.delete(0, tk.END)

def calculate():
    try:
        expression = entry_field.get()
        result = eval(expression)
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, result)

    except:
        entry_field.config(fg="#FF8181")
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "error")

# buttons
button_frame = tk.Frame(root, bg=frame_bg)
button_frame.pack(expand=True, fill="both")

calc_buttons = [
   ["7", "8", "9", "/"],
   ["4", "5", "6", "*"],
   ["1", "2", "3", "-"],
   ["0", ".", "=", "+"],
]

for row_index, row in enumerate(calc_buttons):
    button_frame.rowconfigure(row_index, weight=1)
    for column_index, button_text in enumerate(row):
        button_frame.columnconfigure(column_index, weight=1)
        if button_text == "=":
            btn = tk.Button(
              button_frame,
              text=button_text,
              font=("Ubuntu Mono", "15"),

              relief="flat",
              borderwidth=0,
              highlightthickness=0,
              bg="#294F68",
              fg=all_fore,
              activebackground=active_bg,
              activeforeground=active_fg,

              command=calculate
            )
        else:
            btn = tk.Button(
                button_frame,
                text=button_text,
                font=("Ubuntu Mono", "15"),

                relief="flat",
                borderwidth=0,
                highlightthickness=0,
                bg=frame_bg,
                fg=all_fore,
                activebackground=active_bg,
                activeforeground=active_fg,

                command=lambda value=button_text: entry(value)
               )

        btn.grid(
            row=row_index,
            column=column_index,
            sticky="nsew",
            padx=4, pady=4
            ) 

clear_btn = tk.Button(
    root,
    text="clear",
     font=("Ubuntu Mono", "15"),

    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    highlightcolor="#536186",
    bg=frame_bg,
    fg=all_fore,
    activebackground=active_bg,
    activeforeground=active_fg,

    command=clear_button
)
clear_btn.pack(fill="both", padx=4, pady=10)

root.mainloop()
