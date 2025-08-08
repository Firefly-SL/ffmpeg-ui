import sys
from modules import gui

console_mode = '--console' in sys.argv

# Creating app instance
app = gui.GUI(title="Converter",
              width=640,
              height=360,
              console=console_mode)

if __name__ == "__main__":
    app.run()
