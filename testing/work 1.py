import tkinter as tk
import customtkinter as ctk

# Initialize the main window
window = ctk.CTk()
window.geometry("800x600")

# Set the main window background color (optional)
window.configure(bg="#282828")  # Darker background for the window

# Create the header frame (this will be your tab area)
header_frame = ctk.CTkFrame(window, width=800, height=50, corner_radius=0, fg_color="#1E1E1E")  # Darker tab
header_frame.place(x=0, y=0)

# Add buttons to the header frame
button1 = ctk.CTkButton(header_frame, text="Home", width=80, height=40)
button1.place(x=10, y=5)

button2 = ctk.CTkButton(header_frame, text="Settings", width=80, height=40)
button2.place(x=100, y=5)

button3 = ctk.CTkButton(header_frame, text="About", width=80, height=40)
button3.place(x=190, y=5)

# Example content below the header
content_frame = ctk.CTkFrame(window, width=800, height=550, corner_radius=0)
content_frame.place(x=0, y=50)

label = ctk.CTkLabel(content_frame, text="Main Content Area", font=("Roboto", 24))
label.pack(pady=20)

# Run the main event loop
window.mainloop()
