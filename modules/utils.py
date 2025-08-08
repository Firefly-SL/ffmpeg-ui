import subprocess
import sys
import os
import platform

# get ffmpeg.exe if on windows or use golabl version if not
# def get_ffmpeg():
#     global system
#     system = platform.system().lower()

#     if system == "windows":
#         if getattr(sys, 'frozen', False):
#             return os.path.join(sys._MEIPASS, 'ffmpeg.exe')
#         return os.path.join(os.path.dirname(__file__), 'ffmpeg.exe')

#     return "ffmpeg"

def get_ffmpeg():
    global system
    system = platform.system().lower()

    if getattr(sys, 'frozen', False):
        if system == "windows":
            return os.path.join(sys._MEIPASS, 'ffmpeg.exe')
        else:
            return os.path.join(sys._MEIPASS, 'ffmpeg')

    if system == "windows":
        return os.path.join(os.path.dirname(__file__), 'ffmpeg.exe')
    else:
        return os.path.join(os.path.dirname(__file__), 'ffmpeg')


# define default browse path
def defualt_path():
    if system == "windows":
        return "C:/"
    else:
        return os.path.expanduser("/home/user-zero/Downloads") 


def change_filename(base_name, extension):
    counter = 1
    candidate = f"{base_name}_converted.{extension}"
    print(candidate)
    while os.path.exists(candidate):
        candidate = f"{base_name}_{counter}.{extension}"
        print(candidate)
        counter += 1
    return candidate

def assign_filename(input_file, output_format):
    if input_file.rsplit(".", 1)[0].endswith("_converted"):
        return change_filename(base_name=input_file.rsplit(".", 1)[0], extension=output_format)
    else:
        return input_file.rsplit(".", 1)[0] + "_converted." + output_format
    
# simple converter
def convert_and_output(command, input_file, output_file, ffmpeg):
    try:
        subprocess.run(
            command,
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


def convert_video(input_file, output_format, ffmpeg):
    output_file = assign_filename(input_file, output_format)
    command = [ffmpeg, "-i", input_file, "-c", "copy", output_file]
    return convert_and_output(command, input_file, output_file, ffmpeg)

def cmd_convert(list, input_file, ffmpeg):
    list[0] = ffmpeg
    index = list.index("$input_file")
    list[index] = input_file

    for item in reversed(list):
        if "." in item:
            output_format = item.split(".")[-1] # got output format
            output_file = assign_filename(input_file, output_format=output_format) #got output filename
            break
    
    index = list.index(f"$output_file.{output_format}")
    list[index] = output_file
    return convert_and_output(list, input_file, output_file, ffmpeg)
    