import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.configure(bg="#1e1e1e")  # Window background

# Label
label = tk.Label(root, text="This is a label", bg="#1e1e1e", fg="white")
label.pack()

# Button
button = tk.Button(root, text="Click Me", bg="#333", fg="white", activebackground="#555", activeforeground="white")
button.pack()

# Console (ScrolledText)
console = scrolledtext.ScrolledText(root, bg="#000000", fg="#00FF00", insertbackground="white")
console.pack()

# Insert sample text
console.insert(tk.END, "Hello from the console...\n")

root.mainloop()
