import customtkinter as ctk

# Initialize the GUI window
app = ctk.CTk()
app.title("TBD")
app.geometry("600x400")  # default window size (adjustable)

# set weights for auto-resizing
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# placeholder for gauge
gauge_label = ctk.CTkLabel(app, text="Gauge (placeholder)", corner_radius=10, fg_color="lightgray")
gauge_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nesw")

# battery box bullshit™
battery_val = int((input("battery val: "))) / 100  # takes percentage
# battery_box = ctk.CTkFrame(app, corner_radius=10)
# battery_box.grid(row=2, column=0, padx=10, pady=10, sticky="nesw")
# battery_label = ctk.CTkLabel(battery_box, text="Battery\n", font=("Arial", 16))
# battery_label.pack(expand=True, fill="both")

#Clints lovely and wonderfulcomments
#more comments because I love github
# AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH

# battery progress
progress_bar_1 = ctk.CTkProgressBar(app)
progress_bar_1.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
progress_bar_1.set(battery_val)

# progress Bar 2
bar2_val = int((input("bar2 val: "))) / 100  # takes percentage
progress_bar_2 = ctk.CTkProgressBar(app)
progress_bar_2.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
progress_bar_2.set(bar2_val)

# left tire
left_temp = str(input("left tire: ")) + "°" # must be string cause display error for ints
left_temp_box = ctk.CTkFrame(app, corner_radius=10)
left_temp_box.grid(row=2, column=0, padx=10, pady=10, sticky="nesw")
left_label = ctk.CTkLabel(left_temp_box, text="LEFT:\n" + left_temp, font=("Arial", 16))
left_label.pack(expand=True, fill="both")

# right tire
right_temp = str(input("right tire: ")) + "°" # must be string cause display error for ints
right_temp_box = ctk.CTkFrame(app, corner_radius=10)
right_temp_box.grid(row=2, column=1, padx=10, pady=10, sticky="nesw")
right_label = ctk.CTkLabel(right_temp_box, text="RIGHT:\n" + right_temp, font=("Arial", 16))
right_label.pack(expand=True, fill="both")

# run it
app.mainloop()