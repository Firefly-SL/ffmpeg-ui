import subprocess
import sys
import os
import platform

# get ffmpeg.exe if on windows or use golabl version if not
def get_ffmpeg():
    global system
    system = platform.system().lower()

    if system == "windows":
        if getattr(sys, 'frozen', False):
            return os.path.join(sys._MEIPASS, 'ffmpeg.exe')
        return os.path.join(os.path.dirname(__file__), 'ffmpeg.exe')

    return "ffmpeg"


# define default browse path
def defualt_path():
    if system == "windows":
            return "C:/"
    else:
        return os.path.expanduser("~") 


# simple converter
def convert_video(input_file, output_format, ffmpeg):
    output_file = input_file.rsplit(".", 1)[0] + "_converted." + output_format
    subprocess.run([ffmpeg, "-i", input_file, "-c", "copy", output_file])