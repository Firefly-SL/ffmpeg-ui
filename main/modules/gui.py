import tkinter as tk
from tkinter import filedialog

class GUI:
    def __init__(self, title):
        self.root = tk.Tk()
        self.root.title(title)

        self.browse_button = tk.Button(self.root, text="Browse File", command=self.select_file)
        self.browse_button.pack(pady=20)

    def select_file(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            print(f"Selected file: {filepath}")

    def run(self):
        self.root.mainloop()
