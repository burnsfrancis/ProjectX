import customtkinter
import ctypes
from admin import request_admin_privileges
from Functions.tempfile import delete_temp_files
from Functions.powermanagement import performance_mode
from Functions.diskcleanup import cleanup_disk

# Request admin privileges when the app starts
request_admin_privileges()

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# Application frame
app = customtkinter.CTk()
app.geometry("600x400")  # Sets a fixed window size
app.title("TBA")  # Title of the window

# Main frame
main_frame = customtkinter.CTkFrame(app)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Title Label
title = customtkinter.CTkLabel(
    main_frame, 
    text="TBA", # Title in the frame
    font=("Arial", 20, "bold")
)
title.pack(pady=(10, 20))

# Creates a frame for switches
switch_frame = customtkinter.CTkFrame(main_frame)
switch_frame.pack(pady=10, padx=10, fill="x")

# Switch+Label defaults
def create_switch_with_label(parent, text, row):
    label = customtkinter.CTkLabel(
        parent,
        text=text,
        font=("Arial", 14)
    )
    label.grid(row=row, column=0, padx=(10, 5), pady=10, sticky="w")

    switch = customtkinter.CTkSwitch(
        parent,
        text="",
        width=50,
        height=30
    )
    switch.grid(row=row, column=1, padx=(5, 10), pady=10, sticky="e")
    return switch

# Create switches using the function
switchTemp = create_switch_with_label(switch_frame, "Delete Temporary Files", 0)
switchPower = create_switch_with_label(switch_frame, "Enable Performance Mode", 1)
switchDisk = create_switch_with_label(switch_frame, "Run Disk Cleanup", 2)

# Adjusts column weights to push switches to the right
switch_frame.grid_columnconfigure(0, weight=1)  # Label column expands
switch_frame.grid_columnconfigure(1, weight=0)  # Switch column does not expand

# Defining the execution command
def execute():
    tasks = {
        "Temp Files": (switchTemp, delete_temp_files),
        "Power Management": (switchPower, performance_mode),
        "Disk Cleanup": (switchDisk, cleanup_disk),
    }

    any_task_selected = False
    for task_name, (switch, action) in tasks.items():
        if switch.get() == 1:
            try:
                action()
                print(f"{task_name}: Task executed successfully.")
                any_task_selected = True
            except Exception as e:
                print(f"{task_name}: Error - {e}")
                ctypes.windll.user32.MessageBoxW(0, f"Error executing {task_name}: {e}", str(app.title), 0)
        else:
            print(f"{task_name}: Switch is off, no action taken.")

    if not any_task_selected:
        ctypes.windll.user32.MessageBoxW(0, "No tasks selected. Please select a task to execute.", str(app.title), 0)
    else:
        ctypes.windll.user32.MessageBoxW(0, "All selected tasks completed successfully.", str(app.title), 0)

# Execute Button
button = customtkinter.CTkButton(
    main_frame,
    text="Execute",
    width=200,
    height=40,
    font=("Arial", 14, "bold"),
    command=execute
)
button.pack(pady=20)

# Running the application
app.mainloop()