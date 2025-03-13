import tkinter as tk
from tkinter import ttk
import psutil

# Creating Class for GUI
class StorageCheckerGUI:

    # Initialize the root window
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    # Create widgets
    def create_widgets(self):
        self.storage_label = ttk.Label(self.root, text="")
        self.storage_label.pack(pady=10)

        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

        self.percentage_label = ttk.Label(self.root, text="")
        self.percentage_label.pack(pady=10)

    # Create window
    def create_window(self):
        self.show_storage_info()

    # Show storage information
    def show_storage_info(self):
        usage = psutil.disk_usage('/')
        total, used, free = usage.total, usage.used, usage.free

        # Convert bytes to GB
        total_gb = total / (1024 ** 3)
        free_gb = free / (1024 ** 3)
        used_percentage = usage.percent

        # Update the labels
        self.storage_label.config(text=f"Total / Free: {total_gb:.2f} GB / {free_gb:.2f} GB")
        self.progress['value'] = used_percentage
        self.percentage_label.config(text=f"Used: {used_percentage:.2f}%")

# Main function
def main():
    # Create the root window
    root = tk.Tk()
    root.title("Storage Checker")
    
    # Create an object of the class
    app = StorageCheckerGUI(root)
    app.create_window()
    
    # Run the main loop
    root.mainloop()

# Entry point of the program
if __name__ == "__main__":
    main()