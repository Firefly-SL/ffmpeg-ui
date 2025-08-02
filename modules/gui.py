import tkinter as tk
from tkinter import filedialog
from modules import utils
import threading
import time

ffmpeg = utils.get_ffmpeg()

class GUI:
    def __init__(self, title, width, height):
        # colors (higher the number the brighter)
        bg0 = "#181A1B" #black darker (console bg)
        bg1="#26292C"  #black (root, label bg)
        bgbutton0 = "#495057" #gray dark (buttons bg)
        bgbutton1 = "#6C757D" #gray (button bg active)
        text0 = "#ADB5BD" #white darker (console fg)
        text1 = "#CED4DA" #white (label, button fg)
        text2 = "#DEE2E6" #whitest (button fg active)

        # Setting the window up
        self.root = tk.Tk()
        self.root.title(title)
        self.root.configure(bg=bg1)

        # Frame to center objects
        # button_frame = tk.Frame(self.root)
        # button_frame.pack(expand=True)
        # Calling window centering method
        self.center_window(width,height)

        self.filepath = None
        # Track start time
        self.start_time = None
        self.timer_running = False



        # -------- TOP FRAME (Buttons) --------
        top_frame = tk.Frame(self.root, bg=bg1)
        top_frame.pack(fill=tk.X, padx=10, pady=10)

        browse_btn = tk.Button(top_frame, text="Browse", command=self.select_file, bg=bgbutton0, fg=text1, activebackground=bgbutton1, activeforeground=text2)
        convert_btn = tk.Button(top_frame, text="Convert", command=self.start_conversion, bg=bgbutton0, fg=text1, activebackground=bgbutton1, activeforeground=text2)

        browse_btn.pack(side=tk.LEFT, padx=5)
        convert_btn.pack(side=tk.LEFT, padx=5)

        # -------- MIDDLE FRAME (Console Area) --------
        middle_frame = tk.Frame(self.root, bg=bg1)
        middle_frame.pack(fill=tk.BOTH, expand=True)

        self.console = tk.Text(middle_frame, height=10, bg=bg0, fg=text0, selectbackground=bg0, selectforeground=text0)
        self.console.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.console.config(state="disabled")

        # -------- BOTTOM FRAME (Console Area) --------
        bottom_frame = tk.Frame(self.root, bg=bg1)
        bottom_frame.pack(fill=tk.X, padx=5, pady=5)

        self.stopwatch_label = tk.Label(bottom_frame, text="Time: 0.000", bg=bg1, fg=text1)
        self.stopwatch_label.pack(side="left")



    # Window centering method
    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def start_conversion(self):
        if not self.filepath:
            self.log("No file selected.")
            return
        
        self.timer_running = False
        self.stopwatch_label.config(text="Time: 0.000")

        # Start timer
        self.start_time = time.time()
        self.timer_running = True
        self.update_timer()

        # Start background thread for conversion
        thread = threading.Thread(target=self.convert_file)
        thread.start()

    def update_timer(self):
        if self.timer_running:
            self.elapsed = time.time() - self.start_time
            self.stopwatch_label.config(text=f"Time: {self.elapsed:.3f}")
            self.root.after(10, self.update_timer)  # Update every 10ms.
        


## Object Methods ##
    def select_file(self):
        self.filepath = filedialog.askopenfilename(
            initialdir = utils.defualt_path(),
            title = "Select a file",
            filetypes = (("Supported files", "*.mkv *.mp4 *.m4v *.mov"), ("All files", "*.*")))
   
        if self.filepath:
            self.log(f"Selected: {self.filepath}")
        else:
            self.log("Select a file")

    def convert_file(self):
        # arg (input_file, file_format. ffmpeg_path)
        result = utils.convert_video(self.filepath, '.mp4', ffmpeg)
        self.log(result)

        # Stop timer
        self.timer_running = False
        self.log(f"Conversion finished in {self.elapsed:.3f} seconds\n")

    def log(self,message):
        self.console.config(state="normal")
        self.console.insert(tk.END, message + "\n")
        self.console.see(tk.END)
        self.console.config(state="disabled")


    def run(self):
        self.root.mainloop()