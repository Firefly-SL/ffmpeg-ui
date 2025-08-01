import subprocess
import sys
import os
import platform

# get ffmpeg.exe if on windows or use golabl version if not
def get_ffmpeg():
    system = platform.system().lower()

    if system == "windows":
        if getattr(sys, 'frozen', False):
            return os.path.join(sys._MEIPASS, 'ffmpeg.exe')
        return os.path.join(os.path.dirname(__file__), 'ffmpeg.exe')

    return "ffmpeg"

ffmpeg = None

# simple converter
def convert_video(input_file, output_format):
    output_file = input_file.rsplit(".", 1)[0] + "_converted" + output_format
    subprocess.run([ffmpeg, "-i", input_file, output_file])