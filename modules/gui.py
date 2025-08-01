import tkinter as tk
from tkinter import filedialog
from modules import utils

ffmpeg = utils.get_ffmpeg()

class GUI:
    def __init__(self, title, width, height):
        # Setting the window up
        self.root = tk.Tk()
        self.root.title(title)

        # Frame to center objects
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True)
        # Calling window centering method
        self.center_window(width,height)

        self.filepath = "No file selected"

        # Defining Objects
        self.browse_button = tk.Button(button_frame, text="Browse File", command=self.select_file)
        self.label = tk.Label(button_frame, text=self.filepath)
        self.export_button = tk.Button(button_frame, text="Convert", command=self.export_file)

        # Changing placement of objects
        self.browse_button.pack(pady=5)
        self.label.pack(pady=5)
        self.export_button.pack(pady=25)
    
    # Window centering method
    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")

## Object Methods ##
    def select_file(self):
        self.filepath = filedialog.askopenfilename(
            initialdir = utils.defualt_path(),
            title = "Select a file",
            filetypes = (("MP4 files", "*.mp4"), ("All files", "*.*")))
        
        self.label.config(text=f"Selected: {self.filepath}")

    def export_file(self):
        # arg (input_file, file_format)
        utils.convert_video(self.filepath, '.mp4', ffmpeg)
        self.label.config(text=f"File Converted")

    def run(self):
        self.root.mainloop()