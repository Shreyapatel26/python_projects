# NOTE: ENTER YOUR API KEY WITNIN THE DOUBLE QUOTES ON LINE 6 FOR THE CODE TO WORK
import tkinter as tk
import requests
from datetime import datetime, timezone, timedelta

API_KEY = "YOUR_API_KEY"

root = tk.Tk()
root.title("world clock")
root.geometry("550x370")
root.resizable(False, False)

font_style = {
    "font_family": "Arial",
    "normal": 13,
    "medium": 15,
    "large": 20,
    "title": 22,
    "clock": 28
}
# variables
bg="#111111"
time_bg="#534D4D"
clockcard_bg="#222222"
ddse_bg="#383737" # ddse = date, day, search, entry
clock_fg="#87EDFA"
fg="#dcdcdc"

timezone_offset = None

root.config(bg=bg)

# search area
search_frame = tk.Frame(root, bg=bg)
search_frame.pack(fill="x", padx=10, pady=10)

search_btn = tk.Button(
    search_frame,
    text="Search",
    bd=0,
    relief="flat",
    bg=ddse_bg,
    highlightthickness=0,
    activebackground="#87EDFA",
    activeforeground=bg,
    fg=fg,
    font=(font_style["font_family"], font_style["normal"])
)
search_btn.pack(
    side="left",
    padx=(0, 10),
    ipady=3
)

search_entry = tk.Entry(
    search_frame,
    bd=0,
    relief="flat",
    bg=ddse_bg,
    highlightthickness=0,
    fg=fg,
    insertbackground=fg,
    font=(font_style["font_family"], font_style["normal"])
)
search_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=7
)

# placeholder
search_entry.insert(0, "Enter city or country...")
def clear_placeholder(event):
    if search_entry.get() == "Enter city or country...":
        search_entry.delete(0, tk.END)
        search_entry.config(fg=fg)

def add_placeholder(event):
    if not search_entry.get():
        search_entry.insert(0, "Enter city or country...")
        search_entry.config(fg=bg)

search_entry.bind("<FocusIn>", clear_placeholder)
search_entry.bind("<FocusOut>", add_placeholder)

# main card
main_frame = tk.Frame(
    root,
    bg=clockcard_bg
)

city_label = tk.Label(
    main_frame,
    text="",
    bg=clockcard_bg,
    fg=fg,
    font=(font_style["font_family"], font_style["large"], "bold")
)
city_label.pack(fill="x", pady=15)

bottom_frame = tk.Frame(
    main_frame,
    bg=clockcard_bg
)
bottom_frame.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

# date section
date_frame = tk.Frame(
    bottom_frame,
    bg=ddse_bg,
    width=170
)
date_frame.pack(
    side="left",
    fill="both"
)
date_frame.pack_propagate(False)

date_content = tk.Frame(
    date_frame,
    bg=ddse_bg
)
date_content.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)

day_label = tk.Label(
    date_content,
    text="",
    bg=ddse_bg,
    fg=fg,
    font=(font_style["font_family"], font_style["large"], "bold")
)
day_label.pack()

date_label = tk.Label(
    date_content,
    text="",
    bg=ddse_bg,
    fg=fg,
    font=(font_style["font_family"], font_style["medium"])
)
date_label.pack()

# time section
time_frame = tk.Frame(
    bottom_frame,
    bg=time_bg
)
time_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(10, 0)
)

time_label = tk.Label(
    time_frame,
    text="",
    bg=time_bg,
    fg=clock_fg,
    font=(font_style["font_family"], font_style["clock"], "bold")
)
time_label.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)

def update_clock():
    if timezone_offset is not None:
        utc_now = datetime.now(timezone.utc)
        local_time = utc_now + timedelta(seconds=timezone_offset)

        day_label.config(text=local_time.strftime("%A"))
        date_label.config(text=local_time.strftime("%d %B %Y"))
        time_label.config(text=local_time.strftime("%H:%M:%S %p"))

    root.after(1000, update_clock)

# search function
def search_city():
    global timezone_offset

    city = search_entry.get().strip()

    if city == "Enter city or country...":
        return
    if not city:
        return
    try:
        geo_url = (
    "https://api.openweathermap.org/geo/1.0/direct"
    f"?q={city}"
    f"&limit=1"
    f"&appid={API_KEY}"
)

        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()

        if not geo_data:
            city_label.config(text="City Not Found")
            return

        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]
        city_name = geo_data[0]["name"]
        country = geo_data[0]["country"]

        weather_url = (
    "https://api.openweathermap.org/data/2.5/weather"
    f"?lat={lat}"
    f"&lon={lon}"
    f"&appid={API_KEY}"
)

        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        timezone_offset = weather_data["timezone"]

        utc_now = datetime.now(timezone.utc)
        local_time = utc_now + timedelta(seconds=timezone_offset)

        city_label.config(text=f"{city_name}, {country}")
        day_label.config(text=local_time.strftime("%A"))
        date_label.config(text=local_time.strftime("%d %B %Y"))
        time_label.config(text=local_time.strftime("%H:%M:%S %p"))

        if not main_frame.winfo_ismapped():
            main_frame.pack(
                fill="both",
                expand=True,
                padx=10,
                pady=(0, 10)
            )

    except Exception as e:
        city_label.config(text="Error")

search_btn.config(command=search_city)

update_clock()

root.mainloop()
