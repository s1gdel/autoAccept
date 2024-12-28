import pyautogui
import time
import threading
import tkinter as tk
from tkinter import scrolledtext

# Image path
image_path = r"IMPAGE PATH HERE"

# Global flag to control the loop
running = True

# Function to run the auto-accept script
def autoAccept(log_text):
    global running
    while running:
        try:
            # Locate the image on the screen
            center_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.7)

            if center_location:
                pyautogui.moveTo(center_location)
                pyautogui.click()
                log_text.insert(tk.END, "Accepted!\n")
                log_text.yview(tk.END)  # Auto-scroll to the bottom
                break
            else:
                log_text.insert(tk.END, "Button not found, trying again.\n")
                log_text.yview(tk.END)
        except pyautogui.ImageNotFoundException:
            log_text.insert(tk.END, "Button not found\n")
            log_text.yview(tk.END)
        
        time.sleep(4)

# Function to start the auto-accept in a separate thread
def start_auto_accept(log_text):
    global running
    running = True  # Reset the running flag in case it was stopped
    # Start the autoAccept function in a separate thread to avoid blocking the GUI
    threading.Thread(target=autoAccept, args=(log_text,), daemon=True).start()

# Function to stop the script
def stop_auto_accept():
    global running
    log_text.insert(tk.END,"Stopping Program.")
    running = False  # Stop the loop in autoAccept

# Create the main GUI window
root = tk.Tk()
root.title("Auto Accept Script")
root.config(bg='black')

# Create a scrolled text box to display logs
log_text = scrolledtext.ScrolledText(root, width=40, height=15, wrap=tk.WORD, font=("Helvetica", 12), bg="black", fg="sky blue", insertbackground="sky blue")
log_text.grid(row=0, column=0, padx=10, pady=10)

# Create start button to start the auto-accept function
start_button = tk.Button(root, text="Start Auto Accept", command=lambda: start_auto_accept(log_text), bg="sky blue", fg="black", font=("Helvetica", 12))
start_button.grid(row=1, column=0, padx=10, pady=10)

# Create stop button to stop the auto-accept function
stop_button = tk.Button(root, text="Stop", command=stop_auto_accept, bg="sky blue", fg="black", font=("Helvetica", 12))
stop_button.grid(row=2, column=0, padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()
