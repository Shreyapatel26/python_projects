import tkinter as tk

root = tk.Tk()
root.geometry("250x300")
root.title('to-do list app')
# root.resizable(False, False)
root.config(bg="#3D2948", padx=20, pady=20)

# variables 
main_font="DejaVu Serif"
all_bg="#3D2948"
all_fg="#EACAFF"

# FUNCTIONS 
def add_task():
    task = task_entry.get()

    if task != "":
        task_frame = tk.Frame(
            tasks_frame,
            bg=all_bg
        )
        task_frame.pack(fill="x", pady=0)

        task_label = tk.Label(
            task_frame,
            text=task,
            font=(main_font, 10),
            bg=all_bg,
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

# GUI
title_label = tk.Label(
    root,
    text="add task here:",
    font=(main_font, 12),
    fg="#EACAFF",
    bg=all_bg
)
title_label.pack(pady=10, anchor="nw")

# a base frame to hold the text field and add task button together
input_frame = tk.Frame(
    root,
    bg=all_bg
)
input_frame.pack(fill="x")

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
addtask_btn.pack(side="right", fill="both")

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
task_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=10
)

root.mainloop()
