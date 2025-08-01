import modules.functions as function
from modules.gui import GUI

app = GUI("Converter")

ffmpeg = function.get_ffmpeg()

input_file = app.select_file()

# arg (input_file, file_format)
#function.convert_video()

if __name__ == "__main__":
    app.run()