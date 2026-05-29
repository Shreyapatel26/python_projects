import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.geometry("250x350")
root.title('to-do list app')
root.resizable(False, False)
root.config(bg="#3D2948", padx=20, pady=20)

# variables 
main_font="DejaVu Serif"
all_bg="#3D2948"
all_fg="#EACAFF"
placeholder_color="#666666"

# FUNCTIONS 
def add_task():
    task = task_entry.get()

    if task != "" and task != "Enter task...":
        task_frame = tk.Frame(
            tasks_frame,
            bg="#5B3F6A"
        )
        task_frame.pack(fill="x", pady=3)

        task_label = tk.Label(
            task_frame,
            text=task,
            font=(main_font, 10),
            bg="#5B3F6A",
            fg="#EACAFF",
            anchor="w"
        )
        task_label.pack(
            side="left",
            padx=10,
            pady=5
        )

        delete_btn = tk.Button(
            task_frame,
            text="x",
            font=(main_font, 10),
            bg=all_bg,
            fg=all_fg,
            relief="flat",
            bd=0,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#EE7272",
            activeforeground=all_bg,

            command=task_frame.destroy
        )
        delete_btn.pack(
            side="right",
            padx=5,
            pady=5,
            fill="x"
        )

        task_entry.delete(0, tk.END)

def on_focus_in(event):
    if task_entry.get() == "Enter task...":
        task_entry.delete(0, tk.END)
        task_entry.config(fg=all_fg)

def on_focus_out(event):
    if task_entry.get() == "":
        task_entry.insert(0, "Enter task...")
        task_entry.config(fg=placeholder_color)

# GUI

#  date and time
today = datetime.now()
current_day = today.strftime("%A")
current_date = today.strftime("%d %B %Y")

day_label = tk.Label(
    root,
    text=current_day,
    font=(main_font, 17),
    bg=all_bg,
    fg=all_fg
)
day_label.pack()

date_label = tk.Label(
    root,
    text=current_date,
    font=(main_font, 7, "bold"),
    bg=all_bg,
    fg=all_fg
)
date_label.pack()

# seperator
seperator = tk.Frame(
    root,
    bg=all_fg,
    width=150,
    height=1
)
seperator.pack(pady=8)

# a base frame to hold the text field and add task button together
input_frame = tk.Frame(
    root,
    bg=all_bg
)
input_frame.pack(fill="x", pady=10)

# added tasks-list frame
tasks_frame = tk.Frame(
    root,
    bg=all_bg
)
tasks_frame.pack(
    expand=True,
    fill="both"
)

# add task button
addtask_btn = tk.Button(
    input_frame,
    text="+",
    font=(main_font, 13),
    bg="#1E1424",
    fg="#EACAFF",
    relief="flat",
    highlightthickness=0,
    borderwidth=0,
    activebackground="#781F93",
    activeforeground="#FFFFFF",

    command=add_task
)
addtask_btn.pack(side="left", fill="both")

# the text field to enter task
task_entry = tk.Entry(
    input_frame,
    font=(main_font, 12),
    relief="flat",
    bd=0,
    fg="#EACAFF",
    bg="#1E1424",
    highlightthickness=0,
    insertbackground=all_fg
)

# entry placeholder
task_entry.insert(0, "Enter task...")
task_entry.config(fg=placeholder_color)

task_entry.bind("<FocusIn>", on_focus_in)
task_entry.bind("<FocusOut>", on_focus_out)

task_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=10
)

root.mainloop()
