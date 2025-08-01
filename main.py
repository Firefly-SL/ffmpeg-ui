from modules import gui

# Creating app instance
app = gui.GUI(title="Converter",
              width=640,
              height=360)

if __name__ == "__main__":
    app.run()