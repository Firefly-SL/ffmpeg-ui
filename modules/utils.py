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

def change_filename(base_name, extension):
    counter = 1
    candidate = f"{base_name}_converted.{extension}"
    while os.path.exists(candidate):
        candidate = f"{base_name}_converted_{counter}.{extension}"
        counter += 1
    return candidate


# simple converter
def convert_video(input_file, output_format, ffmpeg):
    output_file = input_file.rsplit(".", 1)[0] + "_converted." + output_format

    if os.path.exists(output_file):
        output_file = change_filename(base_name=input_file.rsplit(".", 1)[0], extension=output_format)
    
    try:
        subprocess.run(
            [ffmpeg, "-i", input_file, "-c", "copy", output_file],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return f"File converted as: {output_file}"
    except FileNotFoundError:
        return "Error: ffmpeg executable not found. Report this error."
    except subprocess.CalledProcessError as e:
        return f"ffmpeg encountered an error:\n{e.stderr}" #important
    except Exception as e:
        return f"An unexpected error occurred: {e}"